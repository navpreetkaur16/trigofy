import streamlit as st
import numpy as np
import math
import pandas as pd

# Page setup
st.set_page_config(page_title="Trigofy", layout="centered")

# Custom title (better UI)
st.markdown(
    "<h1 style='text-align: center; color: #ef4444;'>🔺 Trigofy</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Learn Trigonometry Visually</p>",
    unsafe_allow_html=True
)

# Input
angle = st.number_input("Enter angle (degrees):", value=30.0)

# Function selection
func = st.radio("Choose function:", ["sin", "cos", "tan"])

r = math.radians(angle)

# Calculate
if func == "sin":
    value = math.sin(r)
    concept = "Sine = opposite / hypotenuse"
    real = "Used in waves and sound"
elif func == "cos":
    value = math.cos(r)
    concept = "Cosine = adjacent / hypotenuse"
    real = "Used in navigation and GPS"
elif func == "tan":
    value = math.tan(r)
    concept = "Tangent = opposite / adjacent"
    real = "Used in height and distance"

# Result
st.markdown("### 📊 Result")
st.success(f"{func}({angle}) = {round(value, 4)}")

# Explanation
st.markdown("### 📘 Explanation")
st.markdown(f"""
**Angle:** {angle}°  
**Radians:** {round(r, 4)}  

**Concept:**  
{concept}  

**Real-life use:**  
{real}  
""")

# Graph
x = np.linspace(0, 360, 200)
x_rad = np.radians(x)

if func == "sin":
    y = np.sin(x_rad)
elif func == "cos":
    y = np.cos(x_rad)
else:
    y = np.tan(x_rad)

# Data for graph
data = pd.DataFrame({
    "Degrees": x,
    "Value": y
})

st.markdown("### 📈 Graph")
st.line_chart(data.set_index("Degrees"))

# Highlight selected point
st.markdown("### 📍 Selected Point")
st.info(f"({angle}, {round(value, 4)})")

# Why it matters
st.markdown("### 🌍 Why this matters")
st.write(
    "Trigonometry is used in physics, engineering, navigation, "
    "architecture, and even game development."
)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Created by NAV</p>",
    unsafe_allow_html=True
)