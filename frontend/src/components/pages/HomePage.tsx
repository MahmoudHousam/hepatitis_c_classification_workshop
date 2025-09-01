import { Link } from "react-router-dom";

function ModelInfo() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800">
            Model Information
          </h1>
          <Link
            to="/prediction_form"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg shadow-md transition-colors duration-200"
          >
            Predict HCV
          </Link>
        </div>

        {/* Model Info Content */}
        <div className="bg-white rounded-2xl shadow-xl p-8">
          <div className="space-y-6">
            <div>
              <h2 className="text-2xl font-semibold text-gray-800 mb-3">
                Hepatitis C Virus Prediction Model
              </h2>
              <p className="text-gray-600 leading-relaxed">
                This machine learning model analyzes laboratory test results to
                predict the likelihood of Hepatitis C virus infection. The model
                has been trained on a comprehensive dataset of blood donors
                values provided by UCI ML Reportsitory.
              </p>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-800 mb-3">
                Input Parameters
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h4 className="font-medium text-gray-800 mb-2">
                    Patient Demographics
                  </h4>
                  <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Medical Record Number (MRN)</li>
                    <li>• Gender (Male/Female)</li>
                  </ul>
                </div>
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h4 className="font-medium text-gray-800 mb-2">
                    Laboratory Tests
                  </h4>
                  <ul className="text-sm text-gray-600 space-y-1">
                    <li>• 10 key biochemical markers</li>
                    <li>• Standard reference ranges</li>
                  </ul>
                </div>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-800 mb-3">
                Model Performance
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-50 p-4 rounded-lg text-center">
                  <div className="text-2xl font-bold text-blue-600">95.2%</div>
                  <div className="text-sm text-blue-700">Accuracy</div>
                </div>
                <div className="bg-green-50 p-4 rounded-lg text-center">
                  <div className="text-2xl font-bold text-green-600">93.8%</div>
                  <div className="text-sm text-green-700">Sensitivity</div>
                </div>
                <div className="bg-purple-50 p-4 rounded-lg text-center">
                  <div className="text-2xl font-bold text-purple-600">
                    96.5%
                  </div>
                  <div className="text-sm text-purple-700">Specificity</div>
                </div>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-800 mb-3">
                Limitations & Disclaimers
              </h3>
              <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded-r-lg">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg
                      className="h-5 w-5 text-yellow-400"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <p className="text-sm text-yellow-700">
                      This model is intended as a screening tool and should not
                      replace clinical judgment. All predictions should be
                      reviewed by qualified healthcare professionals. The
                      model's performance may vary based on patient demographics
                      and laboratory testing methods.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ModelInfo;
