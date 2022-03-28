import { useEffect, useState } from "react";
import axios from "axios";
import {format} from "date-fns";
import './App.css';

const baseUrl = "http://localhost:5000"

function App() {

  const [plate, setPlate] = useState("")
  const [owner, setOwner] = useState("")
  const [startDate, setStartDate] = useState("")
  const [endDate, setEndDate] = useState("")

  const handleChange = e => {
    setPlate(e.target.value);
  }

  const handleSubmit =  e => {
    e.preventDefault();
    console.log(plate)
  }

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label htmlFor="plate">Plate:</label>
          <input
            onChange={handleChange}
            type="text"
            name="plate"
            id="plate"
            value={plate}
          /><br/>
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
}

export default App;
