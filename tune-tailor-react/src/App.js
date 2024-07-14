import React, { useState } from "react";
import "./App.css";
import Title from "./components/Title";
import Instructions from "./components/Instructions";
import GenerateButton from "./components/GenerateButton";

function App() {
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
    <div className="App min-h-screen min-w-screen relative">
      {/* Right Green Ellipse Blur */}
      {/* <svg
        width="993"
        height="988"
        viewBox="0 0 993 988"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g filter="url(#filter0_f_16_19)">
          <ellipse
            cx="496.448"
            cy="493.683"
            rx="252"
            ry="236.981"
            transform="rotate(-40.233 496.448 493.683)"
            fill="#2D9871"
            fill-opacity="0.5"
          />
        </g>
        <defs>
          <filter
            id="filter0_f_16_19"
            x="0.592957"
            y="0.321716"
            width="991.711"
            height="986.723"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="125"
              result="effect1_foregroundBlur_16_19"
            />
          </filter>
        </defs>
      </svg>
      <svg
        width="942"
        height="898"
        viewBox="0 0 942 898"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g filter="url(#filter0_f_16_15)">
          <ellipse
            cx="361.973"
            cy="512.91"
            rx="111.973"
            ry="135.097"
            fill="#25E1E1"
            fill-opacity="0.5"
          />
        </g>
        <g filter="url(#filter1_f_16_15)">
          <ellipse
            cx="526.987"
            cy="449.004"
            rx="165.013"
            ry="199.004"
            fill="#60BA28"
            fill-opacity="0.5"
          />
        </g>
        <g filter="url(#filter2_f_16_15)">
          <ellipse
            cx="443.498"
            cy="563.903"
            rx="64.4993"
            ry="135.097"
            fill="#DBFDCF"
            fill-opacity="0.5"
          />
        </g>
        <defs>
          <filter
            id="filter0_f_16_15"
            x="0"
            y="127.813"
            width="723.947"
            height="770.195"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="125"
              result="effect1_foregroundBlur_16_15"
            />
          </filter>
          <filter
            id="filter1_f_16_15"
            x="111.973"
            y="0"
            width="830.027"
            height="898.007"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="125"
              result="effect1_foregroundBlur_16_15"
            />
          </filter>
          <filter
            id="filter2_f_16_15"
            x="278.999"
            y="328.805"
            width="328.999"
            height="470.195"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="50"
              result="effect1_foregroundBlur_16_15"
            />
          </filter>
        </defs>
      </svg>
      <svg
        width="1265"
        height="1258"
        viewBox="0 0 1265 1258"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g filter="url(#filter0_f_16_20)">
          <ellipse
            cx="122.362"
            cy="137.589"
            rx="122.362"
            ry="137.589"
            transform="matrix(-0.160875 -0.986975 0.947719 -0.319106 522.17 794.093)"
            fill="#7AEBFB"
            fill-opacity="0.5"
          />
        </g>
        <g filter="url(#filter1_f_16_20)">
          <ellipse
            cx="67.089"
            cy="83.4994"
            rx="67.089"
            ry="83.4994"
            transform="matrix(0.156629 -0.987657 0.997855 -0.0654711 551.813 644.311)"
            fill="#D225E1"
            fill-opacity="0.5"
          />
        </g>
        <g filter="url(#filter2_f_16_20)">
          <ellipse
            cx="98.868"
            cy="122.998"
            rx="98.868"
            ry="122.998"
            transform="matrix(0.156629 -0.987657 0.997855 -0.0654711 483.494 583.222)"
            fill="#25E1CB"
            fill-opacity="0.5"
          />
        </g>
        <g filter="url(#filter3_f_16_20)">
          <ellipse
            cx="38.6448"
            cy="83.4994"
            rx="38.6448"
            ry="83.4994"
            transform="matrix(0.156629 -0.987657 0.997855 -0.0654711 595.368 565.912)"
            fill="#CFECFD"
            fill-opacity="0.5"
          />
        </g>
        <defs>
          <filter
            id="filter0_f_16_20"
            x="0.989258"
            y="0.881683"
            width="1263.78"
            height="1257.07"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="250"
              result="effect1_foregroundBlur_16_20"
            />
          </filter>
          <filter
            id="filter1_f_16_20"
            x="311.652"
            y="256.094"
            width="667.978"
            height="632.979"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="125"
              result="effect1_foregroundBlur_16_20"
            />
          </filter>
          <filter
            id="filter2_f_16_20"
            x="247.993"
            y="129.537"
            width="747.44"
            height="695.969"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="125"
              result="effect1_foregroundBlur_16_20"
            />
          </filter>
          <filter
            id="filter3_f_16_20"
            x="501.198"
            y="383.715"
            width="367.087"
            height="277.125"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="BackgroundImageFix"
              result="shape"
            />
            <feGaussianBlur
              stdDeviation="50"
              result="effect1_foregroundBlur_16_20"
            />
          </filter>
        </defs>
      </svg> */}

      <div class="line-border">
        <div class="v1"></div>
        <div class="v2"></div>
        <div class="v3"></div>
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
            stroke-width="5"
            stroke-linecap="round"
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
      <GenerateButton handleGeneratePlaylist={handleGeneratePlaylist} />
    </div>
  );
}

export default App;
