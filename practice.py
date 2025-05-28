import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, time_update)

root = tk.Tk()
root.title("Clock")

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

time_update()
root.mainloop()