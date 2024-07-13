import React, { useState } from 'react';
import './App.css';

function App() {
  const [mood, setMood] = useState('');
  const [tempo, setTempo] = useState('');
  const [title, setTitle] = useState('TuneTailor AI')

  const handleMoodChange = (e) => setMood(e.target.value);
  const handleTempoChange = (e) => setTempo(e.target.value);
  const handleGeneratePlaylist = () => {
    console.log('Generate playlist with mood:', mood, 'and tempo:', tempo);
    setTitle('Poop');
  };

  return (
    <div className="App">
      <div class="line-border">
        <div class="v1"></div>
        <div class="v2"></div>
        <div class="v3"></div>
        <div class="v4"></div>
      </div>
      <header className="App-header">
        <h1>{title}</h1>
        <p>An AI-driven playlist generator with Spotify.</p>
      </header>
      <div className="content">
        <div className="options">
          <h2>To create a playlist recommendation, you can either:</h2>
          <div className="manual-selection">
            <label>
              Manually select a 'mood':
              <select value={mood} onChange={handleMoodChange}>
                <option value="">Select Mood</option>
                <option value="happy">Happy</option>
                <option value="sad">Sad</option>
                <option value="energetic">Energetic</option>
              </select>
            </label>
            <label>
              and 'tempo':
              <select value={tempo} onChange={handleTempoChange}>
                <option value="">Select Tempo</option>
                <option value="slow">Slow</option>
                <option value="medium">Medium</option>
                <option value="fast">Fast</option>
              </select>
            </label>
          </div>
          <h2>OR</h2>
          <div className="ai-selection">
            <p>Decide together with our TuneTailor AI!</p>
          </div>
        </div>
        <div className="generate">
          <button onClick={handleGeneratePlaylist}>
            <img src="spotify-icon.png" alt="Spotify" />
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;