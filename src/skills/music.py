import music_library
import webbrowser
from speech.speak import speak 

def play_music(command):
    song = command.lower().split(" ")[1]
    link = music_library.music[song]
    speak("Playing song!")
    webbrowser.open(link)
    print("playing song...")