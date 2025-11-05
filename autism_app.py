import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import speech_recognition as sr

# Load model and encoders
model = joblib.load("autism_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# --- Sidebar Info ---
st.sidebar.markdown("## 🧠 About the App")
st.sidebar.info("""
This app predicts the **type of Autism Spectrum Disorder (ASD)** 
based on patient behavioral and cognitive features and also categorizes severity.

**Types of ASD:**
- Classic Autism
- Asperger's Syndrome
- PDD-NOS
- High Functioning Autism

**Severity Levels:**
- Small
- Moderate
- High

👉 Built with ML & Streamlit
""")

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🧠 Autism Spectrum Disorder Predictor</h1>", unsafe_allow_html=True)

# --- Speech Recognizer Function ---
def record_speech(prompt):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info(f"Listening for: {prompt}")
            audio = recognizer.listen(source, timeout=5)
            try:
                text = recognizer.recognize_google(audio)
                st.success(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                st.warning("Could not understand audio")
                return ""
            except sr.RequestError:
                st.warning("Could not request results; check your internet connection")
                return ""
    except:
        st.warning("Microphone not detected or not working")
        return ""

# --- Input Fields with Optional Speech ---
st.markdown("### 👤 Enter Patient Details")

def input_with_speech(label, options=None, min_val=None, max_val=None):
    col1, col2 = st.columns([3,1])
    with col1:
        if options:  # Dropdown
            value = st.selectbox(label, options)
        else:       # Numeric input
            value = st.number_input(label, min_value=min_val, max_value=max_val, value=min_val if min_val else 0)
    with col2:
        if st.button(f"🎤 Speak: {label}"):
            spoken = record_speech(label)
            if options and spoken in options:
                value = spoken
            else:
                try:
                    value = int(float(spoken))
                except:
                    st.warning(f"Could not convert speech to value for {label}")
    return value

# Collect inputs
age = input_with_speech("Age", options=[""] + list(range(1, 101)))
gender = input_with_speech("Gender", options=["", "M", "F"])
ethnicity = input_with_speech("Ethnicity", options=["", "Asian", "White-European", "Middle Eastern", "Black", "Latino", "South Asian", "Hispanic", "Others", "Turkish", "Pasifika", "Mixed", "Native Indian", "Other", "African"])
eye_contact = input_with_speech("Eye Contact (1–10)", min_val=1, max_val=10)
repetitive_behavior = input_with_speech("Repetitive Behavior (1–10)", min_val=1, max_val=10)
social_interaction = input_with_speech("Social Interaction (1–10)", min_val=1, max_val=10)
communication_skills = input_with_speech("Communication Skills (1–10)", min_val=1, max_val=10)
speech_delay = input_with_speech("Speech Delay (1–10)", min_val=1, max_val=10)
motor_skills = input_with_speech("Motor Skills (1–10)", min_val=1, max_val=10)
family_history = input_with_speech("Family History (1–10)", min_val=1, max_val=10)
IQ = input_with_speech("IQ", min_val=50, max_val=160)
sensory_sensitivity = input_with_speech("Sensory Sensitivity (1–10)", min_val=1, max_val=10)
anxiety = input_with_speech("Anxiety (1–10)", min_val=1, max_val=10)

# --- Function to Calculate Severity ---
def calculate_severity(inputs):
    score = inputs[3] + inputs[4] + inputs[5] + inputs[6] + inputs[11] + inputs[12]
    if score <= 30:
        return "Small"
    elif score <= 45:
        return "Moderate"
    else:
        return "High"

# --- Predict Button ---
if st.button("🎯 Predict Autism Type"):
    inputs = [age, gender, ethnicity, eye_contact, repetitive_behavior, social_interaction,
              communication_skills, speech_delay, motor_skills, family_history, IQ,
              sensory_sensitivity, anxiety]

    if "" in inputs:
        st.warning("⚠️ Please fill in all fields before predicting.")
    else:
        # Encode categorical features
        inputs[1] = label_encoders["gender"].transform([inputs[1]])[0]
        inputs[2] = label_encoders["ethnicity"].transform([inputs[2]])[0]

        input_array = np.array([inputs], dtype=float)

        # Input summary
        with st.expander("📋 Input Summary"):
            feature_names = ["age", "gender", "ethnicity", "eye_contact", "repetitive_behavior", "social_interaction",
                             "communication_skills", "speech_delay", "motor_skills", "family_history", "IQ",
                             "sensory_sensitivity", "anxiety"]
            st.write(pd.DataFrame(input_array, columns=feature_names))

        # Predict ASD type
        prediction = model.predict(input_array)[0]
        asd_type = label_encoders["ASD_Type"].inverse_transform([prediction])[0]

        # Calculate severity
        severity = calculate_severity(inputs)

        st.success(f"🌟 Predicted Autism Type: **{asd_type}**")
        st.info(f"⚡ Severity Level: **{severity}**")

        # Descriptions
        descriptions = {
            "Classic Autism": "Classic Autism is characterized by significant language delays, social and communication challenges, and unusual behaviors and interests.",
            "Asperger": "Asperger's Syndrome often includes average or above-average intelligence but difficulties in social interactions and nonverbal communication.",
            "PDD-NOS": "PDD-NOS (Pervasive Developmental Disorder - Not Otherwise Specified) refers to symptoms that don’t fully meet criteria for other ASD types.",
            "High Functioning Autism": "Individuals with High Functioning Autism usually have milder symptoms and higher intellectual abilities."
        }
        st.write(descriptions.get(asd_type, ""))

        # Prescriptions
        prescriptions = {
            "Classic Autism": """
            **Prescriptions & Recommendations:**
            - Early intensive behavioral intervention (EIBI)
            - Speech and language therapy
            - Occupational therapy for motor and sensory skills
            - Structured routines and social skills training
            - Family counseling and support
            """,
            "Asperger": """
            **Prescriptions & Recommendations:**
            - Social skills training
            - Cognitive Behavioral Therapy (CBT) for anxiety
            - Support for executive function and planning
            - Encourage special interests for confidence building
            """,
            "PDD-NOS": """
            **Prescriptions & Recommendations:**
            - Individualized education plans
            - Behavioral therapy tailored to specific challenges
            - Speech and language support as needed
            - Social and emotional skills support
            """,
            "High Functioning Autism": """
            **Prescriptions & Recommendations:**
            - Focused support on social communication
            - CBT or counseling for stress/anxiety management
            - Occupational therapy for fine motor skills if needed
            - Encourage academic and personal strengths
            """
        }
        st.markdown(prescriptions.get(asd_type, "No prescription available."))

        # --- Graph ---
        fig, ax = plt.subplots()
        symptom_labels = ["Eye Contact", "Repetitive Behavior", "Social Interaction",
                          "Communication Skills", "Speech Delay", "Motor Skills",
                          "Family History", "IQ", "Sensory Sensitivity", "Anxiety"]
        numeric_inputs = [eye_contact, repetitive_behavior, social_interaction,
                          communication_skills, speech_delay, motor_skills,
                          family_history, IQ, sensory_sensitivity, anxiety]
        ax.barh(symptom_labels, numeric_inputs, color="#4B8BBE")
        ax.set_xlabel("Score / IQ")
        ax.set_title("Patient Symptom Scores")
        st.pyplot(fig)
