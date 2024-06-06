# import speech_recognition as sr
# import os

# def say(text):
#     os.system(f"say {text}")
    
# def TakeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         audio = r.listen(source)
#         query = r.recognize_google(audio, language="en-in")
#         print(f"User Said: {query}")
#         return query
        
# say("Hello , i am Jarvis A I")
# while True:
#     print("Listening...")
#     text = TakeCommand()
#     say(text)


import speech_recognition as sr
import os

def say(text):
    os.system(f"say {text}")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Adjusting for ambient noise...")
        # r.adjust_for_ambient_noise(source)
        print("Listening...")
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
    text = TakeCommand()
    say(text)
