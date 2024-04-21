import React, {useState} from 'react';

import {Header} from "./components/Header";
import {Gallery} from "./components/Galery";
import {createBrowserRouter, Route, RouterProvider, Routes} from "react-router-dom";
import {NoteDetail} from "./pages/NoteDetail";
import {Footer} from "./components/Footer";
import {NoteSimilar} from "./components/NoteSimilar";

async function fetchNoteData(meeting_id) {
  const response = await fetch(`http://localhost:8080/note/${meeting_id}`);
  const note = await response.json();
  return Promise.resolve(note);
}

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Gallery searchTerm={searchTerm}/>,
    },
    {
      path: "/note/:noteId",
      element: <NoteDetail/>,
      loader: async ({params}) => {
        return fetchNoteData(params.noteId);
      }
    }
  ]);
  return (
    <div className={"App"}>
      <Header onSearchChange={setSearchTerm}/>
      <RouterProvider router={router}/>
      <Footer/>
    </div>
  );
}

export default App;
