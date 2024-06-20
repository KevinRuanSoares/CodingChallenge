import React from 'react';
import './App.css';
import WordCounter from './components/WordCounter';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Word Counter Web App</h1>
      </header>
      <main>
        <WordCounter />
      </main>
    </div>
  );
};

export default App;
