import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import AuthProvider from './contexts/UserProvider.tsx';
import DeleteProvider from './contexts/CharacterProvider.tsx';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <AuthProvider>
      <DeleteProvider>
        <App />
      </DeleteProvider>
    </AuthProvider>
  </React.StrictMode>
);
