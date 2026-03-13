# 🏃 Walk or Run Classifier — PRCP-1013

A machine learning web app that predicts whether a person is **walking or running** based on wrist-worn sensor data.

## 🚀 Live Demo
### 👉 [https://walkrun-classifier.onrender.com](https://walkrun-classifier.onrender.com)

## 📊 Project Overview

| | |
|---|---|
| **Project ID** | PRCP-1013 |
| **Type** | Binary Classification |
| **Best Model** | LightGBM |
| **Test Accuracy** | 99.27% |
| **Dataset** | 88,588 wrist sensor readings |

## 🚀 Live Demo
### 👉 [https://walkrun-classifier.onrender.com](https://walkrun-classifier.onrender.com)

## 🏆 Model Results

| Model | Accuracy |
|-------|----------|
| LightGBM | **99.25%** |
| XGBoost | 99.22% |
| KNN (k=5) | 99.17% |
| Gradient Boosting (Tuned) | 99.08% |
| Random Forest (Tuned) | 98.93% |
| Extra Trees (Tuned) | 98.89% |
| Decision Tree | 98.07% |
| Logistic Regression | 95.94% |
| Gaussian Naive Bayes | 69.09% |

## 📁 Project Structure
```
walkrun-classifier/
├── Data/walkrun.csv
├── PRCP-1013-WalkRunClass.ipynb
├── app.py
├── walkrun_best_model.pkl
├── walkrun_scaler.pkl
├── requirements.txt
└── README.md
```

## 🛠️ Run Locally
```bash
git clone https://github.com/uwaiszmuhammed07-hash/walkrun-classifier.git
cd walkrun-classifier
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 👤 Author
**Uwais** | Data Science Capstone Project — PRCP-1013
