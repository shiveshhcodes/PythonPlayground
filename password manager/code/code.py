import os
from cryptography.fernet import Fernet

def load_key():
    folder_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/.txt files'
    file_path = os.path.join(folder_path, 'key.key')
    os.makedirs(folder_path, exist_ok=True)
    
    if not os.path.exists(file_path):
        key = Fernet.generate_key()
        with open(file_path, 'wb') as file:
            file.write(key)
    else:
        with open(file_path, 'rb') as file:
            key = file.read()
    
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    folder_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/.txt files'
    file_path = os.path.join(folder_path, 'password.txt')
    os.makedirs(folder_path, exist_ok=True)
    
    name = input("Enter the name: ")
    pwd = input("Enter the password: ")
    with open(file_path, 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    file_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/.txt files/password.txt'
    if not os.path.exists(file_path):
        print("No passwords stored yet.")
        return
    
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

while True:
    mode = input("What do you want to do with the password? view/add and q to quit - ").lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")