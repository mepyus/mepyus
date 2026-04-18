import React from "react";
import { createRoot } from "react-dom/client";
import VectorFLSurfacesMock from "../../vectorfl_dual_surface";
import "./styles.css";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <VectorFLSurfacesMock />
  </React.StrictMode>,
);
