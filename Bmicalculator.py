import tkinter 

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("BMI Calculator")
    window.geometry("700x400")
    window.configure(bg="black")
    
    frame = tkinter.Frame(window)
    frame.configure(bg="black")

    def bmicalculator():
        height =float(height_input.get())
        weight = float(weight_input.get())
        result =((weight / height / height) * 10000)
        res_label=tkinter.Label(frame, text="Result",bg="black",fg="white", font=("Arial",14) )
        res =tkinter.Message(frame, text = round(result,2),font=('Arial',15),bg="grey", fg="white")  
        txt=""
        fg=""

   
        if result <= 18.5:
            txt = "Under Weight"
            fg="red"
        if result >= 18 :
           txt = "Normal Weight"
           fg="green"
        if result >25:
           txt = "Over Weight"
           fg="red"
        if  result >= 30:
           txt = "Obesity"
           fg="red"
    
        note=tkinter.Message(frame, text=txt ,fg=fg, font=('Arial',15),bg="black",width=200)
        note.grid(row=6,column=1)
        res_label.grid(row=4, column=0,pady=8)
        res.grid(row=4, column=1)

    app_title = tkinter.Label(frame, text="BMI calculator",bg="black",fg="white", font=("Arial",20) )
    weight_label = tkinter.Label(frame, text="Weight in kg",bg="black",fg="white", font=("Arial",14) )
    weight_input = tkinter.Entry(frame, font=("Arial",14) )
    height_label = tkinter.Label(frame, text="Height in cm",bg="black",fg="white", font=("Arial",14) )
    height_input = tkinter.Entry(frame, font=("Arial",14) )
    submit_button = tkinter.Button(frame,text="Calculate",command=bmicalculator,font=("Arial",14))


    app_title.grid(row=0,column=1,pady=10)
    weight_label.grid(row=1, column=0)
    weight_input.grid(row=1, column=1)
    height_label.grid(row=2, column=0, pady=10)
    height_input.grid(row=2, column=1)
    submit_button.grid(row=3,column=1)

    frame.pack()
    window.mainloop()

