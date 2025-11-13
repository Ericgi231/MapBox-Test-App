import { useState } from 'react'
import './App.css'

function App() {
  const [result, setResult] = useState('Result will appear here...');
  const [name, setName] = useState('');

  const API_URL = 'http://localhost:8000';

  const testHello = async () => {
    try {
      const response = await fetch(`${API_URL}/api/hello`);
      const data = await response.json();
      setResult(`Success!\n${data.message}`);
    } catch (error) {
      setResult(`Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  };

  const testGreet = async () => {
    if (!name) {
      setResult('Please enter a name');
      return;
    }

    try {
      const response = await fetch(`${API_URL}/api/greet/${name}`);
      const data = await response.json();
      setResult(`Success!\n${data.message}`);
    } catch (error) {
      setResult(`Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  };

  return (
    <div className="container">
      <h1>FastAPI Web Application</h1>
      
      <div className="section">
        <h3>Test 1: Simple API Call</h3>
        <button onClick={testHello}>Get Hello Message</button>
      </div>

      <div className="section">
        <h3>Test 2: API with Parameter</h3>
        <input 
          type="text" 
          id="nameInput" 
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <button onClick={testGreet}>Get Greeting</button>
      </div>

      <div id="result">
        <strong>{result}</strong>
      </div>
    </div>
  )
}

export default App
