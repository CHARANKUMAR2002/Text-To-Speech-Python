from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pyttsx3


root = Tk()
root.title("Text To Speech (Offline)")
root.geometry("680x485")
root.iconbitmap("ts.ico")
root.resizable(0,0)
root.config(bg="white")



def Import():
    global file, file_fill
    file = filedialog.askopenfilename(initialdir="C:/Users/Welcome/Documents", title='Select Text File', filetype=(("Text Files", "*.txt"), ("All Files", "*.*")))
    f = open(file)
    file_fill = f.readlines(100000000000000)
    text.insert(0.0, file_fill)
    text.config(state=DISABLED)


Button(root, text="Import Text File", command=Import, bd=0, bg='white').pack(pady=10)
text = ScrolledText(root, background='blue', foreground='white', selectbackground="red", selectforeground="yellow")
text.pack(pady=5, padx=10)


def play():
    t = text.get(0.0, END)
    speak = pyttsx3.init()
    speak.setProperty('rate', 150)
    speak.setProperty('volume', 1)
    speak.say(text=t)
    speak.runAndWait()
    root.update_idletasks()
    
def clear():
    text.config(state=NORMAL)
    text.delete(0.0, END)


def edit():
    text.config(state=NORMAL)


Button(root, text="Clear", command=clear, bd=0, bg='white').place(x=395, y=450)

speak = Image.open('read.png')
speak_button = ImageTk.PhotoImage(speak)

Button(root, image=speak_button, command=play, bd=0).pack(pady=5)


Button(root, text="Edit", command=edit, background='white', bd=0).place(x=250, y=450)


root.mainloop()