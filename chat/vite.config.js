import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/graphql/": {
        target: "https://middleware.demo.inf326.nursoft.dev",
        changeOrigin: true,
        ws: true,
      },
    },
    watch: {
      usePolling: true
    },
    host: true,
  },
});
