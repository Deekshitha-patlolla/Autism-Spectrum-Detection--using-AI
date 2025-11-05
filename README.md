
🌟 Introduction

This Streamlit-based web application is designed to predict the type of Autism Spectrum Disorder (ASD) in individuals using machine learning. It provides an intelligent, user-friendly, and interactive way to assess autism-related behavioral and cognitive patterns.

The app combines voice-based inputs, machine learning predictions, and visual analytics, making it both accessible and insightful for users like psychologists, researchers, and healthcare professionals. 🎯

⚙️ 1️⃣ Importing Required Libraries

The code begins by importing essential Python libraries:

🧮 NumPy & Pandas – For numerical and data handling.

📊 Matplotlib – For visualizing patient symptom patterns.

🎙️ SpeechRecognition – To capture patient details through speech.

💾 Joblib – To load the pre-trained ML model and encoders.

🌐 Streamlit – To create an interactive web interface.

🧩 2️⃣ Loading Machine Learning Model

The pre-trained model (autism_model.pkl) and categorical encoders (label_encoders.pkl) are loaded using joblib.
These files contain:

The trained classifier that predicts the ASD type.

The label encoders that convert categorical inputs (like gender, ethnicity) into numerical form for prediction.

If these files aren’t found, the app gracefully stops and alerts the user with an error message. 🚫

🎛️ 3️⃣ Sidebar Information

The sidebar gives users an overview of the app:

Explains ASD types such as Classic Autism, Asperger’s Syndrome, PDD-NOS, and High-Functioning Autism.

Shows severity levels: Small, Moderate, and High.

Mentions that the app is built using ML & Streamlit.
📚 This helps users quickly understand the app’s purpose.

🧏 4️⃣ Speech Recognition Integration

The record_speech() function allows users to input data by speaking instead of typing.
It:

Activates the microphone 🎤

Listens for speech for 5 seconds

Converts voice to text using Google’s Speech API

Displays what the user said on the screen

If the voice is unclear or the mic isn’t working, the app handles errors smoothly with friendly messages. ⚡

📝 5️⃣ Input Collection Section

This section gathers the patient’s details such as:

Age 👶

Gender 🚻

Ethnicity 🌍

Eye Contact, Repetitive Behavior, Social Interaction, Communication Skills, Speech Delay, Motor Skills, Family History, IQ, Sensory Sensitivity, and Anxiety 😌

Each input field also has a 🎤 speech button, enabling users to say their answers aloud instead of typing.
The function input_with_speech() handles this logic smartly.

🧮 6️⃣ Severity Level Calculation

The function calculate_severity() computes a severity score based on multiple behavioral and emotional features.
Depending on the total score:

Small 🟢 — Milder symptoms

Moderate 🟡 — Noticeable difficulties

High 🔴 — Severe autistic traits

This helps users understand not just the type but also the intensity of ASD.

🤖 7️⃣ Prediction Logic

When the user clicks “🎯 Predict Autism Type”, the app:

Checks if all inputs are filled ✅

Encodes categorical variables (Gender, Ethnicity) using label encoders.

Converts all inputs into a NumPy array suitable for ML model input.

Uses the loaded ML model to predict the type of ASD.

The model outputs a category that’s decoded back into human-readable form such as Classic Autism or Asperger’s Syndrome. 🧩

💡 8️⃣ Displaying Results

Once the prediction is complete:

🌟 The predicted ASD type is shown with emphasis.

⚡ The severity level (Small, Moderate, or High) is displayed.

🧠 A brief description of the predicted ASD type is provided — explaining its characteristics, such as language delays or social challenges.

💊 9️⃣ Prescriptions & Recommendations

Depending on the ASD type, the app gives personalized recommendations such as:

Behavioral therapy

Speech & occupational therapy

Family counseling

Social skills training

Cognitive Behavioral Therapy (CBT) for anxiety

This section adds real-world clinical value 💬 by guiding users on the next steps.

📈 🔟 Data Visualization

Finally, the app generates a horizontal bar chart displaying:

Eye contact

Repetitive behaviors

Social skills

Speech delay

IQ

Anxiety levels, etc.

This visualization helps compare symptom intensity across multiple domains in one glance. 📊
It offers a clear, visual summary of the patient’s behavioral profile.

🏁 Conclusion

This Streamlit app beautifully integrates:

🎤 Speech interaction

🧠 Machine learning prediction

💡 Explainability

📊 Visualization

It serves as a smart AI-powered diagnostic support system for understanding autism-related characteristics with simplicity and accessibility.

Built with compassion 💖, intelligence 🧩, and technology ⚙️ —
this app bridges the gap between AI and mental health awareness.

🌈 "Empowering early detection, enhancing understanding, and promoting inclusion for every mind." 🌈
