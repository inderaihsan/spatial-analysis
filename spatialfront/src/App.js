import React, { useState } from 'react';
import './App.css';
import FileUploadForm from './component/fileuploadform';

function App() {
  const [responseData, setResponseData] = useState(null);
  return (
    <div className="App">
      <h1>File Upload and Data Table</h1>
      <FileUploadForm />
    </div>
  );
}

export default App;