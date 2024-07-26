import React, { useState } from "react";

function Instructions({ mood, tempo, handleMoodChange, handleTempoChange }) {
  const [isDropdownSelected, setIsDropdownSelected] = useState(false);
  const [isTextareaFilled, setIsTextareaFilled] = useState(false);

  const handleMoodChangeWrapper = (event) => {
    handleMoodChange(event);
    setIsDropdownSelected(event.target.value !== "");
    setIsTextareaFilled(false);
  };

  const handleTempoChangeWrapper = (event) => {
    handleTempoChange(event);
    setIsDropdownSelected(event.target.value !== "");
    setIsTextareaFilled(false);
  };

  const handleTextareaChange = (event) => {
    setIsTextareaFilled(event.target.value.trim() !== "");
    if (event.target.value.trim() !== "") {
      setIsDropdownSelected(false);
    }
  };

  return (
    <div className="instructions flex flex-col w-1/2">
      <p>To create a playlist recommendation, you can either:</p>
      <ol className="flex flex-col w-3/4">
        <li>
          Manually select a 'mood' and 'tempo'
          <div className="dropdowns flex flex-row gap-28">
            <select
              value={mood}
              onChange={handleMoodChangeWrapper}
              className="mood-dropdown"
              disabled={isTextareaFilled}
            >
              <option value="">Select Mood</option>
              <option value="happy">Happy</option>
              <option value="sad">Sad</option>
              <option value="energetic">Energetic</option>
            </select>
            <select
              value={tempo}
              onChange={handleTempoChangeWrapper}
              className="tempo-dropdown"
              disabled={isTextareaFilled}
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
            onChange={handleTextareaChange}
            disabled={isDropdownSelected}
            style={{ backgroundColor: isDropdownSelected ? "#9c9c9c" : "#fff" }}
          ></textarea>
        </li>
      </ol>
    </div>
  );
}

export default Instructions;
