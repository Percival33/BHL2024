import React, { useState, useEffect } from 'react';
import { Note} from "./Note";

const baseApiUrl = "http://localhost:8080"; // Adjusted as necessary

const filterDataByTitlePhrase = (responses, phrase) => {
    return responses.filter(response => response.title.toLowerCase().includes(phrase.toLowerCase()));
};

const fetchData = async (phrase = "") => {
    // Uncomment when ready to fetch from API
    const resp = await fetch(baseApiUrl+"/note");
    const data = await resp.json();
    console.log(data);
    return filterDataByTitlePhrase(data, phrase);
}

export function Gallery({ searchTerm }) {
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        fetchData(searchTerm).then(setNotes).catch(error => console.error("Failed to fetch data", error));
    }, [searchTerm]);

    return (
        <div className="flex flex-wrap justify-center w-full gap-4">
            {notes.map((note) => (
                <div className="w-1/2 md:w-1/3 lg:w-1/4 p-2" key={note.meeting_id}>
                    <Note {...note} />
                </div>
            ))}
        </div>
    );
}
