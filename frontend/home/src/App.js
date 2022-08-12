import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  
  const [apiData, parsedData] = useState(0);
  const [timeData, setCurrentTime] = useState(0)

 // Get data from Flask
  useEffect(() => {
    fetch('/data').then(res => res.json()).then(data => {
      parsedData(data.userData[0].bio);
      console.log(data.userData)
    });
  }, []);

  // Get data from FastAPI
  useEffect(()=> {
    fetch('/vf/home').then(res => res.json()).then(time => {
      setCurrentTime(time.time);
    })
  })
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>Bio of User from FastAPI backend: {apiData}.</p>
        <p>Current time from Flask server is: {timeData}</p>
      </header>
    </div>
  );
}

export default App;
