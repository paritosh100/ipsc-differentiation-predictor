import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="iPSC Purity Predictor", layout="wide")

# Load model
model = joblib.load("models/best_model_rf.pkl")  # Update path if needed
rf_purity = joblib.load("models/rf_purity.pkl")
rf_viability = joblib.load("models/rf_viability.pkl")
rf_yield = joblib.load("models/rf_yield.pkl")

# Title & description
st.title("🧬 iPSC Differentiation Outcome Predictor")
st.markdown("""
Welcome! This tool predicts **Purity (%)** — a measure of how successfully stem cells differentiate — 
based on your experimental setup. Whether you're a researcher, student, or just curious about stem cells,
this app helps visualize how protocol changes may influence outcomes.
""")

tab1, tab2, tab3 = st.tabs(["🧪 Prediction", "🧠 How It Works", "📚 Glossary"])

with tab1:
    st.header("📥 Enter Experimental Parameters")

    with st.form("protocol_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            BMP4 = st.slider("BMP4 (ng/mL)", 0.0, 100.0, 50.0, help="Growth factor used to guide differentiation.")
            ActivinA = st.slider("ActivinA (ng/mL)", 0.0, 100.0, 50.0)
            FGF2 = st.slider("FGF2 (ng/mL)", 0.0, 100.0, 50.0)

        with col2:
            Wnt3a = st.slider("Wnt3a (ng/mL)", 0.0, 100.0, 50.0)
            O2_Level = st.selectbox("Oxygen Level (%)", [5, 10, 20], help="O₂ tension during culture.")
            Seeding_Density = st.number_input("Seeding Density (cells/mL)", min_value=50000.0, max_value=200000.0, value=100000.0)

        with col3:
            Passage_Number = st.slider("Passage Number", 5, 30, 15, help="Number of times cells have been subcultured.")

            SOX2 = st.slider("SOX2 (log expr.)", 0.0, 10.0, 5.0)
            NANOG = st.slider("NANOG", 0.0, 10.0, 5.0)
            POU5F1 = st.slider("POU5F1", 0.0, 10.0, 5.0)
            CDX2 = st.slider("CDX2", 0.0, 10.0, 5.0)
            NEUROD1 = st.slider("NEUROD1", 0.0, 10.0, 5.0)

        submitted = st.form_submit_button("🔮 Predict Purity")

    if submitted:
        inputs = pd.DataFrame([{
            'BMP4': BMP4,
            'ActivinA': ActivinA,
            'FGF2': FGF2,
            'Wnt3a': Wnt3a,
            'O2_Level': O2_Level,
            'Seeding_Density': Seeding_Density,
            'Passage_Number': Passage_Number,
            'SOX2': SOX2,
            'NANOG': NANOG,
            'POU5F1': POU5F1,
            'CDX2': CDX2,
            'NEUROD1': NEUROD1
        }])
        pred_purity = rf_purity.predict(inputs)[0]
        pred_viability = rf_viability.predict(inputs)[0]
        pred_yield = rf_yield.predict(inputs)[0]

        col1, col2, col3 = st.columns(3)
        col1.metric("🎯 Predicted Purity (%)", f"{pred_purity:.2f}")
        col2.metric("🧪 Viability (%)", f"{pred_viability:.2f}")
        col3.metric("📦 Yield (%)", f"{pred_yield:.2f}")
        with st.expander("📋 View Input Parameters Used"):
            st.dataframe(inputs.style.format("{:.2f}"))
        inputs["Predicted_Purity"] = pred_purity
        inputs["Predicted_Viability"] = pred_viability
        inputs["Predicted_Yield"] = pred_yield

        csv = inputs.to_csv(index=False).encode("utf-8")

        st.download_button("📥 Download Results as CSV", data=csv, file_name="prediction_result.csv", mime="text/csv")

with tab2:
    st.header("🧠 How the Model Works")

    st.markdown("""
This app uses a **Random Forest Regression model** trained on synthetic data that simulates iPSC experiments.

- Each input (like BMP4 or SOX2) plays a role in cell fate decisions.
- The model was trained on 120 experiments with varied parameters.
- The output is **Purity (%)**, predicted based on your inputs.

We chose Random Forest because:
- It handles small datasets well.
- It's interpretable and robust to noise.
- It gave the best performance compared to XGBoost, MLP, and TabNet.
    """)

    st.image("model_comparison_final.png", caption="📊 Model Performance Comparison")


with tab3:
    st.header("📚 Glossary of Terms")

    st.markdown("""
- **iPSC**: Induced pluripotent stem cell — a stem cell made by reprogramming adult cells.
- **Purity**: How many cells became the intended type after differentiation.
- **BMP4 / ActivinA / FGF2 / Wnt3a**: Cytokines (growth signals) used to direct cell fate.
- **Seeding Density**: How many cells you start with.
- **Passage Number**: Number of times cells have been split and regrown.
- **SOX2 / NANOG / POU5F1**: Genes indicating stemness.
- **CDX2 / NEUROD1**: Genes indicating early lineage markers.
    """)
