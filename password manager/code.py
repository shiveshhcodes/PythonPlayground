import os
master_pwd = input("What is the master password? ")
def add():
    folder_path = '/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager'
    file_path = os.path.join(folder_path , 'password.txt')
    os.makedirs(folder_path , exist_ok=True)
    
    name = input("Enter the name: ")
    pwd = input("Enter the password: ")
    with open(file_path, 'a') as f:
        f.write("name is " + name + "and password = " + pwd + "\n")
        

def view():
    with open('/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/password manager/password.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())

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
