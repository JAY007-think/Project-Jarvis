from dotenv import load_dotenv
load_dotenv()
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import src.music_library as music_library
import os
import requests
from gtts import gTTS
import pygame

# Initialize
r = sr.Recognizer()
NewsApi = os.getenv("NEWS_API_KEY")


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
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general task like alexa and google cloud,but you always speak hindi and briefly, give short better responses"},
        {"role":"user","content":command}
        ]
    )

    return completion.choices[0].message.content

# command processor
def processCommand(command):
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google!")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook!")
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube!")
    elif "open whatsapp" in command:
        os.system("start whatsApp:")
        speak("Opening WhatsApp!")
    elif command.startswith("play"):
        song = command.lower().split(" ")[1]
        link = music_library.music[song]
        speak("Playing song!")
        webbrowser.open(link)
    elif "news" in command:
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=950122d8987446218b249f222f4a38a7")
        if r.status_code == 200:
            # parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get('articles',[])
            # Speak headlines
            for article in articles:
                speak(article['title'])

    else:
        # let OpenAI handle the command
        output = AiProcess(command)
        speak(output)
    
if __name__ == "__main__":
    speak("initializing jarvis")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from microphone
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5)
            word = r.recognize_google(audio).lower()
            print("Heard:", word)
            

            if "jarvis" in word:
                print("Jarvis Active...")
                speak("Yes, how can I help you?")
                # Listening for command...
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio).lower()
                    print("command: ",command)
                    processCommand(command)   

        except sr.WaitTimeoutError:
            pass  # silence, ignore

        except sr.UnknownValueError:
            speak("I could not understand")

        except Exception as e:
            print("Error:", e)

