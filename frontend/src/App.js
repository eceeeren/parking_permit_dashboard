import { useEffect, useState } from "react";
import axios from "axios";
import { format } from "date-fns";
import "./App.css";

const baseUrl = "http://localhost:5000";

const plateInfo = {
  plate: "",
  owner: "",
  start_date: "",
  end_date: "",
}

function App() {
  const [inputs, setInputs] = useState(plateInfo);

  const handleChange = (event) => {
    const {name, value} = event.target;
    setInputs({...inputs, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputs)
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label htmlFor="plate">Plate:</label>
          <input
            onChange={handleChange}
            value={inputs.plate}
            type="text"
            name="plate"
            id="plate"
          />
          <br />
          <label htmlFor="plate">Owner:</label>
          <input
            onChange={handleChange}
            value={inputs.owner}
            type="text"
            name="owner"
            id="owner"
          />
          <br />
          <label htmlFor="plate">Start Date:</label>
          <input
            onChange={handleChange}
            value={inputs.start_date}
            type="text"
            name="start_date"
            id="start_date"
          />
          <br />
          <label htmlFor="plate">End Date:</label>
          <input
            onChange={handleChange}
            value={inputs.end_date}
            type="text"
            name="end_date"
            id="end_date"
          />
          <br />
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
}

export default App;
