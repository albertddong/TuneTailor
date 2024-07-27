import React from "react";
import { useLocation } from "react-router-dom";
import Title from "./Title";
import Instructions from "./Instructions";
import GenerateButton from "./GenerateButton";

const SecondPage = () => {
  const location = useLocation();
  const { playlist } = location.state || { playlist: [] };

  return (
    <div className="loadpage">
      <div className="line-border w-full">
        <div className="v1"></div>
        <div className="v2"></div>
        <div className="v3"></div>
      </div>
      <div className="left-side">
        <Title title="Generated Playlist" />
        <Instructions
          mood={""}
          tempo={""}
          handleMoodChange={() => {}}
          handleTempoChange={() => {}}
        />
      </div>
      <div className="right-side">
        <iframe
          src={`https://open.spotify.com/embed/playlist/${playlist}`}
          width="300"
          height="380"
          frameBorder="0"
          allow="encrypted-media"
        ></iframe>
      </div>
    </div>
  );
};

export default SecondPage;
