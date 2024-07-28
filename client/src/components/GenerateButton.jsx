import React from "react";

const GenerateButton = ({ onClick }) => {
  return (
    <div className="generate">
      <button onClick={onClick}>
        <img src="spotify-icon.png" alt="Spotify" />
      </button>
    </div>
  );
};

export default GenerateButton;
