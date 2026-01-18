import tkinter as tk
from datetime import date
from tkinter import messagebox

def calc_age():
    d, m, y = int(day.get()), int(month.get()), int(year.get())
    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))
    messagebox.showinfo("Age", f"You are {age} years old")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Year").grid(row=2, column=0)

day = tk.Entry(root); day.grid(row=0, column=1)
month = tk.Entry(root); month.grid(row=1, column=1)
year = tk.Entry(root); year.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calc_age).grid(row=3, column=0, columnspan=2)

root.mainloop()
