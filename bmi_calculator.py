from tkinter import *

window = Tk()


def set_window():
    global window
    window.title("BMI Calculator")
    window.minsize(width=350, height=275)
    window.config(bg="light gray")


def set_widgets():

    def calculate_bmi():

        weight = (weight_entry.get())
        height = (height_entry.get())

        try:
            bmi = (float(weight) / (float(height) / 100) ** 2)
            error_label.pack_forget()

            if bmi < 16.0:
                result_label.config(text=f"You are in a severely underweight condition. \nBMI: {int(bmi)}")

            elif 16.0 < bmi < 16.9:
                result_label.config(text=f"You are in a moderately underweight condition. \nBMI: {int(bmi)}")

            elif 17.0 < bmi < 18.4:
                result_label.config(text=f"You are in a mildly underweight condition. \nBMI: {int(bmi)}")

            elif 18.5 < bmi < 24.9:
                result_label.config(text=f"You are in the normal weight range. \nBMI: {int(bmi)}")

            elif 25 < bmi < 29.9:
                result_label.config(text=f" You are in the overweight range. \nBMI: {int(bmi)}")

            elif 30 < bmi < 34.9:
                result_label.config(text=f"You are in the Class I obesity category (mild obesity). \nBMI: {int(bmi)}")

            elif 35 < bmi < 39.9:
                result_label.config(
                    text=f"You are in the Class II obesity category (moderate obesity).\nBMI: {int(bmi)}")

            elif bmi > 40:
                result_label.config(
                    text=f"You are in the Class III obesity category (severe obesity).\nBMI: {int(bmi)}")

            result_label.pack()

        except ValueError:
            result_label.pack_forget()

            if height == "" and weight == "":
                error_label.config(text="Please enter numeric values for weight and height")

            elif height != "" or weight != "":
                error_label.config(text="Please enter valid weight and height")

            error_label.pack()

    weight_label = Label(text="Enter your weight (kg): ", bg="light gray", fg="black")
    weight_label.pack(padx=10, pady=10)

    weight_entry = Entry(width=10)
    weight_entry.pack(padx=10, pady=10)
    weight_entry.focus()

    height_label = Label(text="Enter your height (cm): ", bg="light gray", fg="black")
    height_label.pack(padx=10, pady=10)

    height_entry = Entry(width=10)
    height_entry.pack(padx=10, pady=10)

    calculate_button = Button(text="Calculate", bg="light gray", fg="black", command=calculate_bmi)
    calculate_button.pack(padx=10, pady=10)

    result_label = Label(bg="light gray", fg="navy")

    error_label = Label(bg="light gray", fg="dark red")


set_window()

set_widgets()

window.mainloop()
