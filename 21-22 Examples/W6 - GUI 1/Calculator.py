import tkinter as tk
from tkinter import ttk


def addition():
    print(f"{numberA.get() + numberB.get()}")


root = tk.Tk()
root.geometry("500x200")

numberA = tk.IntVar()
numberB = tk.IntVar()

lbl_numA = ttk.Label(root, text="Num: ")
lbl_numA.pack(side="left", padx=(0, 15))

ent_numA = ttk.Entry(root, width=20, textvariable=numberA)
ent_numA.pack(side="left")

lbl_numB = ttk.Label(root, text="Num: ")
lbl_numB.pack(side="left", padx=(0, 15))

ent_numB = ttk.Entry(root, width=20, textvariable=numberB)
ent_numB.pack(side="left")

btn_addition = ttk.Button(root, text="+", command=addition)
btn_addition.pack(side="left")

root.mainloop()