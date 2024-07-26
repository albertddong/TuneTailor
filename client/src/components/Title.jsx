import React, { usestate } from "react";

const Title = ({ title }) => {
  return (
    <div>
      <h1 className="title">{title}</h1>
      <p className="title-description">
        An AI-driven playlist generator with Spotify.
      </p>
    </div>
  );
};

export default Title;
