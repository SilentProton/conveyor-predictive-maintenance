import { useState } from 'react';
import { FileUpload } from './components/ui/FileUpload';

function App() {
  const [resultImage, setResultImage] = useState<string | null>(null);

  return (
    <>
      <div className="flex w-screen h-screen">
        {/* Left Panel */}
        <div className="flex-1 text-white flex items-center justify-center h-screen">
          <FileUpload onChange={setResultImage} />
        </div>

        {/* Right Panel */}
        <div className="flex-1 text-white flex flex-col items-center justify-center">
          <h1 className="text-2xl font-bold mb-4">Output Panel</h1>
          {resultImage ? (
            <img
              src={resultImage}
              alt="YOLO Output"
              className="rounded-lg max-w-[90%] max-h-[80%] shadow-lg"
            />
          ) : (
            <p className="text-gray-400">No output yet</p>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
