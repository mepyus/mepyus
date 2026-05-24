import React from "react";
import EngineStateDashboard from "./EngineStateDashboard.tsx";
import PromptIntakeCardBuilder from "./PromptIntakeCardBuilder.tsx";
import VectorFLIntegrationShell from "./VectorFLIntegrationShell.tsx";

function App() {
  if (window.location.pathname === "/engine-state-dashboard") {
    return <EngineStateDashboard />;
  }
  if (window.location.pathname === "/prompt-intake-card-builder-preview") {
    return (
      <main className="min-h-screen bg-black p-6 text-slate-100">
        <PromptIntakeCardBuilder />
      </main>
    );
  }
  return <VectorFLIntegrationShell />;
}

export default App;
