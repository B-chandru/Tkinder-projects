import tkinter
import tkinter.messagebox
import pyshorteners
import pyperclip

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("URL Shortener")
    window.geometry('400x400')
    frame = tkinter.Frame(window)
    # function to copy the shorturl to clipboard
    def copytoclip():
        urlshort = pyshorteners.Shortener()
        short_url = urlshort.tinyurl.short(longurl.get())
        pyperclip.copy(short_url)
        pyperclip.paste()
        tkinter.messagebox.showinfo("URL shortener", "Copied to Clipboard")

   #function to create a shorturl for longurl
    def urlshortener():
        urlshort = pyshorteners.Shortener()
        short_url = urlshort.tinyurl.short(longurl.get())
        short_label = tkinter.Label(frame, text="This is your Short URL ",pady=10,font="Arial 15 ")
        shorturl = tkinter.Entry(frame,width=50,font="Arial 10 ")
        copy_btn = tkinter.Button(frame,text="copy", padx=10 ,command=copytoclip ,font="Arial 10 ")
        shorturl.insert(0,short_url)
        pyperclip.copy(short_url)
        pyperclip.paste()
        short_label.grid(row=3,column=1)
        shorturl.grid(row=4,column=1)
        copy_btn.grid(row=5,column=1,pady=10)
        # print(longurl.get())


    long_label = tkinter.Label(frame, text="Enter your Long URL ",pady=10,font="Arial 15 ")
    longurl = tkinter.Entry(frame,width=50,font="Arial 10 ")
    btn = tkinter.Button(frame,text="Convert to short url", padx=10, command=urlshortener,font="Arial 10 ")

    long_label.grid(row=0,column=1)
    longurl.grid(row=1,column=1,pady=10)
    btn.grid(row=2,column=1)

    frame.pack()
    window.mainloop()
