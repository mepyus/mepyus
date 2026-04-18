import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "node:path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: [
      { find: "@", replacement: path.resolve(__dirname, "src") },
      { find: "framer-motion", replacement: path.resolve(__dirname, "src/lib/framer-motion-shim.tsx") },
      { find: "lucide-react", replacement: path.resolve(__dirname, "node_modules/lucide-react/dist/esm/lucide-react.js") },
      { find: /^react$/, replacement: path.resolve(__dirname, "node_modules/react/index.js") },
      { find: /^react-dom\/client$/, replacement: path.resolve(__dirname, "node_modules/react-dom/client.js") },
      { find: /^react-dom$/, replacement: path.resolve(__dirname, "node_modules/react-dom/index.js") },
    ],
  },
  server: {
    fs: {
      allow: [path.resolve(__dirname), path.resolve(__dirname, "..")],
    },
  },
});
