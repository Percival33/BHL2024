import {Link} from "react-router-dom";
import { format } from 'date-fns';

export function Note({meeting_id, title, created_at, description}) {
  console.log(title);
  return (
    <Link
      to={`/note/${meeting_id}`}
      className="block w-full p-6 bg-our_dark border-4 border-our_dark rounded-lg shadow hover:border-our_magenta min-h-60"
    >
      <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        {title.replaceAll("\"", "")}
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-200">{format(new Date(created_at), 'dd.MM.yyyy')}</p>
      <p className="font-normal text-gray-700 dark:text-gray-400">{description}</p>
    </Link>
  );
}
