from speak import Speak
import speech_recognition as sr
import pyaudio
import webbrowser
# webbrowser.open('www.google.com')
# Speak('Hello world')
r = sr.Recognizer()
with sr.Microphone() as source:
    # print("Listening......")
    audio = r.listen(source)
    print('done')
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"USER: {query}\n")

    except Exception:
        print("Did not catch that")  