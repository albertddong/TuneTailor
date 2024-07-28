import React, { useEffect } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useNavigate,
} from "react-router-dom";
import "./App.css";
import HomePage from "./components/HomePage";
import SecondPage from "./components/SecondPage";


const App = () => {
  const adjustV2Height = () => {
    const v2Element = document.querySelector(".line-border .v2");
    if (v2Element) {
      const topPosition = v2Element.offsetTop;
      const viewportHeight = window.innerHeight;
      v2Element.style.height = `${viewportHeight - topPosition}px`;
    }
  };

  useEffect(() => {
    adjustV2Height();
    window.addEventListener("resize", adjustV2Height);
    return () => window.removeEventListener("resize", adjustV2Height);
  }, []);

  return (
    <Router>
      <div className="App min-h-screen min-w-screen relative">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route
            path="/second"
            element={
              <div className="loadpage">
                <SecondPage />
              </div>
            }
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
