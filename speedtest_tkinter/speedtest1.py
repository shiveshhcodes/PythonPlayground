#TO - DO

from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed")
sp.geometry("560x580")
sp.config(bg="green")

lab = Label(sp,text="Internet Speed Test" , font=("Time New Roman" , 30 , "bold"))
lab.place(x=40,y=40)

sp.mainloop()