const baseApiUrl = "http://localhost:8000";

const captureButton = document.getElementById("capture-btn");
const captureIcon = document.getElementById("recordingIcon");
const timerDiv = document.getElementById("timer");
const notesList = document.getElementById("sugUL");
const captureButtonText = document.getElementById("capture-btn-text");
const suggestionsDiv = document.getElementById("suggestions");
const audioPlayback = document.getElementById('audio-playback');

const suggestionsTimeout = 3000;

let mediaRecorder;
let intervalId;
let elapsedSeconds = 0;
const renderSuggestionLine = (text) => {
    return `<div class="font-sans text-base">- ${text}</div>`
}

let suggestionsInterval = null;
let mockData = [
    {
        reflink: "https://twitter.com/mamodrzejewski",
        title: "Hello Happy World",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nunc tortor, convallis vitae molestie in, posuere in nisi. Pellentesque habitant."
    },
    {
        reflink: "https://twitter.com/mamodrzejewski",
        title: "Hello Sad World",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nunc tortor, convallis vitae molestie in, posuere in nisi. Pellentesque habitant."
    },
]

function createDataRow(item, index) {
    const row = document.createElement("li");
    row.className = 'data-row flex rounded-lg bg-dark  items-center p-2 px-6';
    row.dataset.index = index;

    row.innerHTML = `
                <a href=${item.reflink}>
                    <div class="grid grid-rows-2 items-center">
                        <div class="font-bold text-white">${item.title}</div>
                        <div class="text-white">${item.description}</div>
                    </div>
                </a>
            </li>
    `;
    return row;
}

//TODO back to API
const getNewSuggestions = async () => {
    // const resp = await fetch(baseApiUrl + "/matching_notes");
    // const data = await resp.json();

    // const rows = data.map(row => renderSuggestionLine(row));
    suggestionsDiv.innerHTML = "";
    mockData
        .map((row, index) => createDataRow(row, index))
        .forEach(row => suggestionsDiv.appendChild(row))
}


const endCapturing = () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
    }

    clearInterval(suggestionsInterval);
    suggestionsInterval = null;
    captureButtonText.innerText = "Capture";
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

function updateTime() {
    elapsedSeconds++;
    const hours = Math.floor(elapsedSeconds / 3600);
    const minutes = Math.floor((elapsedSeconds % 3600) / 60);
    const seconds = elapsedSeconds % 60;

    // Format time to HH:MM:SS
    timerDiv.textContent =
        `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}


const startCapturing = () => {
    let audioChunks = [];

    navigator.mediaDevices.getUserMedia({audio: true, video: false})
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start(1000);
            console.log("Started audio recording")

            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
                console.log("Chunk")
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

    getNewSuggestions();
    suggestionsInterval = setInterval(getNewSuggestions, suggestionsTimeout);
    captureButtonText.innerText = "Stop";
}


captureButton.onclick = () => {
    if (!suggestionsInterval) {
        intervalId = setInterval(updateTime, 1000);
        captureIcon.classList.add('blinking')
        startCapturing();
    } else {
        clearInterval(intervalId)
        elapsedSeconds = 0
        timerDiv.textContent = "00:00:00"
        captureIcon.classList.remove('blinking')

        endCapturing();
    }
}


