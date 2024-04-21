import {NoteSimilar} from "./NoteSimilar";
import {useEffect, useState} from "react";

const baseApiUrl = "http://localhost:8080"; // Adjusted as necessary

function splitNotesAlternately(notes) {
  const listA = [];
  const listB = [];

  notes.forEach((note, index) => {
    if (index % 2 === 0) {
      listA.push(note);
    } else {
      listB.push(note);
    }
  });

  return {listA, listB};
}

const fetchData = async (meeting_id) => {
  // Uncomment when ready to fetch from API
  const resp = await fetch(baseApiUrl + "/suggestions/" + meeting_id);
  return await resp.json();
}

export function SimilarGalery({meeting_id}) {
  const [similarNotes, setSimilarNotes] = useState([]);
  useEffect(() => {

    fetchData(meeting_id).then(data => {
      setSimilarNotes(data);
    }).catch(error => {
      console.error("Failed to fetch data", error);
    });
  }, [meeting_id]);

  const {listA, listB} = splitNotesAlternately(similarNotes);

  return (
    <div className="justify-center flex place-self-start flex-row gap-0">
      {/*grid grid-cols-2 gap-2*/}
      <div className="justify-center items-start flex flex-col">
        {listA.map((note) => (
          <NoteSimilar meeting_id={note.meeting_id} title={note.title} similarity={note.similarity}
                       key={note.meeting_id}/>
        ))}
      </div>
      <div className="justify-center place-self-start flex flex-col">
        {listB.map((note) => (
          <NoteSimilar meeting_id={note.meeting_id} title={note.title} similarity={note.similarity}
                       key={note.meeting_id}/>
        ))}
      </div>

    </div>
  );
}
