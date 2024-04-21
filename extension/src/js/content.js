import {getNewSuggestions, mediaRecorder, startMediaRecorder} from "./capture.js";

const captureButton = document.getElementById("capture-btn");
const captureIcon = document.getElementById("recordingIcon");
const timerDiv = document.getElementById("timer");
const captureButtonText = document.getElementById("capture-btn-text");
const suggestionsDiv = document.getElementById("suggestions");

sessionStorage.clear();

let intervalId;
let elapsedSeconds = 0;
const SUGGESTIONS_RATE = 3_000;
let suggestionsInterval = null;


function createDataRow(item, index) {
    const row = document.createElement("li");
    const percentage = Math.round(100 * item.similarity);
    row.className = 'data-row  rounded-lg bg-our_dark p-4 transition ease-in-out duration-300 hover:bg-our_gray';
    row.dataset.index = index;

    row.innerHTML = `
            <a href="${item.uri}" target="_blank" class="items-center justify-between flex ">
                <div>
                    <div class="grid grid-rows-2 items-center">
                        <div class="font-bold text-our_white text-2xl">${item.title}</div>
                        <div class="text-our_white truncate w-96">${item.content}</div>
                    </div>
                </div>
                <div>
                    <div class="w-40 ml-4 text-our_white">
                        <div class="flex justify-end mb-1">
                            <span class="text-sm font-medium">${percentage}% match</span>
                        </div>
                        <div class=" bg-our_white rounded-full h-2.5">
                            <div class="bg-our_magenta h-2.5 rounded-full" style="width: ${percentage}%"></div>
                        </div>
                    </div>
                </div>
            </a>
    `;
    return row;
}


const endCapturing = () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
    }

    clearInterval(suggestionsInterval);
    clearInterval(intervalId);
    sessionStorage.clear();
    handleTimerStop();
    handleRecordButtonStop();

    suggestionsInterval = null;
    suggestionsDiv.innerHTML = "";
}


function updateTime() {
    elapsedSeconds++;
    const hours = Math.floor(elapsedSeconds / 3600);
    const minutes = Math.floor((elapsedSeconds % 3600) / 60);
    const seconds = elapsedSeconds % 60;

    timerDiv.textContent =
        `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}


const handleRecordButtonStart = () => {
    captureButtonText.innerText = "Stop";
    captureIcon.classList.add('blinking')
}

const handleRecordButtonStop = () => {
    captureIcon.classList.remove('blinking')
    captureButtonText.innerText = "Capture";
}

const handleTimerStart = () => {
    intervalId = setInterval(updateTime, 1000);
}

const handleTimerStop = () => {
    elapsedSeconds = 0
    timerDiv.textContent = "00:00:00"

}

const updateSuggestions = (data) => {
    suggestionsDiv.innerHTML = '';
    if (data && suggestionsInterval) {
        data
            .map((row, index) => createDataRow(row, index))
            .forEach(row => suggestionsDiv.appendChild(row))
    }
}

const startSuggestions = async () => {
    const suggestions = await getNewSuggestions();
    console.log(suggestions)
    updateSuggestions(suggestions);
    suggestionsInterval = setInterval(() => getNewSuggestions()
        .then(data => updateSuggestions(data))
        .catch(e => console.log(e)), SUGGESTIONS_RATE);
}


captureButton.onclick = async () => {
    if (!suggestionsInterval) {
        handleTimerStart();
        handleRecordButtonStart();
        await startMediaRecorder();
        await startSuggestions();
        return;
    }

    endCapturing();
}

