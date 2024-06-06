import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say {text}")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source)
        # print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return "Sorry, my speech service is down."

say("Hello, I am Jarvis A I")
while True:
    print("Listening...")
    query = TakeCommand()
    if "open youtube" in query.lower():
        webbrowser.open("https://youtube.com")
        say("opening Youtube shivesh")
        break
    
