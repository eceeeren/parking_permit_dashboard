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
};

function App() {
  const [inputs, setInputs] = useState(plateInfo);
  const [platesList, setPlatesList] = useState([]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${baseUrl}/plate`, inputs);
    } catch (err) {
      console.error(err.message);
    }
  };

  const getPlates = async () => {
    try {
      const data = await axios.get(`${baseUrl}/plate`);
      const { plates } = data.data;
      setPlatesList(plates);
    } catch (err) {
      console.error(err.message);
    }
  };

  useEffect(() => {
    getPlates();
  }, []);

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
            type="date"
            name="start_date"
            id="start_date"
          />
          <br />
          <label htmlFor="plate">End Date:</label>
          <input
            onChange={handleChange}
            value={inputs.end_date}
            type="date"
            name="end_date"
            id="end_date"
          />
          <br />
          <button type="submit">Submit</button>
          <br />
          <h4>Plates List</h4>
          <ul>
            {platesList.map((plate) => {
              return (
                <li key={plate.plate}>
                  <div style={{textAlign: 'left'}}>
                    Plate Number: {plate.plate}
                    <br />
                    Owner: {plate.owner}
                    <br />
                    Start Date: {plate.start_date}
                    <br />
                    End Date: {plate.end_date}
                    <br />
                  </div>
                </li>
              );
            })}
          </ul>
        </form>
      </header>
    </div>
  );
}

export default App;
