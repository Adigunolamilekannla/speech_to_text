# Speech-to-Text Application using Whisper Large V3

##  Project Overview
This project is a **Speech-to-Text (STT) web application** built using the open-source **Whisper Large V3** model.  
The model is deployed using **:contentReference[oaicite:0]{index=0}** for fast inference, and a simple, interactive user interface is created using **:contentReference[oaicite:1]{index=1}**.

The application allows users to upload or record audio and receive accurate text transcriptions in real time.

This project was developed as part of an academic assignment given by my lecturer.

---

##  Objectives
- Convert speech audio into text accurately
- Use an open-source, state-of-the-art speech recognition model
- Deploy the model using high-performance inference
- Provide an easy-to-use web-based interface

---

##  Model Used
- **Model Name:** Whisper Large V3  
- **Type:** Automatic Speech Recognition (ASR)  
- **Features:**
  - High transcription accuracy
  - Supports multiple languages
  - Robust to noise and accents
  - Open-source model

---

##  Technologies Used
- **Programming Language:** Python  
- **Speech-to-Text Model:** Whisper Large V3  
- **Inference Platform:** Groq  
- **User Interface:** Gradio  

---

## 🖥️ Application Features
- Upload audio files (e.g., `.wav`, `.mp3`)
- Record audio directly from the browser
- Fast and accurate transcription
- Simple and user-friendly interface

---

##  How It Works
1. User uploads or records an audio file.
2. The audio is sent to the Whisper Large V3 model.
3. The model processes the audio using Groq’s inference engine.
4. Transcribed text is displayed on the Gradio interface.

---

## 📦 Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Adigunolamilekannla/speech_to_text.git
cd speech_to_text

## Install Dependencies
pip install -r requirements.txt

## run the application the application will open in Browser
python app.py



#After running the application sucessully, open the provided local URL (usually http://127.0.0.1:7860) in your browser.

# project sruture 

├── app.py
├── requirements.txt
├── README.md
└── experiment.ipynb
