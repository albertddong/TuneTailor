import React, { useState } from "react";
import Title from "./Title";
import Instructions from "./Instructions";
import GenerateButton from "./GenerateButton";

const SecondPage = () => {
  const [mood, setMood] = useState("");
  const [tempo, setTempo] = useState("");
  const [title, setTitle] = useState("TuneTailor AI");

  const handleMoodChange = (e) => setMood(e.target.value);
  const handleTempoChange = (e) => setTempo(e.target.value);
  const handleGeneratePlaylist = () => {
    console.log("Generate playlist with mood:", mood, "and tempo:", tempo);
    setTitle("Poop");
  };
  return (
    <div className="loadpage">
      <div class="line-border w-full">
        <div class="v1"></div>
        <div class="v2"></div>
        <div class="v3"></div>
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
      <GenerateButton handleGeneratePlaylist={handleGeneratePlaylist} />
    </div>
  );
};

export default SecondPage;
