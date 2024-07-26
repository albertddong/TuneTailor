import React from "react";

const GenerateButton = ({handleGeneratePlaylist}) => {
  return (
    <div className="generate">
      <button onClick={handleGeneratePlaylist}>
        <img src="spotify-icon.png" alt="Spotify" />
      </button>
    </div>
  );
};

export default GenerateButton;
