import {apiEndpoints, headerConfig, responseKeys} from "./constants.js";

export let mediaRecorder;
let audioChunks = [];
const CHUNK_INTERVAL = 10_000;
const output = new AudioContext();
const validateBody = (body) => {
    const currentMeetingId = sessionStorage.getItem(headerConfig.sessionKey)
    if (!currentMeetingId) {
        return;
    }
    if (!(responseKeys.sessionKey in body)) {
        throw new Error("Headers from API doesn't contains meeting id");
    }
    const receivedMeetingId = body[responseKeys.sessionKey] || null;
    if (currentMeetingId !== receivedMeetingId) {
        throw new Error('Meeting ID has changed');
    }
}

function uploadAudioChunk(audioBlob) {
    const formData = new FormData();
    formData.append('audio_file', audioBlob, 'recording.mp3');
    const sessionId = sessionStorage.getItem(headerConfig.sessionKey) || null;
    return fetch(apiEndpoints.uploadAudio, {
        method: 'POST',
        body: formData,
        headers: sessionId ? {[headerConfig.sessionKey]: sessionId} : {}
    })
}

const sendAudioChunk = async (audioBlob) => {

    const response = await uploadAudioChunk(audioBlob);
    if (!response.ok) {
        throw new Error('Error when uploading chunk');
    }
    const responseBody = await response.json();
    validateBody(responseBody);
    const receivedMeetingId = responseBody[responseKeys.sessionKey] || null;
    if (!sessionStorage.getItem(headerConfig.sessionKey)) {
        sessionStorage.setItem(headerConfig.sessionKey, receivedMeetingId);
    }
}

const handleChunk = async (event) => {
    if (event.data.size <= 0) {
        return;
    }
    audioChunks.push(event.data);
    try {
        await sendAudioChunk(new Blob(audioChunks, {type: 'audio/mp3'}));
    } catch (e) {
        console.log("Error when sending chunk", e);
    }
}

function mixAudioStreams(micStream) {
    const micSource = output.createMediaStreamSource(micStream);

    const destination = output.createMediaStreamDestination();

    micSource.connect(destination);
    tabSource.connect(destination)
    return destination.stream;
}

async function getMixedStream() {
    const micStream = await navigator.mediaDevices.getUserMedia({audio: true})
    return mixAudioStreams(micStream)
}


export const startMediaRecorder = async () => {
    const mixedStream = await getMixedStream();

    mediaRecorder = new MediaRecorder(mixedStream);
    mediaRecorder.ondataavailable = handleChunk;
    mediaRecorder.onstop = () => {
        audioChunks = [];
        console.log("Stopped recording");
    };
    mediaRecorder.start(CHUNK_INTERVAL);
    console.log("Started audio recording")
}

export const getNewSuggestions = async () => {
    const meetingId = sessionStorage.getItem(headerConfig.sessionKey);
    if (!meetingId) {
        return;
    }
    const resp = await fetch(apiEndpoints.getSuggestions(meetingId));
    return await resp.json();
}
let tabStream;
let tabSource;
chrome.tabCapture.getMediaStreamId({}, async (streamId) => {
    console.log("HELLO")
    tabStream = await navigator.mediaDevices.getUserMedia({
            audio: {
                mandatory: {
                    chromeMediaSource: "tab",
                    chromeMediaSourceId: streamId,
                },
            },
            video: false
        }
    )
    tabSource = output.createMediaStreamSource(tabStream);
    tabSource.connect(output.destination);
});