# SIMPLE GAME , which speaks whatever you say..

import os

print("Hi , welcome to Robo Speaker , Created By Shiveshhhh")
while True: 
    x = input("Hi , what do you want me to speak today?? ")
    if x == "quit":
        os.system("say 'Bye Bye Friend'")
        break
    command = f"say {x}"
    
    os.system(command)
