# 🏃 Walk or Run Classifier — PRCP-1013

A machine learning web app that predicts whether a person is **walking or running** based on wrist-worn sensor data.

## 🎯 Project Overview

| | |
|---|---|
| **Project ID** | PRCP-1013 |
| **Type** | Binary Classification |
| **Best Model** | LightGBM |
| **Test Accuracy** | 99.27% |
| **Dataset** | 88,588 wrist sensor readings |

## 🚀 Live Demo
[👉 Click here to try the app](https://walkrun-classifier.onrender.com)

## �� Models Trained

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
├── Data/
│   └── walkrun.csv
├── PRCP-1013-WalkRunClass.ipynb
├── app.py
├── walkrun_best_model.pkl
├── walkrun_scaler.pkl
├── requirements.txt
└── README.md
```

## 🔧 Features Used

| Feature | Description |
|---------|-------------|
| wrist | Sensor placement (0=Left, 1=Right) |
| acceleration_x/y/z | Raw accelerometer readings |
| gyro_x/y/z | Raw gyroscope readings |
| acc_magnitude | Total resultant acceleration |
| gyro_magnitude | Total rotational intensity |
| acc_energy | Signal energy |
| jerk_proxy | Combined linear + rotational jerk |
| acc_std_proxy | Cross-axis variability |

## 🛠️ Run Locally
```bash
git clone https://github.com/YOURUSERNAME/walkrun-classifier.git
cd walkrun-classifier
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 📈 Key Findings

1. **Vertical acceleration** (`acceleration_y`) is the strongest signal (r = +0.64)
2. **Boosting models** consistently outperform all other families
3. **Feature engineering** added measurable value to model performance
4. **Final test accuracy is fully unbiased** — test set touched exactly once

## 👤 Author
**Uwais** | Data Science Capstone Project
