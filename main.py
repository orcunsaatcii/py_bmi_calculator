import tkinter

window = tkinter.Tk()
window.title("BMI")
window.config(bg="light blue")
window.minsize(width=200,height=200)
window.config(pady=20,padx=20)

def calculate_bmi():
    try:
        float(weight_entry.get())
        float(height_entry.get())

        height_meters = int(height_entry.get()) / 100
        weight = int(weight_entry.get())
        square_of_height = height_meters * height_meters
        bmi = weight / square_of_height
        if bmi < 18.5:
            result.config(text="Your BMI is {:.1f}\nYou are Underweight".format(bmi))
        elif bmi >= 18.5 and bmi <= 24.9:
            result.config(text="Your BMI is {:.1f}\nYou are Normal weight".format(bmi))
        elif bmi >= 25 and bmi <= 29.9:
            result.config(text="Your BMI is {:.1f}\nYou are Overweight".format(bmi))
        elif bmi >= 30 and bmi <= 34.9:
            result.config(text="Your BMI is {:.1f}\nYou are Obese Class I".format(bmi))
        elif bmi >= 35 and bmi <= 39.9:
            result.config(text="Your BMI is {:.1f}\nYou are Obese Class II".format(bmi))
        else:
            result.config(text="Your BMI is {:.1f}\nYou are Obese Class III".format(bmi))

    except ValueError:
        if height_entry.get() == "" and weight_entry.get() == "":
            result.config(text="Please enter the desired values")
        elif height_entry.get() == "":
            result.config(text="Please enter the height value")
        elif weight_entry.get() == "":
            result.config(text="Please enter the weight value")

        else:
            result.config(text="Please enter the height and weight values correctly")











weight_label = tkinter.Label(
    text="Enter your weight (kg)",
    font=("Arial",10,"bold"),
    bg="light blue"

)
weight_label.pack()

weight_entry = tkinter.Entry(width=11)
weight_entry.focus()
weight_entry.pack()

height_label = tkinter.Label(
    text="Enter your height (cm)",
    font=("Arial",10,"bold"),
    bg="light blue"

)
height_label.pack()

height_entry = tkinter.Entry(width=11)
height_entry.pack()


calculate_button = tkinter.Button(text="Calculate",width=15,command=calculate_bmi)
calculate_button.pack(pady=7)

result = tkinter.Label(
    font=("Arial",10,"bold"),
    bg="light blue"
)
result.pack()




window.mainloop()