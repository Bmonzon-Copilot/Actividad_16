import tkinter as tk

def operaciones():
    try:
        num1 = float (entry_num1.get())
        num2 = float (entry_num2.get())



ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

label_num1 = tk.Label(ventana, text="Ingrese el primer número:")
label_num1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Ingrese el segundo número:")
label_num2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()



