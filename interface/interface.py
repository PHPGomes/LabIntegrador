import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Variável global do set point
set_point = 10

# Função para atualizar o set point
def atualizar_setpoint():
    global set_point
    try:
        set_point = float(entrada.get())
        label_setpoint.config(text=f"Set Point: {set_point}")
    except ValueError:
        label_setpoint.config(text="Valor inválido!")

# Criar janela principal
root = tk.Tk()
root.title("Interface Supervisório - Testes")
root.geometry("1366x768")

# Texto Set Point
label_setpoint = tk.Label(root, text=f"Set Point: {set_point}")
label_setpoint.pack()

# Caixa de texto
entrada = tk.Entry(root)
entrada.pack()

# Botão confirmar
button = tk.Button(root, text="Confirmar", command=atualizar_setpoint)
button.pack()

# Atualizar gráfico
def atualizar_grafico(x_dados, y_dados, linha, ax, canvas):
    global rodando
    while rodando:
        y_dados.append(random.uniform(-180, 180))  # Simula dado
        x_dados.append(len(y_dados))
        linha.set_ydata(y_dados)
        linha.set_xdata(x_dados)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()
        time.sleep(0.2)

#Criar primeiro gráfico
fig1, ax1 = plt.subplots(figsize=(2, 1))
fig1.tight_layout()

x_dados1, y_dados1 = [], []
linha1, = ax1.plot(x_dados1, y_dados1, color='blue')
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Ângulo (graus)")
ax1.set_title("Gráfico do Encoder Pêndulo")

canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().place(x=25, y=180, width=600, height=300)

# Criar segundo gráfico 
fig2, ax2 = plt.subplots(figsize=(2, 1))
fig2.tight_layout()

x_dados2, y_dados2 = [], []
linha2, = ax2.plot(x_dados2, y_dados2, color='green')
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Posição")
ax2.set_title("Gráfico do Encoder Posição")

canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().place(x=730, y=180, width=600, height=300)

# Botão para sair
rodando = True
def sair():
    global rodando
    rodando = False
    root.destroy()

ttk.Button(root, text="Sair", command=sair).pack()

#Threads para atualizar gráficos
threading.Thread(target=atualizar_grafico, args=(x_dados1, y_dados1, linha1, ax1, canvas1), daemon=True).start()
threading.Thread(target=atualizar_grafico, args=(x_dados2, y_dados2, linha2, ax2, canvas2), daemon=True).start()

#Iniciar interface 
root.mainloop()
