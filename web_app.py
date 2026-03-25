import streamlit as st
import numpy as np
import math
import pandas as pd
import random

st.set_page_config(page_title="Trigofy", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #ef4444;'>🔺 Trigofy</h1>",
    unsafe_allow_html=True
)

st.markdown("<p style='text-align: center;'>Learn Trigonometry Visually</p>", unsafe_allow_html=True)

# Mode selection
mode = st.radio("Choose Mode:", ["Calculator", "Quiz"])

# ---------------- CALCULATOR MODE ----------------
if mode == "Calculator":
    angle = st.number_input("Enter angle (degrees):", value=30.0)
    func = st.radio("Choose function:", ["sin", "cos", "tan"])

    r = math.radians(angle)

    if func == "sin":
        value = math.sin(r)
        concept = "Sine = opposite / hypotenuse"
        real = "Used in waves and sound"
    elif func == "cos":
        value = math.cos(r)
        concept = "Cosine = adjacent / hypotenuse"
        real = "Used in navigation and GPS"
    else:
        value = math.tan(r)
        concept = "Tangent = opposite / adjacent"
        real = "Used in height and distance"

    st.markdown("### 📊 Result")
    st.success(f"{func}({angle}) = {round(value, 4)}")

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

    data = pd.DataFrame({"Degrees": x, "Value": y})
    st.line_chart(data.set_index("Degrees"))

# ---------------- QUIZ MODE ----------------
else:
    st.markdown("### 🧠 Quiz Mode")

    if "angle_q" not in st.session_state:
        st.session_state.angle_q = random.choice([0, 30, 45, 60, 90])
        st.session_state.func_q = random.choice(["sin", "cos", "tan"])

    angle = st.session_state.angle_q
    func = st.session_state.func_q

    st.write(f"What is {func}({angle}) ?")

    user_answer = st.number_input("Your answer:", value=0.0)

    if st.button("Check Answer"):
        r = math.radians(angle)

        if func == "sin":
            correct = math.sin(r)
        elif func == "cos":
            correct = math.cos(r)
        else:
            correct = math.tan(r)

        if abs(user_answer - correct) < 0.01:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! Correct answer: {round(correct, 4)}")

    if st.button("Next Question"):
        st.session_state.angle_q = random.choice([0, 30, 45, 60, 90])
        st.session_state.func_q = random.choice(["sin", "cos", "tan"])
        st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by NAV</p>", unsafe_allow_html=True)