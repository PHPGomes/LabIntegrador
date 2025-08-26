import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

set = 10

def funcao():
    return 0


# Criar janela principal
root = tk.Tk()
root.title("Interface Supervisório - Testes")
root.geometry("1366x768")

# Texto
label = tk.Label(root, text=("Set Point: "+ str(set)))
label.pack()

# Texto
label = tk.Label(root, text="")
label.pack()

# Caixa de texto
entrada = tk.Entry(root)
entrada.pack()
valor = entrada.get()  # Lê texto inserido

# Texto
label = tk.Label(root, text="")
label.pack()

# Botao
button = tk.Button(root, text="Confirmar", command=funcao)
button.pack()





root.mainloop()