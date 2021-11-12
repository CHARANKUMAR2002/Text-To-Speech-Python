from tkinter import *
from tkinter.scrolledtext import ScrolledText
from gtts import gTTS
from gtts.tts import gTTSError
from playsound import playsound
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Text To Speech")
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
text = ScrolledText(root, background='blue', foreground='white')
text.pack(pady=5, padx=10)


def play():
    t = text.get(0.0, END)
    try:
        audio = gTTS(text=t, lang="en", slow=False)
        audio.save("read.mp3")
        root.update_idletasks()
        playsound("read.mp3")
        root.update_idletasks()
        a = messagebox.askquestion("TTS", "Do You Want To Save The Audio?")
        if a == "yes":
            au = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Music", title='Save As',defaultextension=".jpg", filetype=(("MP3", "*.mp3"),("WAV", "*.wav")))
            audio.save(au)
            os.remove("read.mp3")
            messagebox.showinfo("TTS", "Audio Saved!")
        else:
            os.remove("read.mp3")
    except AssertionError:
        messagebox.showerror("Text To Speech", "Text File Not Imported or No Content is Manually Entered!\nPlease Import Or Enter The Content Manually!")
    except gTTSError:
        messagebox.showerror("Text To Speech", "Please Check You Internet Connection")

def clear():
    text.delete(0.0, END)
    text.config(state=NORMAL)


def edit():
    text.config(state=NORMAL)


Button(root, text="Clear", command=clear, bd=0, bg='white').place(x=395, y=450)

speak = Image.open('read.png')
speak_button = ImageTk.PhotoImage(speak)

Button(root, image=speak_button, command=play, bd=0).pack(pady=5)


Button(root, text="Edit", command=edit, background='white', bd=0).place(x=250, y=450)

root.mainloop()