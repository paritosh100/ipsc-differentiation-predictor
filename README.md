
# 🧬 iPSC Differentiation Outcome Predictor

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Streamlit-ff4b4b?logo=streamlit)](https://your-streamlit-app-url.streamlit.app/)

---

## 🔍 Overview

This project simulates and predicts the outcomes of **iPSC (Induced Pluripotent Stem Cell) differentiation protocols** using machine learning.

We've built a smart, interactive dashboard that predicts:
- **Purity** (% of desired cell types)
- **Viability** (how many cells survive)
- **Yield** (overall success rate of protocol)

All based on inputs like cytokine concentrations, oxygen levels, seeding density, and gene expression markers.

---

## 🧪 What This Does

This tool helps:
- **Researchers** simulate new experimental protocols
- **Biotech teams** optimize stem cell yields
- **Students** understand the impact of protocol decisions on cell outcomes

---

## 💡 How It Works

1. **Data Simulation**  
   Synthetic datasets modeled on real biological parameters (e.g., BMP4, FGF2, SOX2)

2. **Model Training**  
   We trained several models including:
   - Random Forest (🏆 best performer)
   - XGBoost
   - TabNet
   - MLP Neural Network

3. **Prediction Engine**  
   The app uses the best model to generate predictions on user input.

4. **SHAP Explanations (NEW)**  
   We now include **SHAP (Shapley Additive Explanations)** visualizations to explain:
   - Which features influence Purity predictions
   - Waterfall breakdown for individual protocols
   - Side-by-side visuals in Streamlit for interpretability

5. **Dashboard App**  
   Built with Streamlit for accessibility and ease-of-use — no coding needed!

---

## 📊 Model Performance Summary

- **Random Forest** performed best overall
- Metrics:

```
- Linear Regression — R²: 0.8491, MAE: 1.7373, RMSE: 2.0581
- XGBoost — R²: 0.8438, MAE: 1.8502, RMSE: 2.0940
- Random Forest — R²: 0.8718, MAE: 1.5575, RMSE: 1.8968 ✅
- TabNet (Optimized) — R²: 0.8622, MAE: 1.5711, RMSE: 1.9670
- MLP — R²: 0.4996, MAE: 3.3232, RMSE: 3.7478
```

---

## 📦 Tech Stack

- `Python`, `Pandas`, `NumPy`
- `scikit-learn`, `XGBoost`, `pytorch-tabnet`, `SHAP`
- `Streamlit` for interactive app
- `Joblib` for saving models

---

## 📁 Repo Structure

```
📦 ipsc-differentiation-predictor/
├── notebooks/                  # Jupyter notebooks with training + analysis
├── models/                     # Saved ML models
├── data/                       # Simulated dataset
├── streamlit_app.py            # Main app file
├── requirements.txt
└── README.md
```

---

## 📌 Project Status

✅ Predicts Purity, Viability, and Yield  
✅ Clean Streamlit interface  
✅ SHAP-based model explanations ✅  
✅ Model comparison + exportable predictions  
🔜 Protocol optimizations + dashboard

---

## 📈 Versioning / Changelog

### 🔹 Version 1.0 – Pre-SHAP
- Built ML models for Purity prediction
- Developed and deployed Streamlit dashboard
- Model comparison and feature importance using sklearn

### 🔹 Version 1.1 – Post-SHAP
- Added SHAP explanations for model interpretability
- Global feature summary + waterfall plots for top protocol
- Side-by-side SHAP visualization in Streamlit
- Improved README and performance insights

---

## 👋 Want to Collaborate?

Feel free to fork, open issues, or reach out. Happy to connect with folks in stem cell research, bioinformatics, or ML for biology!

---

© 2025 — Built with ❤️ for science and curiosity.
