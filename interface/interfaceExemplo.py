import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para atualizar gráfico em thread separada
def atualizar_grafico():
    global rodando
    while rodando:
        y_dados.append(random.uniform(-180, 180))  # Simula dados do encoder
        x_dados.append(len(y_dados))
        linha.set_ydata(y_dados)
        linha.set_xdata(x_dados)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()
        time.sleep(0.2)  # Atualiza a cada 200ms

# Criar janela principal
root = tk.Tk()
root.title("Interface Supervisório - Tkinter")
root.geometry("600x400")

# Criar figura Matplotlib
fig, ax = plt.subplots()
x_dados, y_dados = [], []
linha, = ax.plot(x_dados, y_dados, color='blue')
ax.set_xlabel("Tempo")
ax.set_ylabel("Ângulo (graus)")
ax.set_title("Gráfico do Encoder")

# Adicionar ao Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

# Botão para sair
rodando = True
def sair():
    global rodando
    rodando = False
    root.destroy()

ttk.Button(root, text="Sair", command=sair).pack()

# Thread para atualizar gráfico
threading.Thread(target=atualizar_grafico, daemon=True).start()

root.mainloop()
