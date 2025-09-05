import tkinter as tk

def operar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        resta = num1 - num2
        multi = num1 * num2
        if num2 != 0:
            div = num1 / num2
            resultado = (f"Suma: {suma}\n"
                         f"Resta: {resta}\n"
                         f"Multiplicación: {multi}\n"
                         f"División: {div}")
        else:
            resultado = (f"Suma: {suma}\n"
                         f"Resta: {resta}\n"
                         f"Multiplicación: {multi}\n"
                         f"División: Error (división por cero)")
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, ingrese números válidos.")

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

btn_operar = tk.Button(ventana, text="Calcular", command=operar)
btn_operar.pack()

label_resultado = tk.Label(ventana, text="", justify="left")
label_resultado.pack(pady=10)

ventana.mainloop()