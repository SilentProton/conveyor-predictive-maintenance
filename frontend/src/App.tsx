import { FileUpload } from './components/ui/FileUpload';

function App() {
  return (
    <>
      <div className="flex w-screen h-screen ">
        {/* Left Panel */}
        <div className="flex-1 text-white flex items-center justify-center h-screen">
          <FileUpload />
        </div>

        {/* Right Panel */}
        <div className="flex-1 text-white flex items-center justify-center">
          <h1 className="text-2xl font-bold">Output Panel</h1>
        </div>
      </div>
    </>
  );
}

export default App;
