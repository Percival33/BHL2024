import "./App.css";
import { Navbar } from "./components/Navbar";
import { Card } from "./components/Card";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Card title={"ugabua"} date={"28.03.2020"} description={"duap"} />
    </div>
  );
}

export default App;
