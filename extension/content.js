const baseApiUrl = "http://localhost:8000";

const captureButton = document.getElementById("capture-btn");
const suggestionsDiv = document.getElementById("suggestions");
const audioPlayback = document.getElementById('audio-playback');
const output = new AudioContext();

const suggestionsTimeout = 3000;

let mediaRecorder;

const renderSuggestionLine = (text) => {
    return `<div class="font-sans text-base">- ${text}</div>`
}

let suggestionsInterval = null;

const getNewSuggestions = async () => {
    const resp = await fetch(baseApiUrl + "/matching_notes");
    const data = await resp.json();

    const rows = data.map(row => renderSuggestionLine(row));

    suggestionsDiv.innerHTML = rows.join("");
}


const endCapturing = () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
    }

    clearInterval(suggestionsInterval);
    suggestionsInterval = null;
    captureButton.innerText = "Capture";
    suggestionsDiv.innerHTML = "";
}

const sendAudioBlob = (audioBlob) => {
    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.mp3');
    const sessionId = sessionStorage.getItem('sessionId');
    fetch(baseApiUrl + "/upload_audio", {
        method: 'POST',
        body: formData,
        headers: sessionId ? {'sessionId': sessionId} : {}
    })
        .then(response => {
            if (response.headers.has('sessionId')) {
                const receivedSessionId = response.headers.get("sessionId");
                sessionStorage.setItem('sessionId', receivedSessionId);
            }
            return response.json()
        })
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function mixAudioStreams(micStream, tabStream) {
    const audioContext = new AudioContext();
    const source1 = audioContext.createMediaStreamSource(micStream);
    const source2 = audioContext.createMediaStreamSource(tabStream);

    const destination = audioContext.createMediaStreamDestination();
    source1.connect(destination);
    source2.connect(destination);

    return destination.stream;
}

async function getMixedStream(streamId) {
    const tabStream = await navigator.mediaDevices.getUserMedia({
            audio: {
                mandatory: {
                    chromeMediaSource: "tab",
                    chromeMediaSourceId: streamId,
                },
            },
            video: false
        }
    );
    const source = output.createMediaStreamSource(tabStream);
    source.connect(output.destination);
    const micStream = await navigator.mediaDevices.getUserMedia({audio: true})
    return mixAudioStreams(micStream, tabStream)
}


const startCapturing = () => {
    let audioChunks = [];
    chrome.tabCapture.getMediaStreamId({}, (streamId) => {
        getMixedStream(streamId)
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start(5000);
                console.log("Started audio recording")

                mediaRecorder.ondataavailable = event => {
                    if (!event.data.size) {
                        return;
                    }
                    audioChunks.push(event.data);
                    const audioBlob = new Blob(audioChunks, {type: 'audio/mp3'});
                    sendAudioBlob(audioBlob);

                    const audioUrl = URL.createObjectURL(audioBlob);
                    console.log(audioUrl);
                };

                mediaRecorder.onstop = () => {
                    console.log("Stopped recording");
                };
            })
            .catch(e => {
                console.error('Error capturing audio:', e);
            });
    })


    getNewSuggestions();
    suggestionsInterval = setInterval(getNewSuggestions, suggestionsTimeout);
    captureButton.innerText = "Stop Capturing";
}


captureButton.onclick = () => {
    if (suggestionsInterval == null) {
        startCapturing()
    } else {
        endCapturing();
    }
}