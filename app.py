import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the model
@st.cache_resource
def load_model():
    with open('rock_vs_mine_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("🪨 Rock vs 💣 Mine Prediction")
st.subheader("Simple Random Forest Model - Manual Input")

st.markdown("""
Enter the 60 sonar frequency band values (between **0.0 and 1.0**).  
Default values are from a sample **Rock**. Change them as needed and click **Predict**.
""")

# Create 60 number inputs in a clean layout
st.subheader("Sonar Measurements (V1 to V60)")

# Use columns to make it look better (4 columns per row)
cols = st.columns(4)

values = []
for i in range(60):
    # Reasonable default values (mostly low for a rock sample)
    default_val = round(0.02 + (i * 0.008), 4)   # simple increasing pattern
    if i > 40:  
        default_val = round(default_val * 0.6, 4)  # lower values at the end (common in rocks)

    with cols[i % 4]:
        val = st.number_input(
            f"V{i+1}", 
            min_value=0.0, 
            max_value=1.0, 
            value=default_val, 
            step=0.001,
            format="%.4f",
            key=f"v{i}"
        )
        values.append(val)

# Convert to DataFrame for prediction
input_data = pd.DataFrame([values])

# Predict button
if st.button("🚀 Predict Rock or Mine", type="primary"):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if prediction == "M":
            st.metric("🔮 Prediction", "💣 MINE", delta="High Risk")
        else:
            st.metric("🔮 Prediction", "🪨 ROCK", delta="Safe")
    
    with col2:
        confidence = max(probabilities) * 100
        st.metric("Confidence", f"{confidence:.1f}%")
    
    # Probability chart
    st.subheader("Prediction Probability")
    prob_df = pd.DataFrame({
        "Class": ["Rock (R)", "Mine (M)"],
        "Probability (%)": [prob * 100 for prob in probabilities]
    })
    st.bar_chart(prob_df.set_index("Class"))
    
    st.success("✅ Prediction completed!")

# Optional: Reset to default button
if st.button("Reset to Default Values"):
    st.rerun()

st.caption("Simple Logistic Regression Model | Values between 0.0 – 1.0 | Pickle loaded")