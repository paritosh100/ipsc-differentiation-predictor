
# 🧬 iPSC Differentiation Outcome Predictor

This project simulates and models the process of differentiating induced pluripotent stem cells (iPSCs) into specific cell types under various experimental protocols. It aims to **predict quality metrics** like **Purity, Viability, and Yield** using cytokine levels, oxygen concentration, seeding density, and gene expression markers.

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `01_data_generation.ipynb` | Simulates biologically inspired dataset for iPSC differentiation |
| `02_eda.ipynb` | Performs EDA: nulls, ranges, distributions, correlation matrix with heatmap |
| `03_modeling.ipynb` | Builds and compares predictive models (Linear, XGBoost, RF, MLP, TabNet) |
| `README.md` | Project overview and interpretation |
| `.gitignore` | Excludes virtualenv, system files from version control |

---

## 📊 What This Project Does

- Simulates data for 120 iPSC differentiation batches with realistic ranges for:
  - Cytokines (BMP4, ActivinA, FGF2, Wnt3a)
  - Culture conditions (O₂ level, seeding density, passage number)
  - Gene expression levels (SOX2, NANOG, CDX2, NEUROD1, etc.)
  - Output outcomes: **Purity**, **Viability**, **Yield**
- Explores relationships using **Pearson correlation with p-values**
- Models outcome (e.g. Purity) using:
  - **Linear Regression**
  - **XGBoost**
  - **Random Forest**
  - **MLP Neural Network**
  - (Upcoming) **TabNet**
- Evaluates and compares performance using:
  - **R²** (coefficient of determination)
  - **MAE** (mean absolute error)
  - **RMSE** (root mean square error)
- Visualizes feature importance to understand biological drivers of success

---

## 🧠 Model Comparison (Purity Prediction)

| Model              | R² (↑) | MAE (↓) | RMSE (↓) |
|-------------------|--------|---------|----------|
| Linear Regression | 0.8491 | 1.7373  | 2.0581   |
| XGBoost           | 0.8438 | 1.8502  | 2.0940   |
| Random Forest     | 0.870+ | ~1.55   | ~1.90    |
| MLP (Neural Net)  | 0.50   | 3.30+   | 3.80+    |

📌 **Linear Regression** surprisingly outperformed XGBoost, suggesting the relationships in this data are mostly linear.  
📌 **Random Forest** performed even better, capturing slight nonlinearities.  
📌 **MLP** underperformed due to sensitivity to scaling and the small dataset size.

---

## 🧪 For Non-Technical Readers

Imagine you're trying to cook the perfect dish using different ingredients. You vary the amounts of spices, the cooking temperature, and time — and record the outcome.

This project does the same, but for **stem cell experiments**. It analyzes how changing **inputs** (like BMP4 levels or gene activity) affects **results** (like how many cells turned into the right type, or how pure and alive they are).

We use different types of AI models to predict and optimize these outcomes. Some models are simple (like drawing a straight line), and some are more advanced (like decision trees or neural networks that mimic how the brain works).

---

## 🛠 How to Use

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run notebooks in order:
   - Start with `01_data_generation.ipynb`
   - Then `02_eda.ipynb`
   - Then `03_modeling.ipynb`

---

## 🔭 Future Work

- Add TabNet deep learning model with attention
- SHAP explainability for model transparency
- Streamlit dashboard for live protocol simulation

---

## 📜 License

MIT License — free for personal and commercial use with attribution.
