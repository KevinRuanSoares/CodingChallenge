import React from 'react';
import WordCounter from './components/WordCounter';
import './App.css';

const App: React.FC = () => {
    return (
        <div className="App">
            <header className="App-header">
                <WordCounter />
            </header>
        </div>
    );
};

export default App;
