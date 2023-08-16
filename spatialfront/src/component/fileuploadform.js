import React, { useState } from 'react';
import axios from 'axios';
import ResponseTable from './responsetable';

const FileUploadForm = () => {
  const [file, setFile] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const [numericData, setNumericData] = useState([]);
  const [categoricData, setCategoricData] = useState([]);
  const [selectedNumericColumns, setSelectedNumericColumns] = useState([]);
  const [selectedCategoricColumns, setSelectedCategoricColumns] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('data', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/clean/reading', formData);
      setResponseData(response.data.data); // Store the response data array
      setNumericData(response.data.numerical); // Store the response data array
      setCategoricData(response.data.categorical_data); // Store the response data array
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {responseData && <ResponseTable data={responseData} />}

      <div>
        <h3>Select Numeric Columns:</h3>
        <select
          multiple
          value={selectedNumericColumns}
          onChange={(e) => setSelectedNumericColumns(Array.from(e.target.selectedOptions, (option) => option.value))}
        >
          {numericData.map((column) => (
            <option key={column} value={column}>
              {column}
            </option>
          ))}
        </select>
      </div>

      <div>
        <h3>Select Categoric Columns:</h3>
        <select
          multiple
          value={selectedCategoricColumns}
          onChange={(e) => setSelectedCategoricColumns(Array.from(e.target.selectedOptions, (option) => option.value))}
        >
          {categoricData.map((column) => (
            <option key={column} value={column}>
              {column}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default FileUploadForm;
