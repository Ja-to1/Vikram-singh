import streamlit as st

# Import Tran_Eff function
def Tran_Eff(VA, CL, FCL, K, PF):
    CUL = (K ** 2) * FCL
    Eff = (K * VA * PF) / (K * VA * PF + CL + CUL) * 100  # Convert to percentage
    return round(Eff, 2), round(CUL, 2)

# Streamlit UI
st.title("Transformer Efficiency and Copper Loss Calculator")
st.write("Calculate transformer efficiency and copper losses for different loads.")

# Input fields
VA = st.number_input("Transformer Rating (VA):", min_value=0.0, value=1000.0, step=100.0)
CL = st.number_input("Core Losses (Watts):", min_value=0.0, value=50.0, step=5.0)
FCL = st.number_input("Full Load Copper Losses (Watts):", min_value=0.0, value=100.0, step=5.0)
K = st.slider("Loading on Transformer (K):", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
PF = st.slider("Power Factor (PF):", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

# Calculate Efficiency and Copper Losses
if st.button("Calculate"):
    Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)
    st.success(f"Efficiency of Transformer: {Eff} %")
    st.success(f"Copper Losses at {K} Loading: {CUL} Watts")