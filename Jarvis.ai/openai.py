import speech_recognition as sr
import os
import webbrowser
import shutil

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
    
    
say("I am Jarvis A I")
while True:
    print("Listening...")
    query = TakeCommand()
    
    # open websites 
    sites = [["youtube" , "https://youtube.com"] , ["wikipedia" , "https://wikipedia.com"] , ["google" , "https://google.com"]]
    for site in sites:
        if f"open {site[0]}" in query.lower():
            say(f"opening {site[0]} shivesh")
            webbrowser.open(site[1])
    
    if "open facetime".lower() in query.lower():
        os.system(f"open /System/Applications/FaceTime.app")  
        
    if "open photos".lower() in query.lower():
        os.system(f"open /System/Applications/Photos.app")
        
    if "copy paste".lower() in query.lower():
        source_file = input("Source File - ")
        # desination_dir = input("Destination File - ")
        destination_file_name = input("file name - ")
        
        source = f"/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/Jarvis.ai/{source_file}"
        desination = f"/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/Jarvis.ai"
        
        desination_file = os.path.join(desination , destination_file_name)
        
        if not os.path.exists(desination):
            print(f"Creating Directory {desination}")
            os.makedirs(desination)

        if os.path.exists(source):
         shutil.copy(source , desination_file)
    

    
