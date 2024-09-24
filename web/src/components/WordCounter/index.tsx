import React, { useState } from 'react';
import { isAxiosError } from 'axios';

import axiosInstance from '../../api';
import './style.css';
import packageJson from '../../../package.json';

interface TextDTO {
    text: string;
}

interface WordCountDTO {
    word_count: number;
}

const WordCounter: React.FC = () => {
    const [text, setText] = useState<string>('');
    const [wordCount, setWordCount] = useState<number | null>(null);
    const [error, setError] = useState<string | null>(null);

    const countWords = async () => {
        setError(null);
        setWordCount(null);
        try {
            const response = await axiosInstance.post<WordCountDTO>(
                '/api/count_words',
                { text } as TextDTO,
            );
            setWordCount(response.data.word_count);
        } catch (err) {
            if (isAxiosError(err) && err.response) {
                setError(err.response.data.detail);
            } else {
                setError('An unexpected error occurred');
            }
        }
    };

    return (
        <div className="word-counter-container">
            <h1>Word Counter v{packageJson.version}</h1>
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Enter your text here"
                rows={10}
            />
            <button onClick={countWords}>Count Words</button>
            {wordCount !== null && <p>Word Count: {wordCount}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default WordCounter;
