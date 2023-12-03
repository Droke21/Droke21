import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Toplevel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pastel_blue = "#add8e6"  

root = tk.Tk()
root.geometry("600x600")  # Adjusted window size
root.title("Growth/Decay Project DE")
root.configure(bg=pastel_blue)

style = ttk.Style()
style.configure('My.TFrame', background=pastel_blue)

active_entry = None

def set_active_entry(entry):
    global active_entry
    active_entry = entry

def population_formula(P0, r, t):
    return P0 * np.exp(r * t)

def calculate_population():
    try:
        P0 = float(initial_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        t_values = np.linspace(0, t, 400)
        P_values = population_formula(P0, r, t_values)

        result_label.config(text=f"Population at time {t}: {P_values[-1]:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers for the parameters.")

def open_graph():
    try:
        P0 = float(initial_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        t_values = np.linspace(0, t, 400)
        P_values = population_formula(P0, r, t_values)

        graph_window = Toplevel(root)
        graph_window.title("Graph and Answer")

        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.plot(t_values, P_values)
        ax.set_xlabel('Time')
        ax.set_ylabel('Population')
        ax.set_title('Growth/Decay Equation Solution')

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        result_label = Label(graph_window, text=f"Population at time {t}: {P_values[-1]:.2f}", font=('Verdana', 16), bg=pastel_blue)
        result_label.pack()

        canvas.draw()

    except ValueError:
        result_label.config(text="Please enter valid numbers for the parameters.")

def calculate_rate_of_change():
    try:
        P0 = float(initial_rate_entry.get())
        P = float(final_rate_entry.get())
        t = float(time_rate_entry.get())

        r = np.log(P / P0) / t

        rate_result_label.config(text=f"Rate of change: {r:.4f}")

        # Display rate of change answer
        rate_window = Toplevel(root)
        rate_window.title("Rate of Change")
        
        rate_label = Label(rate_window, text=f"Rate of change: {r:.4f}m/s²", font=('Verdana', 16), bg=pastel_blue)
        rate_label.pack()

    except ValueError:
        rate_result_label.config(text="Please enter valid numbers for the parameters.")

def reset_values():
    # Reset button
    initial_entry.delete(0, tk.END)
    initial_entry.insert(0, "0")

    rate_entry.delete(0, tk.END)
    rate_entry.insert(0, "0")

    time_entry.delete(0, tk.END)
    time_entry.insert(0, "0")

    initial_rate_entry.delete(0, tk.END)
    initial_rate_entry.insert(0, "0")

    final_rate_entry.delete(0, tk.END)
    final_rate_entry.insert(0, "0")

    time_rate_entry.delete(0, tk.END)
    time_rate_entry.insert(0, "0")

    # Reset result tanan
    result_label.config(text="")
    rate_result_label.config(text="")


frame = ttk.Frame(root, style='My.TFrame')
frame.pack(pady=20)

# Calculate Population 
rate_label = Label(frame, text="Rate (r):", font=('Verdana', 16), bg=pastel_blue)
rate_label.grid(row=0, column=0, pady=5)
rate_entry = Entry(frame, font=('Verdana', 16))
rate_entry.grid(row=0, column=1, pady=5)
rate_entry.bind("<FocusIn>", lambda event: set_active_entry(rate_entry))

initial_label = Label(frame, text="Initial Population (P0):", font=('Verdana', 16), bg=pastel_blue)
initial_label.grid(row=1, column=0, pady=5)
initial_entry = Entry(frame, font=('Verdana', 16))
initial_entry.grid(row=1, column=1, pady=5)
initial_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_entry))

time_label = Label(frame, text="Time (t):", font=('Verdana', 16), bg=pastel_blue)
time_label.grid(row=2, column=0, pady=5)
time_entry = Entry(frame, font=('Verdana', 16))
time_entry.grid(row=2, column=1, pady=5)
time_entry.bind("<FocusIn>", lambda event: set_active_entry(time_entry))

result_label = Label(frame, text="", font=('Verdana', 16), bg=pastel_blue)
result_label.grid(row=3, columnspan=2, pady=10)

open_graph_button = Button(frame, text="Open Graph and Calculate", font=('Verdana', 16), command=open_graph)
open_graph_button.grid(row=4, columnspan=2, pady=10)

keyboard_frame = tk.Frame(frame, bg=pastel_blue)
keyboard_frame.grid(row=5, columnspan=2)

reset_button = Button(frame, text="Reset", font=('Verdana', 16), command=reset_values)
reset_button.grid(row=6, columnspan=2, pady=10)

# Rate of Change 
initial_rate_label = Label(frame, text="Initial Population (P0):", font=('Verdana', 16), bg=pastel_blue)
initial_rate_label.grid(row=7, column=0, pady=5)
initial_rate_entry = Entry(frame, font=('Verdana', 16))
initial_rate_entry.grid(row=7, column=1, pady=5)
initial_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_rate_entry))

final_rate_label = Label(frame, text="Final Population (P):", font=('Verdana', 16), bg=pastel_blue)
final_rate_label.grid(row=8, column=0, pady=5)
final_rate_entry = Entry(frame, font=('Verdana', 16))
final_rate_entry.grid(row=8, column=1, pady=5)
final_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(final_rate_entry))

time_rate_label = Label(frame, text="Time (t):", font=('Verdana', 16), bg=pastel_blue)
time_rate_label.grid(row=9, column=0, pady=5)
time_rate_entry = Entry(frame, font=('Verdana', 16))
time_rate_entry.grid(row=9, column=1, pady=5)
time_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(time_rate_entry))

rate_result_label = Label(frame, text="", font=('Verdana', 20), bg=pastel_blue)

calculate_rate_button = Button(frame, text="Calculate Rate of Change", font=('Verdana', 16), command=calculate_rate_of_change)
calculate_rate_button.grid(row=11, columnspan=2, pady=10)

root.mainloop()
