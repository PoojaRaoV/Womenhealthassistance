import React from "react";
import "./home.css";

function Home() {
  return (
    <div className="home">
      <header className="header">FemAI Care</header>

      <div className="container">
        <h2>Find Services Near You</h2>

        <button>Nearby Blood Labs</button>
        <button>Home Sample Collection</button>
      </div>

      <footer className="footer">
        ©️ 2026 FemAI Care | Designed for Easy Healthcare Access
      </footer>
    </div>
  );
}

export default Home;