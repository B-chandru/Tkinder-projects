import ttkbootstrap as ttk
import pyttsx3
from PIL import ImageTk
import random
from tkinter import filedialog


if __name__ == '__main__':

    def texttospeech():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        voice_str=text_input.get("1.0", "end-1c")  
        if m_var.get()==1:
            engine.setProperty('voice', voices[m_var.get()].id) 
            engine.say(voice_str) 
            engine.runAndWait()
        elif m_var.get() ==0:
            engine.setProperty('voice', voices[m_var.get()].id) 
            engine.say(voice_str) 
            engine.runAndWait()

    def download():
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        voice_str=text_input.get("1.0", "end-1c")  
        if m_var.get()==1:
            engine.setProperty('voice', voices[m_var.get()].id) 
            engine.save_to_file(voice_str,  f'{str(folder_selected)}/Femalevoice{random.randint(0,100000)}.mp3')
            engine.runAndWait() 
        elif m_var.get() ==0:
            engine.setProperty('voice', voices[m_var.get()].id) 
            engine.save_to_file(voice_str, f'{str(folder_selected)}/Malevoice{random.randint(0,100000)}.mp3')
            engine.runAndWait() 

    window = ttk.Window()
    window.title("Text-To-Speech")
    window.geometry('700x450')
    frame = ttk.Frame(window,width=700,height=700)
    window.resizable(False,False)
 
    
    # icon- the below two lines of code is for icon 
   # img_icon =ImageTk.PhotoImage(file="logo/texttospeech.png")
    #window.iconphoto(False,img_icon)

    text_label =ttk.Label(frame,text="Enter Text To Convert Into Speech",font=("Times 20 bold"))
    text_input = ttk.Text(frame,height=6,font=("Times 14"), borderwidth=1, relief="solid", width=50, )
    m_var=ttk.IntVar()
    male_voice = ttk.Radiobutton(frame,text="Male", variable=m_var, value=0,cursor="hand2")
    female_voice = ttk.Radiobutton(frame,text="Female", variable=m_var, value=1,cursor="hand2" )
    btn = ttk.Button(frame,text="speak",command=texttospeech,cursor="hand2")
    download_btn = ttk.Button(frame,text="Download",command=download,cursor="hand2",bootstyle="success")


    text_label.place(x=80,y=30)
    text_input.place(x=40,y=80)
    male_voice.place(x=150,y=300)
    female_voice.place(x=250,y=300)
    btn.place(x=450,y=300)
    download_btn.place(x=280,y=380)
    frame.place(x=10,y=10)
    window.mainloop()
