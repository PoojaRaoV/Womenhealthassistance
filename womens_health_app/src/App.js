import { useState, useEffect } from "react";

export default function App() {
  const [language, setLanguage] = useState(null);
  const [search, setSearch] = useState("");

  // Load videos from localStorage
  const [videos, setVideos] = useState(() => {
    const saved = localStorage.getItem("videos");
    return saved
      ? JSON.parse(saved)
      : {
          english: [],
          hindi: [],
          kannada: [],
          telugu: []
        };
  });


  // Save to localStorage
  useEffect(() => {
    localStorage.setItem("videos", JSON.stringify(videos));
  }, [videos]);

  // Get YouTube ID
  const getVideoId = (url) => {
    const regExp = /(?:youtube\.com.*[?&]v=|youtu\.be\/)([^&#]+)/;
    const match = url.match(regExp);
    return match ? match[1] : null;
  };


  // Filter videos
  const filteredVideos = language
    ? videos[language].filter((v) =>
        v.title.toLowerCase().includes(search.toLowerCase())
      )
    : [];

  return (
    <div className="min-h-screen bg-gray-50 pb-16">

      {/* HEADER */}
      <div
        style={{
          background: "#e91e63",
          color: "white",
          textAlign: "center",
          padding: "20px"
        }}
      >
        <h1 style={{ margin: 0, fontSize: "24px", fontWeight: "bold" }}>
          FemAI Care
        </h1>
      </div>

      {/* SUBTITLE (NO BACKGROUND) */}
      <p
        style={{
          textAlign: "center",
          fontSize: "16px",
          marginTop: "10px",
          color: "#333",
          fontWeight: "500"
        }}
      >
        Health Exercises Hub
      </p>

      {/* LANGUAGE SELECTION */}
      {!language && (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
          <h2>Select Your Language</h2>

          {["english", "hindi", "kannada", "telugu"].map((lang) => (
            <button
              key={lang}
              onClick={() => setLanguage(lang)}
              style={{
                background: "#e91e63",
                color: "white",
                padding: "10px 18px",
                borderRadius: "25px",
                border: "none",
                margin: "5px",
                cursor: "pointer"
              }}
            >
              {lang.toUpperCase()}
            </button>
          ))}
        </div>
      )}

      {/* VIDEO SECTION */}
      {language && (
        <div style={{ maxWidth: "1100px", margin: "auto", padding: "20px" }}>

          {/* Back */}
          <button
            onClick={() => setLanguage(null)}
            style={{
              color: "#e91e63",
              marginBottom: "10px",
              border: "none",
              background: "none",
              cursor: "pointer"
            }}
          >
            ⬅ Back
          </button>

          <h2 style={{ textAlign: "center" }}>
            {language.toUpperCase()} Workouts
          </h2>

         

          {/* SEARCH */}
          <input
            placeholder="Search workouts..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              marginBottom: "20px"
            }}
          />

          {/* VIDEO GRID */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
              gap: "20px"
            }}
          >
            {filteredVideos.map((video, index) => (
              <div
                key={index}
                onClick={() =>
                  window.open(
                    `https://www.youtube.com/watch?v=${video.id}`,
                    "_blank"
                  )
                }
                style={{
                  background: "white",
                  borderRadius: "10px",
                  overflow: "hidden",
                  cursor: "pointer"
                }}
              >
                <img
                  src={`https://img.youtube.com/vi/${video.id}/hqdefault.jpg`}
                  style={{ width: "100%" }}
                />

                <p style={{ padding: "10px" }}>{video.title}</p>

              </div>
            ))}
          </div>
        </div>
      )}

      {/* FOOTER */}
      <footer
        style={{
          background: "#e91e63",
          color: "white",
          padding: "12px",
          fontSize: "14px",
          position: "fixed",
          bottom: 0,
          width: "100%",
          textAlign: "center"
        }}
      >
        © 2026 FemAI Care | Designed for Easy Healthcare Access
      </footer>

    </div>
  );
}