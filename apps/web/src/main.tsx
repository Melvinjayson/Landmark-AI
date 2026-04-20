import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return (
    <main style={{ fontFamily: "Inter, sans-serif", padding: "2rem" }}>
      <h1>Landmark AI Operations Console</h1>
      <p>Frontend foundation initialized. Connect gateway APIs for live data.</p>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
