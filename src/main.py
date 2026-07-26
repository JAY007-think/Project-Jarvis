from dotenv import load_dotenv
load_dotenv()
import os
import speech_recognition as sr
import music_library as music_library
import os
# from brain.ai import ai
from brain.ai import AiProcess
from speech import listen
from speech.speak import speak
from skills import web
from skills import music
from skills import news

    
NewsApi = os.getenv("NEWS_API_KEY")

def processCommand(command):
    if "open google" in command:
        web.open_google()
    elif "open facebook" in command:
        web.open_facebook()
    elif "youtube" in command:
        web.open_youtube()
    elif "open whatsapp" in command:
        web.open_whatsapp()
    elif command.startswith("play"):
        music.play_music(command)
    elif "news" in command:
        news.get_news(command)

    else:
        # let OpenAI handle the command
        output = AiProcess(command)
        speak(output)
    
if __name__ == "__main__":
    speak("Initializing JARVIS... ")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from microphone
        try:
            if(listen.listen_for_wakeWord() == True):
                # Listening for command...
                while True:
                    command = listen.listen_for_command()
                    if "stop" in command or "bye" in command:
                        break
                    processCommand(command)

        except sr.WaitTimeoutError:
            pass  # silence, ignore

        except Exception as e:
            print("Error:", e)

