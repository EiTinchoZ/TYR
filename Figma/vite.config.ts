import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './'),
    },
  },
  server: {
    port: 5173,
    host: true,
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    rollupOptions: {
      output: {
        manualChunks: {
          // Separar React y ReactDOM en su propio chunk
          'react-vendor': ['react', 'react-dom'],
          // Separar motion/framer-motion
          'motion-vendor': ['motion'],
          // Separar lucide-react icons
          'icons-vendor': ['lucide-react'],
          // Separar markdown y PDF
          'markdown-vendor': ['react-markdown', 'remark-gfm', 'rehype-raw', 'jspdf'],
        },
      },
    },
    chunkSizeWarningLimit: 600,
  },
})
