import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import FormPage from "./components/pages/FormPage";
import ModelInfo from "./components/pages/HomePage";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        {/* Navigation Header */}
        <nav className="bg-white shadow-lg">
          <div className="max-w-6xl mx-auto px-4">
            <div className="flex justify-between items-center py-4">
              <Link
                to="/prediction_form"
                className="text-2xl font-bold text-gray-800 hover:text-blue-600 transition-colors"
              >
                Hepatitis C Prediction
              </Link>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main>
          <Routes>
            <Route path="/" element={<ModelInfo />} />
            <Route path="/prediction_form" element={<FormPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
