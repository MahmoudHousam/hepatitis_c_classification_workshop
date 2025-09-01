# Hepatitis C Virus Classification Workshop

Most ML enthusiasts don't know how to go byond developing ML models to help the targeted audience use them in their workflow. The objectives of this workshop are:

- ML developers understand where the model lives
- How the API exposes it
- How the frontend consumes it
- Expose web developers to ML workflows.

## Dataset

[**HCV dataset**](https://archive.ics.uci.edu/dataset/571/hcv+data) contains laboratory values of blood donors and Hepatitis C patients and demographic values like age and gender

## Dataset Information

**Dataset Characteristics:** Multivariate

**Subject Area:** Health and Medicine

**Associated Tasks:** Classification, Clustering

**Feature Type:**: Integer, Real

**Instances:** 615

**Features:** 12

**What do the instances in this dataset represent?**

Instances are patients

**Additional Information**

The target attribute for classification is Category (blood donors vs. Hepatitis C, including its progress: 'just' Hepatitis C, Fibrosis, Cirrhosis).

**Has Missing Values?**

Yes

## Objective

Build a web app that allows lab technicians to input some lab tests to classify blood donors to either Blood Donors or Hepatitis C patients with the virus type. Lab tests are:

- Albumin Blood Test (ALB) g/L
- Alkaline Phosphatase Test (ALP) IU/L
- Alanine Transaminase Test (ALT) U/L
- Aspartate Transaminase Test (AST) U/L
- Bilirubin Blood Test (BIL) µmol/L
- Cholinesterase (CHE) kU/L
- Cholesterol (CHOL) mmol/L
- Creatinine Blod Test (CREA) µmol/L
- Gamma-Glutamyl Transpeptidase Test (GGT) U/L
- Protein Blood Test (PROT) g/L

## How the app works?

- Frontend (React) → sends user input (lab results, age, gender)
- Backend (FastAPI) → forwards input to ML model, gets prediction
- ML Model (pickle/joblib artifact) → processes and returns classification
- Backend → sends prediction result back to frontend