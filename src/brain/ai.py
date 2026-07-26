import ollama
from google import genai
from google.genai import types
from config import key

# --- Switch here: True = use Gemini (cloud, current data, needs internet+key) ---
# ---              False = use Ollama (local, offline, but weaker/outdated knowledge) ---
USE_GEMINI = True

system_prompt = (
    "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud. "
    "Respond in the same language the user's question is asked in. "
    "Give brief, well-summarized responses."
)

# Gemini client — created once at import time, reused for every call
client = genai.Client(api_key=key)

# --- Ollama history: list of {"role": "system"/"user"/"assistant", "content": "..."} ---
ollama_history = [
    {"role": "system", "content": system_prompt}
]

# --- Gemini history: list of {"role": "user"/"model", "parts": [{"text": "..."}]} ---
# Gemini does NOT take "system" as a role in this list — the system prompt is passed
# separately via config=types.GenerateContentConfig(system_instruction=...) below.
gemini_history = []


def ai_process_gemini(command):
    gemini_history.append({"role": "user", "parts": [{"text": command}]})

    response = client.models.generate_content(
        model="gemini-flash-latest",  # Flash, not Pro — Pro's free tier is ~50 requests/day, Flash is ~1500/day
        contents=gemini_history,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        ),
    )

    reply_text = response.text
    gemini_history.append({"role": "model", "parts": [{"text": reply_text}]})
    return reply_text


def ai_process_ollama(command):
    ollama_history.append({"role": "user", "content": command})

    response = ollama.chat(model="llama3.2", messages=ollama_history)
    reply_text = response["message"]["content"]

    ollama_history.append({"role": "assistant", "content": reply_text})
    return reply_text


def AiProcess(command):
    if USE_GEMINI:
        try:
            return ai_process_gemini(command)
        except Exception as e:
            # If Gemini fails (rate limit, no internet, bad key), fall back to Ollama
            # instead of crashing the whole assistant.
            print("Gemini failed, falling back to Ollama:", e)
            return ai_process_ollama(command)
    else:
        return ai_process_ollama(command)

def translate_to_hindi(text):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=text,  # <- actual text jo translate karna hai, seedha yahan
        config=types.GenerateContentConfig(
            system_instruction="Translate the given text to Hindi. Keep it natural and brief. Only return the translation, nothing else."
        ),
    )
    return response.text