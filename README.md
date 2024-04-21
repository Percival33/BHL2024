# BHL 2024
## Team
Ale to ty dzwonisz

- [Dawid Kaszyński](https://github.com/dawidkasz)
- [Mikołaj Szawerda](https://github.com/MikolajSzawerda)
- [Krzysztof Fijałkowski](https://github.com/kfijalkowski1)
- [Marcin Jarczewski](https://github.com/Percival33)

## Idea

Framework for recording online and offline meetings together with preparing summeries and proposing notes from previous meetings that have similar semantic meaning.

The main point of interaction with the user is browser extension that records microphone and system audio output and sends data to backened. System after processing audio returns most suitable notes in real time and allows to redirect to separate panel that allows to read content of past summaries and proposes similar notes. Panel allows also full-text search. 

## Overview 

### Browser Extension
- record microphone and system audio and sends it for processing
- receives in real time similar notes
- encorporates tailwindCSS and vanilla JS and chromiumAPI 
- passes WCAG accesibility requirements

### Backened
- uses OpenAI Whsiper speech-to-text model to create transcript
- uses GPT to summarize meeting and computes embedings to represent high dimensional features  to retrive similar semanticly notes
- stores sumarized notes and their embeddings in databases

### Frontend
- presents all notes
- present note details and similiar notes to current one
- allows full-text search capabilities


## Technologies 
- browser extension - tailwindCSS and vanilla JS and chromiumAPI 
- backened - openAI Whisper, ChatGPT, langchain, chromaDB, mongoDB, fastApi
- frontend - React, tailwindCSS, html and vanilaJS

## Instalation guide

- browser extension
```shell
# open browser 
# go to extensions and turn on developer mode
# load unpacked `extension folder`
```

- backend
```shell
cp .env.example .env
# INSERT OPENAI_API_KEY
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
docker compose up
```

- webpage
```shell
npm install
```

## Future ideas
- create or fine tune specific purpose model