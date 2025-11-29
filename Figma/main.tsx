import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './styles/globals.css'

// Asegurar que la página siempre inicie en la parte superior
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}

// Scroll al inicio al cargar
window.scrollTo(0, 0);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
