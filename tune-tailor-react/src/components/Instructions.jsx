import React from "react";

function Instructions({ mood, tempo, handleMoodChange, handleTempoChange }) {
  return (
    <div className="instructions flex flex-col w-1/2">
      <p className="">To create a playlist recommendation, you can either:</p>
      <ol className="flex flex-col w-3/4">
        <li>
          Manually select a 'mood' and 'tempo'
          <div className="dropdowns flex flex-row gap-28">
            <select
              value={mood}
              onChange={handleMoodChange}
              className="mood-dropdown"
            >
              <option value="">Select Mood</option>
              <option value="happy">Happy</option>
              <option value="sad">Sad</option>
              <option value="energetic">Energetic</option>
            </select>
            <select
              value={tempo}
              onChange={handleTempoChange}
              className="tempo-dropdown"
            >
              <option value="">Select Tempo</option>
              <option value="slow">Slow</option>
              <option value="medium">Medium</option>
              <option value="fast">Fast</option>
            </select>
          </div>
        </li>
        <div className="or-divider flex justify-center">OR</div>
        <li>
          Decide together with our TuneTailor AI!
          <textarea
            placeholder="Ex. I'd like to listen to some slow jazz."
            className="textarea"
            rows="4"
          ></textarea>
        </li>
      </ol>
    </div>
  );
}

export default Instructions;
