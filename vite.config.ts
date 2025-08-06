import { resolve } from 'path'
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react-swc'
// import 'vite/modulepreload-polyfill';

// https://vite.dev/config/
export default defineConfig({
  base: "/static/",
  build: {
    manifest: "manifest.json",
    outDir: resolve("./static/www/assets"),
    assetsDir: "",
    modulePreload: {
      polyfill: true
    },
    rollupOptions: {
      input: {
        // Global base script - loaded on every page
        'globals/base': resolve('./frontend/js/globals/base.ts'),
        
        // CSS entry points - separate from JS
        'css/base': resolve('./frontend/css/base.css'),
        'css/auth': resolve('./frontend/css/pages/auth.css'),
        'css/tasks': resolve('./frontend/css/pages/tasks.css'),
        
        // React apps for specific pages
        'apps/tasks': resolve('./frontend/js/apps/tasks.tsx'),
        
        // Helper scripts for specific functionality
        'helpers/projects': resolve('./frontend/js/helpers/projects.ts'),
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
