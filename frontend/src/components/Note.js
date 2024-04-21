import {Link} from "react-router-dom";
import { format } from 'date-fns';

export const truncate = (text, length = 100) => {
  if (text.length > length) {
    return text.substring(0, length) + '...';  // Appends ellipsis to indicate truncation
  }
  return text;
};


export function Note({meeting_id, title, created_at, content}) {
  console.log(title);
  return (
    <Link
      to={`/note/${meeting_id}`}
      className="block w-full p-6 bg-our_dark outline rounded-lg shadow hover:outline-4 hover:outline-our_magenta min-h-60 shadow-md hover:shadow-xl"
    >
      <h5 className="mb-2 text-2xl font-bold tracking-tight text-white">
        {title.replaceAll("\"", "")}
      </h5>
      <p className="font-normal text-gray-200 mb-2">{format(new Date(created_at), 'dd.MM.yyyy')}</p>
      <p className="font-normal text-gray-400 items-end">{truncate(content, 200)}</p>
    </Link>
  );
}
