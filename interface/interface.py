import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def funcao():
    return 0


# Criar janela principal
root = tk.Tk()
root.title("Interface Supervisório - Testes")
root.geometry("1366x768")

# Texto
label = tk.Label(root, text="Olá Mundo!")
label.pack()

# Botao
button = tk.Button(root, text="Clique aqui", command=funcao)
button.pack()
button.

# Caixa de texto
entrada = tk.Entry(root)
entrada.pack()
valor = entrada.get()  # Lê texto inserido



root.mainloop()