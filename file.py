# dashboard.py

import streamlit as st
import pandas as pd
import numpy as np

st.title("🏀 Sports Betting Analytics Prototype")
st.write(
    "This app will eventually visualize sports betting trends and regression results."
)

# Example placeholder dataframe
df = pd.DataFrame({
    "Team": ["Lakers", "Celtics", "Heat", "Warriors"],
    "Spread": [-4.5, +2.5, -3.0, +1.0],
    "Win Probability": [0.60, 0.45, 0.62, 0.51]
})

st.subheader("Sample Data")
st.dataframe(df)

# A quick chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Spread", "Odds", "Edge"])
st.line_chart(chart_data)
