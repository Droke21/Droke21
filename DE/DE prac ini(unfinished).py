import tkinter as tk
from tkinter import Label, Entry, Button
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

bg_color = "#efc9af"

root = tk.Tk()
root.geometry("800x500")
root.title("Growth/Decay Project DE")
root.configure(bg=bg_color)


active_entry = None

def set_active_entry(entry):
    global active_entry
    active_entry = entry

def population_formula(P0, r, t):
    return P0 * np.exp(r * t)

def rate_of_change(P0, P, t):
    return np.log(P / P0) / t

def calculate_population():
    try:
        P0 = float(initial_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        t_values = np.linspace(0, t, 400)
        P_values = population_formula(P0, r, t_values)

        ax.clear()
        ax.plot(t_values, P_values)
        ax.set_xlabel('Time')
        ax.set_ylabel('Population')
        ax.set_title('Growth/Decay Equation Solution')
        canvas.draw()

        result_label.config(text=f"Population at time {t}: {P_values[-1]:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers for the parameters.")

def calculate_rate_of_change():
    try:
        P0 = float(initial_rate_entry.get())
        P = float(final_rate_entry.get())
        t = float(time_rate_entry.get())

        r = rate_of_change(P0, P, t)

        rate_result_label.config(text=f"Rate of change: {r:.4f}")
    except ValueError:
        rate_result_label.config(text="Please enter valid numbers for the parameters.")

notebook = ttk.Notebook(root)
notebook.pack()

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Calculate Population")

input_frame = tk.Frame(tab1, bg=bg_color)
input_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

rate_label = Label(input_frame, text="Rate (r):",font=('Verdana',16), bg=bg_color)
rate_label.pack()
rate_entry = Entry(input_frame)
rate_entry.pack()
rate_entry.bind("<FocusIn>", lambda event: set_active_entry(rate_entry))

initial_label = Label(input_frame, text="Initial Population (P0):",font=('Verdana',16), bg=bg_color)
initial_label.pack()
initial_entry = Entry(input_frame)
initial_entry.pack()
initial_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_entry))

time_label = Label(input_frame, text="Time (t):",font=('Verdana',16), bg=bg_color)
time_label.pack()
time_entry = Entry(input_frame)
time_entry.pack()
time_entry.bind("<FocusIn>", lambda event: set_active_entry(time_entry))

result_label = Label(input_frame, text="",font=('Verdana',16), bg=bg_color)
result_label.pack()

calculate_button = Button(input_frame, text="Calculate Population",font=('Verdana',16), command=calculate_population)
calculate_button.pack()

keyboard_frame = tk.Frame(input_frame, bg=bg_color)
keyboard_frame.pack()



tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Calculate Rate of Change")

input_rate_frame = tk.Frame(tab2, bg=bg_color)
input_rate_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

initial_rate_label = Label(input_rate_frame, text="Initial Population (P0):",font=('Verdana',16), bg=bg_color)
initial_rate_label.pack()
initial_rate_entry = Entry(input_rate_frame)
initial_rate_entry.pack()
initial_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_rate_entry))

final_rate_label = Label(input_rate_frame, text="Final Population (P):",font=('Verdana',16), bg=bg_color)
final_rate_label.pack()
final_rate_entry = Entry(input_rate_frame)
final_rate_entry.pack()
final_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(final_rate_entry))

time_rate_label = Label(input_rate_frame, text="Time (t):",font=('Verdana',16), bg=bg_color)
time_rate_label.pack()
time_rate_entry = Entry(input_rate_frame)
time_rate_entry.pack()
time_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(time_rate_entry))

rate_result_label = Label(input_rate_frame, text="",font=('Verdana',16), bg=bg_color)
rate_result_label.pack()

calculate_rate_button = Button(input_rate_frame, text="Calculate Rate of Change",font=('Verdana',16), command=calculate_rate_of_change)
calculate_rate_button.pack()

plt.style.use("dark_background")
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=tab1)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()
