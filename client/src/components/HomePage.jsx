import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Title from "./Title";
import Instructions from "./Instructions";
import GenerateButton from "./GenerateButton";

const HomePage = () => {
  const [mood, setMood] = useState("");
  const [tempo, setTempo] = useState("");
  const [title, setTitle] = useState("TuneTailor AI");
  const navigate = useNavigate();

  const handleMoodChange = (e) => setMood(e.target.value);
  const handleTempoChange = (e) => setTempo(e.target.value);
  const handleGeneratePlaylist = () => {
    console.log("Generate playlist with mood:", mood, "and tempo:", tempo);
    navigate("/second");
  };

  return (
    <>
      <div className="line-border w-full">
        <div className="v1"></div>
        <div className="v2"></div>
        <div className="v3"></div>
        <svg
          width="67"
          height="63"
          viewBox="0 0 67 63"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="v4"
        >
          <path
            d="M63.666 3.41562C63.666 16.3328 62.7414 29.1212 52.5023 38.6018C40.5205 49.696 23.1356 49.7071 7.90587 49.7071C2.52482 49.7071 8.63739 46.2997 10.5361 43.9791C14.8155 38.7487 9.30387 44.259 7.08759 46.317C3.09959 50.0202 0.44488 50.3799 5.86016 54.4414C8.35556 56.313 10.4635 58.8764 13.1663 60.2278"
            stroke="#1ED760"
            strokeWidth="5"
            strokeLinecap="round"
          />
        </svg>
      </div>
      <div className="left-side">
        <Title title={title} />
        <Instructions
          mood={mood}
          tempo={tempo}
          handleMoodChange={handleMoodChange}
          handleTempoChange={handleTempoChange}
        />
      </div>
      <div className="number3 flex flex-row gap-4 font-semibold">
        <div>3. </div>
        <div className="w-5/6">
          When you're finished, click the Spotify icon in the middle of the
          screen to generate your playlist!
        </div>
      </div>
      <GenerateButton onClick={handleGeneratePlaylist} />
    </>
  );
};

export default HomePage;
