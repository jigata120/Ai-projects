import React, { useEffect, useState } from 'react';

const WordLimitTextarea = ({ wordLimitProp, handleLocalChange ,settings}) => {
  const [content, setContent] = useState('');
  const [wordCount, setWordCount] = useState(0);

  const validateAndTrimContent = (content, wordLimit) => {
    const words = content.trim().split(/\s+/);
    if (words.length > wordLimit) {
      return words.slice(0, wordLimit).join(' ');
    }
    console.log(wordLimit);
    return content;
  };

  useEffect(()=>{
    const trimmedValue = validateAndTrimContent(settings.contextData,wordLimitProp)
    setContent(trimmedValue);
    setWordCount(trimmedValue.trim().split(/\s+/).length);
   },[settings])
  
   
  const handleChange = (event) => {
    const newValue = event.target.value;
    const trimmedValue = validateAndTrimContent(newValue, wordLimitProp);

    setContent(trimmedValue);
    setWordCount(trimmedValue.trim().split(/\s+/).length);
    
    handleLocalChange('contextData', trimmedValue);
  };

  const remainingWords = wordLimitProp - wordCount;

  return (
    <div>
      <textarea
        value={content}
        placeholder="Enter context data here..."
        onChange={handleChange}
        className="w-full border rounded px-2 py-1"
      />
      <div className="mt-2 text-sm text-gray-600">
        {remainingWords} words remaining
      </div>
    </div>
  );
};

export default WordLimitTextarea;
