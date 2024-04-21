import {useLoaderData} from 'react-router-dom';
import {SimilarGalery} from "../components/SimilarGalery";
import Markdown from "react-markdown";


export function NoteDetail() {
  const note = useLoaderData();
  return (
    <>
      <div className="p-10 rounded-lg shadow-lg mx-28 border-4 border-solid border-our_dark mb-8">
        <h1 className="text-3xl text-our_dark font-bold tracking-tight mb-4 border-b border-solid border-our_dark pb-4">
          {note.title.replace(/^"|"$/g, '')}
        </h1>
        <p className="text-md text-gray-700 py-1">
          Created on: {new Date(note.created_at).toLocaleDateString()}
        </p>
        <p className="">
          <Markdown className="markdown">{note.markdown}</Markdown>
        </p>
      </div>
      <div className="mx-28 justify-centre ">
        <div className="mb-4">
          <h4
            className="text-xl text-center text-our_dark font-bold tracking-tight mb-1 border-solid border-our_dark pb-4 drop-shadow-sm">
            {"Similar notes"}
          </h4>
        </div>
        <SimilarGalery meeting_id={note.meeting_id}/>
      </div>
    </>
  );
}