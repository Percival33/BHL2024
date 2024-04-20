import {Header} from "./components/Header";
import {Gallery} from "./components/Galery";
import {Footer} from "./components/Footer";

function App() {
  const cards = [
    {title: "Hello", description: "World", key: "1"},
    {title: "Hello", description: "World", key: "2"},
    {title: "Hello", description: "World", key: "3"},
    {title: "Hello", description: "World", key: "4"},
    {title: "Hello", description: "World", key: "5"},
    {title: "Hello", description: "World", key: "26"},
    {title: "Hello", description: "World", key: "2336"},
    {title: "Hello", description: "World", key: "26d3"},
    {title: "Hello", description: "World", key: "26d32"},
    {title: "Hello", description: "World", key: "26d323"},
  ]
  return (
    <div className="App">
      <Header/>
      <Gallery cards={cards}/>
      <Footer/>
    </div>
  );
}

export default App;
