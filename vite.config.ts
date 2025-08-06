import { resolve } from 'path'
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react-swc'
// import 'vite/modulepreload-polyfill';

// https://vite.dev/config/
export default defineConfig({
  // Don't set root to frontend - keep it at project root for easier path management
  build: {
    manifest: "manifest.json",
    outDir: resolve("./static/www/assets"),
    assetsDir: "",
    rollupOptions: {
      input: {
        main: resolve('./frontend/js/main.ts'),
        // Add more entry points as needed
        // app: resolve('./frontend/js/app.tsx'),
        // other: resolve('./frontend/js/other.tsx'),
      },
    },
  },
  resolve: {
    alias: {
      '@': resolve('./frontend/js'),
      '@/components': resolve('./frontend/js/components'),
    },
  },
  plugins: [
    tailwindcss(),
    react()
  ],
  server: {
    // Configure dev server to work alongside Django
    port: 5173,
    host: true,
  },
})
