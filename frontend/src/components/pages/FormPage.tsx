import { useState } from "react";
import { Link } from "react-router-dom";

interface FormData {
  mrn: string;
  gender: string;
  albumin: string;
  alkalinePhosphatase: string;
  alanineTransaminase: string;
  aspartateTransaminase: string;
  bilirubin: string;
  cholinesterase: string;
  cholesterol: string;
  creatinine: string;
  gammaGlutamylTransferase: string;
  protein: string;
}

function FormPage() {
  const [formData, setFormData] = useState<FormData>({
    mrn: "",
    gender: "",
    albumin: "",
    alkalinePhosphatase: "",
    alanineTransaminase: "",
    aspartateTransaminase: "",
    bilirubin: "",
    cholinesterase: "",
    cholesterol: "",
    creatinine: "",
    gammaGlutamylTransferase: "",
    protein: "",
  });

  const [predictionResult, setPredictionResult] = useState("");

  const handleInputChange = (field: keyof FormData, value: string) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implement prediction logic here
    setPredictionResult(
      "Prediction result will appear here after form submission."
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      {/* Header */}
      <div className="max-w-6xl mx-auto mb-8">
        <div className="flex justify-between items-center">
          <h1 className="text-4xl font-bold text-center text-gray-800 flex-1">
            Hepatitis C Virus Prediction
          </h1>
          <Link
            to="/"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg shadow-md transition-colors duration-200"
          >
            Model Info
          </Link>
        </div>
      </div>

      {/* Main Form */}
      <div className="max-w-6xl mx-auto">
        <form
          onSubmit={handleSubmit}
          className="bg-white rounded-2xl shadow-xl p-8 mb-8"
        >
          {/* Patient Information */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div>
              <label
                htmlFor="mrn"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                MRN
              </label>
              <input
                type="number"
                id="mrn"
                value={formData.mrn}
                onChange={(e) => handleInputChange("mrn", e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Enter MRN"
                required
              />
            </div>
            <div>
              <label
                htmlFor="gender"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Gender
              </label>
              <select
                id="gender"
                value={formData.gender}
                onChange={(e) => handleInputChange("gender", e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                required
              >
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
          </div>

          {/* Lab Tests Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Albumin */}
            <div>
              <label
                htmlFor="albumin"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Albumin (ALB) - g/L
              </label>
              <input
                type="number"
                id="albumin"
                value={formData.albumin}
                onChange={(e) => handleInputChange("albumin", e.target.value)}
                min="35"
                max="50"
                step="0.1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 35-50 g/L"
                required
              />
            </div>

            {/* Alkaline Phosphatase */}
            <div>
              <label
                htmlFor="alkalinePhosphatase"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Alkaline Phosphatase (ALP) - IU/L
              </label>
              <input
                type="number"
                id="alkalinePhosphatase"
                value={formData.alkalinePhosphatase}
                onChange={(e) =>
                  handleInputChange("alkalinePhosphatase", e.target.value)
                }
                min="44"
                max="147"
                step="1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 44-147 IU/L"
                required
              />
            </div>

            {/* Alanine Transaminase */}
            <div>
              <label
                htmlFor="alanineTransaminase"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Alanine Transaminase (ALT) - U/L
              </label>
              <input
                type="number"
                id="alanineTransaminase"
                value={formData.alanineTransaminase}
                onChange={(e) =>
                  handleInputChange("alanineTransaminase", e.target.value)
                }
                min="7"
                max="56"
                step="1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 7-56 U/L"
                required
              />
            </div>

            {/* Aspartate Transaminase */}
            <div>
              <label
                htmlFor="aspartateTransaminase"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Aspartate Transaminase (AST) - U/L
              </label>
              <input
                type="number"
                id="aspartateTransaminase"
                value={formData.aspartateTransaminase}
                onChange={(e) =>
                  handleInputChange("aspartateTransaminase", e.target.value)
                }
                min="10"
                max="40"
                step="1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 10-40 U/L"
                required
              />
            </div>

            {/* Bilirubin */}
            <div>
              <label
                htmlFor="bilirubin"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Bilirubin (BIL) - µmol/L
              </label>
              <input
                type="number"
                id="bilirubin"
                value={formData.bilirubin}
                onChange={(e) => handleInputChange("bilirubin", e.target.value)}
                min="5"
                max="21"
                step="0.1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 5-21 µmol/L"
                required
              />
            </div>

            {/* Cholinesterase */}
            <div>
              <label
                htmlFor="cholinesterase"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Cholinesterase (CHE) - kU/L
              </label>
              <input
                type="number"
                id="cholinesterase"
                value={formData.cholinesterase}
                onChange={(e) =>
                  handleInputChange("cholinesterase", e.target.value)
                }
                min="5.3"
                max="12.9"
                step="0.1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 5.3-12.9 kU/L"
                required
              />
            </div>

            {/* Cholesterol */}
            <div>
              <label
                htmlFor="cholesterol"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Cholesterol (CHOL) - mmol/L
              </label>
              <input
                type="number"
                id="cholesterol"
                value={formData.cholesterol}
                onChange={(e) =>
                  handleInputChange("cholesterol", e.target.value)
                }
                min="3.0"
                max="5.5"
                step="0.1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 3.0-5.5 mmol/L"
                required
              />
            </div>

            {/* Creatinine */}
            <div>
              <label
                htmlFor="creatinine"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Creatinine (CREA) - µmol/L
              </label>
              <input
                type="number"
                id="creatinine"
                value={formData.creatinine}
                onChange={(e) =>
                  handleInputChange("creatinine", e.target.value)
                }
                min="60"
                max="110"
                step="1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 60-110 µmol/L"
                required
              />
            </div>

            {/* Gamma-Glutamyl Transferase */}
            <div>
              <label
                htmlFor="gammaGlutamylTransferase"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Gamma-Glutamyl Transferase (GGT) - U/L
              </label>
              <input
                type="number"
                id="gammaGlutamylTransferase"
                value={formData.gammaGlutamylTransferase}
                onChange={(e) =>
                  handleInputChange("gammaGlutamylTransferase", e.target.value)
                }
                min="9"
                max="48"
                step="1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 9-48 U/L"
                required
              />
            </div>

            {/* Protein */}
            <div>
              <label
                htmlFor="protein"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Protein (PROT) - g/L
              </label>
              <input
                type="number"
                id="protein"
                value={formData.protein}
                onChange={(e) => handleInputChange("protein", e.target.value)}
                min="60"
                max="80"
                step="0.1"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                placeholder="Range: 60-80 g/L"
                required
              />
            </div>
          </div>

          {/* Submit Button */}
          <div className="mt-8 text-center">
            <button
              type="submit"
              className="bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-8 rounded-lg shadow-lg transition-all duration-200 transform hover:scale-105"
            >
              Predict Hepatitis C Risk
            </button>
          </div>
        </form>

        {/* Prediction Result Area */}
        <div className="bg-white rounded-2xl shadow-xl p-8">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            Prediction Result
          </h2>
          <div className="min-h-[120px] p-4 border-2 border-dashed border-gray-300 rounded-lg bg-gray-50">
            <p className="text-gray-600 text-center">
              {predictionResult ||
                "Prediction results will appear here after form submission."}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FormPage;
