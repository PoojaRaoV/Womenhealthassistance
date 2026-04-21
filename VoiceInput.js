import React, { useState, useEffect } from "react";
import axios from "axios";
import "./VoiceInput.css";

function VoiceInput() {
  const [language, setLanguage] = useState("en-US");
  const [started, setStarted] = useState(false);

  const [data, setData] = useState({
    name: "",
    age: "",
    weight: "",
    symptoms: "",
  });

  // 🎤 AI INTRO (runs when language changes)
  useEffect(() => {
    const speech = new SpeechSynthesisUtterance(
      "Hey! I am AI Jarvis, your health assistant. Please select your language."
    );
    speech.lang = language;
    window.speechSynthesis.speak(speech);
  }, [language]);

  // 🎤 Start Voice Recognition
  const startVoice = () => {
    setStarted(true);

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = language;
    recognition.start();

    recognition.onresult = function (event) {
      const text = event.results[0][0].transcript.toLowerCase();
      console.log("User said:", text);

      if (text.includes("name")) {
        setData(prev => ({ ...prev, name: text }));
      } else if (text.includes("age")) {
        setData(prev => ({ ...prev, age: text }));
      } else if (text.includes("weight")) {
        setData(prev => ({ ...prev, weight: text }));
      } else {
        setData(prev => ({ ...prev, symptoms: text }));
      }
    };
  };

  // 📤 Send Data to Backend
  const submitData = async () => {
    try {
      await axios.post("http://localhost:5000/addData", data);
      alert("Data saved successfully");
    } catch (error) {
      console.log(error);
      alert("Error saving data");
    }
  };

  return (
    <div className="voice-container">
      <div className="card">
        <h2>🤖 AI Jarvis</h2>

        {!started && (
          <>
            <p className="intro">
              Hey! I am AI Jarvis, your health assistant 👋 <br />
              Please select your language
            </p>

            {/* 🌍 Language Selection */}
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="input"
            >
              <option value="en-US">English</option>
              <option value="kn-IN">Kannada</option>
              <option value="te-IN">Telugu</option>
              <option value="ta-IN">Tamil</option>
              <option value="hi-IN">Hindi</option>
            </select>

            <button onClick={startVoice} className="mic-btn">
              🎤 Start Assistant
            </button>
          </>
        )}

        {started && (
          <>
            <h3>🎧 Listening...</h3>

            <button onClick={submitData} className="submit-btn">
              Submit Data
            </button>

            <pre>{JSON.stringify(data, null, 2)}</pre>
          </>
        )}
      </div>
    </div>
  );
}

export default VoiceInput;