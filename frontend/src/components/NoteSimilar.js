import {Link} from "react-router-dom";
import {format} from 'date-fns';

export function NoteSimilar({meeting_id, title, similarity}) {
  var similarityPercentage = Math.floor(similarity * 100);
  console.log("meeting_id: " + meeting_id + " title: " + title + " similarity: " + similarity + " similarityPercentage: " + similarityPercentage);
  return (

    <Link
      to={`/note/${meeting_id}`}
      className="block w-3/4 p-7 rounded-lg shadow-md hover:shadow-xl mb-4">
      <div className="flex items-center justify-between text-our_dark hover:text-our_magenta">
        <h5 className="mb-2 text-base font-bold tracking-tight">
          {title.replaceAll("\"", "")}
        </h5>
        <div className="w-40 ml-4 text-our_dark hover:text-our_dark">
          <div className="flex justify-end mb-1">
            <span className="text-sm font-medium">{similarityPercentage}% match</span>
          </div>
          <div className="w-full bg-our_magenta rounded-full h-2.5">
            <div className="bg-our_dark h-2.5 rounded-full" style={{width: `${similarityPercentage}%`}}></div>
          </div>
        </div>

      </div>

    </Link>
  );
}
