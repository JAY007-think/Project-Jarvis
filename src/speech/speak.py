import asyncio
import os
import pygame
import edge_tts

pygame.mixer.init()
TEMP_FILE = "jarvis_temp.mp3"

# --- JARVIS IDENTITY VOICE ---
# Madhur ekmatra Hindi male neural voice hai Edge-TTS mein
HINDI_VOICE = "hi-IN-MadhurNeural"     

# --- JARVIS CINEMATIC AUDIO CONFIG ---
# Rate (+12%): AI assistants thoda tezi aur confidence se bolte hain
# Pitch (-10Hz): Isse aawaz mein heavy bass/gambhirtya aati hai jo exact Jarvis jaisi lagti hai
RATE = "+12%"
PITCH = "-10Hz"

def speak(text):
    try:
        # Rate aur Pitch variables ko Communicate function ke andar pass kiya
        communicate = edge_tts.Communicate(text, HINDI_VOICE, rate=RATE, pitch=PITCH)
        asyncio.run(communicate.save(TEMP_FILE))

        pygame.mixer.music.load(TEMP_FILE)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(TEMP_FILE)

    except Exception as e:
        print(f"Voice Error: {e}")
        try:
            pygame.mixer.music.unload()
            if os.path.exists(TEMP_FILE): os.remove(TEMP_FILE)
        except: pass

if __name__ == "__main__":
    # Note: Punctuation (commas and periods) bohot zaroori hain natural breaks ke liye
    speak("Welcome back, sir. All systems are fully operational.")
    speak("नमस्ते सर, I'm ready for working with you")
