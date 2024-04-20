import { useLoaderData } from 'react-router-dom';

export function NoteDetail() {
  const note = useLoaderData();
  return (
    <div className="p-10 rounded-lg shadow-lg mx-28 border-4 border-solid border-our_dark">
      <h1 className="text-3xl text-our_dark font-bold tracking-tight mb-4 border-b border-solid border-our_dark pb-4">
        {note.title.replace(/^"|"$/g, '')}
      </h1>
      <p className="text-md text-gray-700 py-1">
        Created on: {new Date(note.created_at).toLocaleDateString()}
      </p>
      <p className="text-lg text-gray-700 mt-4">
        {note.content}
      </p>
    </div>
  );
}