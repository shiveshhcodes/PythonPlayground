from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x500")
sp.config(bg="white")

lab = Label(sp,text="Internet Speed Test" , font=("Time New Roman" , 40, "bold"))
lab.place(x=40,y=40)

sp.mainloop()