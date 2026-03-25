import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="Trigofy", layout="centered")

st.title("🔺 Trigofy")
st.subheader("Learn Trigonometry Visually")

angle = st.number_input("Enter angle (degrees):", value=30.0)
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

# Graph (NO matplotlib)
x = np.linspace(0, 360, 200)
x_rad = np.radians(x)

if func == "sin":
    y = np.sin(x_rad)
elif func == "cos":
    y = np.cos(x_rad)
else:
    y = np.tan(x_rad)

st.line_chart({"x": x, "y": y})