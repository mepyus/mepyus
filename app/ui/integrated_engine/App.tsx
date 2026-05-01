import React from "react";
import EngineStateDashboard from "./EngineStateDashboard.tsx";
import VectorFLIntegrationShell from "./VectorFLIntegrationShell.tsx";

function App() {
  if (window.location.pathname === "/engine-state-dashboard") {
    return <EngineStateDashboard />;
  }
  return <VectorFLIntegrationShell />;
}

export default App;
