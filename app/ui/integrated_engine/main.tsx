import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

console.log("VectorFL Sandbox: Starting Boot Sequence...");

window.onerror = (msg, url, line, col, error) => {
  console.error("CRITICAL RUNTIME ERROR:", msg, "at", line, ":", col);
  document.body.innerHTML = `<div style="padding: 20px; color: red; font-family: sans-serif;"><h1>Critical Error</h1><pre>${msg}</pre><p>Check Console for details.</p></div>`;
  return false;
};

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
