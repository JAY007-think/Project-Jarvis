import speech_recognition as sr
r = sr.Recognizer()
from speech.speak import speak

def listen_for_wakeWord():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=5)
        word = r.recognize_google(audio).lower()
        print("Heard:", word)
            
        if "jarvis" in word:
            print("Jarvis Active...")
            speak("Welcome back sir!, how can I help you?")
            return True
        else:
            return False
        
def listen_for_command():
    # Listening for command...
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        command = r.recognize_google(audio).lower()
        print("command: ",command)
    return command