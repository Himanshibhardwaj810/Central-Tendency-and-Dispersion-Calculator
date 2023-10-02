from tkinter import *
import tkinter as tk
from tkinter import ttk
import statistics
#######
#  Project:Central-Tendency-and-Dispersion-Calculator
#  Title: Measure of Central Tendancy and Dispersion
# @author Himanshi
# 
# @version 1.1	17.09.2023 
########

# creating Main window 

root = Tk()
root.title("PROJECT-1: Measure of Central Tendency and Dispersion")
root.minsize(600, 600)
root.maxsize(1200, 988)

# Function to calculate and display the selected measure of central tendency
def calculate_central_tendency():
    numbers = number_text.get("1.0", "end-1c")  # Get the user's input from the text widget
    numbers = [float(num) for num in numbers.split(',')]  # Split input using commas and convert to a list of floats
    
    if numbers:
        selected_option = var.get()  # Get the selected radio button value
        
        if selected_option == 1:  # Arithmetic Mean
            result = statistics.mean(numbers)
            result_label.config(text=f"Arithmetic Mean: {result}")
        elif selected_option == 2:  # Harmonic Mean
            result = statistics.harmonic_mean(numbers)
            result_label.config(text=f"Harmonic Mean: {result} ")
        elif selected_option == 3:  # Geometric Mean
            result = statistics.geometric_mean(numbers)
            result_label.config(text=f"Geometric Mean: {result}")
        elif selected_option == 4:  # Mode
            result = statistics.mode(numbers)
            result_label.config(text=f"Mode: {result} ")
        elif selected_option == 5:  # Median
            result = statistics.median(numbers)
            result_label.config(text=f"Median: {result}")
        elif selected_option == 6:   #Standard Deviation
            result = statistics.stdev(numbers)
            result_label.config(text=f"Standard Deviation: {result}")
        elif selected_option == 7:  # Quartiles
            result = statistics.quantiles(numbers)
            result_label.config(text=f"Quartiles: {result} ")
        elif selected_option == 8:  # Variance
            result = statistics.variance(numbers)
            result_label.config(text=f"Variance: {result}")
       
                
    else:
        result_label.config(text="Please enter a list of numbers")

# Adding widgets to the Main window
title_label = Label(text='Title: Measure of Central Tendency and Dispersion', font=('Arial', 16))
author_label = Label(text='''Author Details: Himanshi''', font=('Arial', 12))
title_label.pack()
author_label.pack()

number_label = Label(text='Enter List of Numbers: ', font=('Arial', 10))
number_label.place(x=10, y=75)
number_text = Text(height=1, width=30)
number_text.place(x=180, y=75)

ctLabel = Label(text='Measure of Central Tendency', font=('Arial', 12))
ctLabel.place(x=10, y=150)
var = IntVar()
r1_ct = Radiobutton(text="Arithmetic Mean", variable=var, value=1)
r1_ct.place(x=10, y=200)
r2_ct = Radiobutton(text="Harmonic Mean", variable=var, value=2)
r2_ct.place(x=10, y=220)
r3_ct = Radiobutton(text="Geometric Mean", variable=var, value=3)
r3_ct.place(x=10, y=240)
r4_ct = Radiobutton(text="Mode", variable=var, value=4)
r4_ct.place(x=10, y=260)
r5_ct = Radiobutton(text="Median", variable=var, value=5)
r5_ct.place(x=10, y=280)

dispLabel = Label(text='Measure of Dispersion', font=('Arial', 12))
dispLabel.place(x=10, y=310)
r6_ct = Radiobutton(text="Standard Deviation", variable=var, value=6)
r6_ct.place(x=10, y=360)
r7_ct = Radiobutton(text="Quartiles", variable=var, value=7)
r7_ct.place(x=10, y=380)
r8_ct = Radiobutton(text="Variance", variable=var, value=8)
r8_ct.place(x=10, y=400)



# Create a "Calculate Central Tendency" button
calculate_ct_button = Button(text='Calculate Central Tendency', command=calculate_central_tendency)
calculate_ct_button.place(x=10, y=450)

# Create a label to display the result for central tendency
result_label = Label(font=('Arial', 10))
result_label.place(x=10, y=490)

quitButton = Button(text='Quit from System', command=root.destroy)
quitButton.pack(padx=5, pady=20, side=tk.BOTTOM)

root.mainloop()