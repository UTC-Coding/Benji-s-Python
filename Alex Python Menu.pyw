from tkinter import *
from tkinter import ttk
import os

NORM_FONT = ("Helvetica", 10)




    
root = Tk()
root.minsize(width=350, height=300)
root.maxsize(width=350, height=300)
root.configure(background='blue')
menubar = Menu(root)
root.title("AlexLamb menu")
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)


  
b1 = Button(root, text = "Chrome", command=lambda : os.startfile('c:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
b1.place(x=10,y=10)

b3 = Button(root, text = "Office Word", command=lambda : os.startfile('c:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE'))
b3.place(x=70,y=10)

b4 = Button(root, text = "Office Powerpoint", command=lambda : os.startfile ('c:\Program Files (x86)\Microsoft Office\Office16\POWERPNT.exe'))
b4.place(x=150,y=10)

b5 = Button(root, text = "Office Outlook", command=lambda :os.startfile('c:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.exe'))
b5.place(x=260,y=10)

b6 = Button(root, text = "Office Onenote", command=lambda :os.startfile('c:\Program Files (x86)\Microsoft Office\Office16\ONENOTE.exe'))
b6.place(x=10,y=40)


EXITb = Button(root, text = "EXIT", command=lambda : root.destroy())
EXITb.place(x=310,y=270)

root.config(menu=menubar)
root.mainloop()

