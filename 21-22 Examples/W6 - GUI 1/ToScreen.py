import tkinter as tk
from tkinter import ttk


def addition():
    x = num_one.get()
    y = num_two.get()
    ans = x + y
    lbl_answer.config(text=str(ans))


root = tk.Tk()

num_one = tk.DoubleVar()
num_two = tk.DoubleVar()

ent_num_one = ttk.Entry(root, textvariable=num_one).pack()
ent_num_two = ttk.Entry(root, textvariable=num_two).pack()

lbl_answer = ttk.Label(root, text="0", padding=(10,10))
lbl_answer.pack()

btn_get_answer = ttk.Button(root, text="Add", command=addition).pack()

root.mainloop()