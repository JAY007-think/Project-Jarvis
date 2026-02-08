# 🤖 Project Jarvis – Python Ai Powered Voice Assistant

A Python-based virtual voice assistant inspired by Alexa & Google Assistant.  
It can recognize voice commands, speak responses, open websites, play music,
fetch latest news, and answer general questions using AI.

---

## ✨ Features
- 🎙️ Voice command recognition
- 🗣️ Text-to-speech responses (Hindi support via gTTS)
- 🌐 Open Google, YouTube, Facebook, WhatsApp etc. you can add more further
- 🎵 Play songs using a custom music library (extendable)
- 📰 Fetch and speak latest news
- 🤖 AI-powered answers using OpenAI API

---

## 🛠️ Tech Stack
- Python
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- pygame (for audio playback)
- pyttsx3
- OpenAI API
- NewsAPI

---

## 📂 Project Structure
PROJECT-JARVIS/

├── src/

    └── main.py 
 
    └── music_library.py
 
├── .env.example

├── .gitignore

├── requirements.txt

├── README.md



---

## ⚙️ Installation & Setup

step 1️⃣. Clone the repository

step 2️⃣. Create virtual Environment
python -m venv .venv
.venv\Scripts\activate   

step 3️⃣. Install dependencies
pip install -r requirements.txt

step 4️⃣. Setup environment variables
Create a .env file in root folder:
    OPENAI_API_KEY=your_openai_api_key
    NEWS_API_KEY=your_news_api_key

step 5️⃣. Run the Assistant
python src/main.py


👨‍💻 Author

Jay Soni
LinkedIn: https://www.linkedin.com/in/jay-soni-01a791261/
LeetCode: https://leetcode.com/u/ZysIunJ150/

> This project was built as a learning exercise and enhanced with additional features.



