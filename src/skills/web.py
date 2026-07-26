import webbrowser
from speech.speak import speak 
import os
def open_google():
    speak("Opening Google!")
    print("Opening Google!")
    webbrowser.open("https://google.com")

def open_facebook():
    speak("Opening Facebook!")
    print("Opening Facebook!")
    webbrowser.open("https://facebook.com")

def open_youtube():
    speak("Opening Youtube!")
    print("Opening Youtube!")
    webbrowser.open("https://youtube.com")

def open_whatsapp():
    speak("Opening WhatsApp!")
    print("Opening WhatsApp!")
    os.system("start whatsApp:")