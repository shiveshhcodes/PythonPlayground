import os
from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

'''
def write_key():
    keyfolder_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/encrypted key'
    keyfile_path = os.path.join(keyfolder_path , 'key.key')
    os.makedirs(keyfolder_path , exist_ok=True)
    
    key = Fernet.generate_key()
    with open(keyfile_path , "wb") as key_file:
        key_file.write(key) '''
    
def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key
def add():
    folder_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/.txt files'
    file_path = os.path.join(folder_path , 'password.txt')
    os.makedirs(folder_path , exist_ok=True)
    
    name = input("Enter the name: ")
    pwd = input("Enter the password: ")
    with open(file_path, 'a') as f:
        f.write(name + "|" + pwd + "\n")
        

def view():
    with open('/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user , passw = data.split("|")
            print("User:" , user , "| Password:" , passw)

while True:
    mode = input("What do you want to do with the password? view/add and q to quit - ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
