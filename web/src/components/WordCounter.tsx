import React, { useState } from 'react';

const WordCounter: React.FC = () => {
  const [text, setText] = useState<string>('');
  const [wordCount, setWordCount] = useState<number>(0);

  const handleTextChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const inputText = e.target.value;
    setText(inputText);
    setWordCount(countWords(inputText));
  };

  const countWords = (text: string): number => {
    return text.trim().split(/\s+/).filter(word => word.length > 0).length;
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h2>Word Counter</h2>
      <textarea
        value={text}
        onChange={handleTextChange}
        rows={10}
        cols={50}
        style={{ width: '100%', padding: '10px' }}
        placeholder="Type or paste your text here..."
      />
      <div style={{ marginTop: '10px' }}>
        <strong>Word Count: </strong>{wordCount}
      </div>
    </div>
  );
};

export default WordCounter;
