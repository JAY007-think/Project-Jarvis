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

<<<<<<< HEAD
=======
# speak function
def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the mp3 file
    pygame.mixer.music.load('temp.mp3')

    # play the mp3 file
    pygame.mixer.music.play()

    # keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
def AiProcess(command):
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general task like alexa and google cloud,but you always speak hindi and briefly, give short and better responses, you are made by a smart software devloper name JAY . you always give amazing answer which shocked peoples, you are highly trained assistant"},
        {"role":"user","content":command}
        ]
    )

    return completion.choices[0].message.content

# command processor
>>>>>>> 71c1e1ab3dfa5e1e03b05f2be3c64c6d50d7f446
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

