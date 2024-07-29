import React from "react";
import { useLocation } from "react-router-dom";
import Title from "./Title";
import Instructions from "./Instructions";

const SecondPage = () => {
  const location = useLocation();
  const { playlist } = location.state || { playlist: "" };

  return (
    <div className="flex flex-row">
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
      </div>
      <div className="flex right-side">
          {playlist && (
            <iframe
              src={playlist}
              width="1000"
              height="1000"
              frameBorder="0"
              allow="encrypted-media"
            ></iframe>
          )}
        </div>
    </div>
  );
};

export default SecondPage;
