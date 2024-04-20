import React, { useState } from 'react';

import {Header} from "./components/Header";
import {Gallery} from "./components/Galery";
import {Footer} from "./components/Footer";

function App() {
    const [searchTerm, setSearchTerm] = useState('');
  return (
    <div className="App">
        <Header onSearchChange={setSearchTerm} />
        <Gallery searchTerm={searchTerm} />
      <Footer/>
    </div>
  );
}

export default App;
