# BHL 2024 Hackathon Documentation
## Team "Ale to ty dzwonisz"

### Members
- [Dawid Kaszyński](https://github.com/dawidkasz)
- [Mikołaj Szawerda](https://github.com/MikolajSzawerda)
- [Krzysztof Fijałkowski](https://github.com/kfijalkowski1)
- [Marcin Jarczewski](https://github.com/Percival33)

## Project Overview: Unified Meeting Framework

### Executive Summary
Our project introduces an innovative framework designed to enhance meeting productivity by seamlessly integrating the recording, summarization, and retrieval of both online and offline meetings. Utilizing a browser extension, our system captures audio inputs and leverages cutting-edge AI technologies to process, summarize, and contextually link meeting content, presenting it through a highly accessible user interface.

### System Components

#### Browser Extension
- **Functionality**: Captures microphone and system audio for real-time processing.
- **Features**: Syncs processed data to provide contextually relevant notes in real time.
- **Technology**: Developed using TailwindCSS, Vanilla JavaScript, and Chromium APIs.
- **Accessibility**: Compliant with WCAG accessibility standards, ensuring usability for all users.

#### Backend
- **Speech-to-Text**: Employs OpenAI's Whisper model to accurately transcribe audio data.
- **Content Summarization and Analysis**: Utilizes GPT models to summarize meetings and compute embeddings for semantic linkage of notes.
- **Data Management**: Stores summaries and their associated embeddings in a structured database for efficient retrieval.
- **Technology Stack**: OpenAI Whisper, ChatGPT, LangChain, ChromaDB, MongoDB, FastAPI.

#### Frontend
- **Display**: Showcases all meeting notes and provides detailed views of specific entries.
- **Functionality**: Supports searching across all notes and dynamically presents notes similar to the current focus.
- **Technology**: Built with React, TailwindCSS, HTML, and Vanilla JavaScript.

### Technologies Employed
- **Browser Extension**: TailwindCSS, Vanilla JavaScript, Chromium APIs.
- **Backend**: OpenAI Whisper, ChatGPT, LangChain, ChromaDB, MongoDB, FastAPI.
- **Frontend**: React, TailwindCSS, HTML, Vanilla JavaScript.

## Installation Guide

### Browser Extension
```shell
# Open your browser and navigate to the extensions page.
# Enable developer mode.
# Load the unpacked extension from the 'extension folder'.
```

### Backend Setup
```shell
cp .env.example .env
# Insert your OPENAI_API_KEY here.
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up
```

### Webpage Deployment
```shell
npm install
npm start
```

## Future Development
- **AI Model Enhancement**: Investigate the creation or fine-tuning of specialized models tailored for specific types of meetings and industries.

### Summary
Our framework is designed to transform how individuals and organizations manage their meeting workflows by automating the capture, analysis, and retrieval of meeting content. By integrating state-of-the-art AI technologies, we provide a scalable solution that enhances productivity and facilitates better decision-making processes. This proposal outlines our commitment to delivering a robust, accessible, and technologically advanced system for effective meeting management.