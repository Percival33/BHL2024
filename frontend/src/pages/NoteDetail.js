import { useLoaderData } from 'react-router-dom';

export function NoteDetail() {
  const note = useLoaderData();
  return (
    <div className="p-6 bg-our_dark border-4 border-our_magenta rounded-lg shadow-lg">
      <h1 className="text-3xl font-bold tracking-tight text-gray-900 dark:text-white mb-4">
        {note.title.replace(/^"|"$/g, '')}
      </h1>
      <p className="text-sm text-gray-700 dark:text-gray-200">
        Created on: {new Date(note.created_at).toLocaleDateString()}
      </p>
      <p className="text-lg text-gray-700 dark:text-gray-400 mt-4">
        {note.content}
      </p>
    </div>
  );
}