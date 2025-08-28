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

# Definir setPoint
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


# Função para atualizar gráfico em thread separada
def atualizar_grafico2():
    global rodando
    while rodando:
        y_dados.append(random.uniform(-180, 180))  # Simula dados do encoder
        x_dados.append(len(y_dados))
        linha.set_ydata(y_dados)
        linha.set_xdata(x_dados)
        ax.relim()
        ax.autoscale_view()
        canvas2.draw()
        time.sleep(0.2)  # Atualiza a cada 200ms
        

# Função para atualizar gráfico em thread separada
def atualizar_grafico1():
    global rodando
    while rodando:
        y_dados.append(random.uniform(-180, 180))  # Simula dados do encoder
        x_dados.append(len(y_dados))
        linha.set_ydata(y_dados)
        linha.set_xdata(x_dados)
        ax.relim()
        ax.autoscale_view()
        canvas1.draw()
        time.sleep(0.2)  # Atualiza a cada 200ms

# Criar figura Matplotlib com tamanho definido
fig, ax = plt.subplots(figsize=(2, 1))
fig.tight_layout()

x_dados, y_dados = [], []
linha, = ax.plot(x_dados, y_dados, color='blue')
ax.set_xlabel("Tempo")
ax.set_ylabel("Ângulo (graus)")
ax.set_title("Gráfico do Encoder Pendulo")

# Adicionar ao Tkinter
canvas1 = FigureCanvasTkAgg(fig, master=root)
canvas1.get_tk_widget().place(x=25, y=180, width=600, height=300)



# Criar figura Matplotlib com tamanho definido
fig, ax = plt.subplots(figsize=(2, 1))
fig.tight_layout()

x_dados, y_dados = [], []
linha, = ax.plot(x_dados, y_dados, color='blue')
ax.set_xlabel("Tempo")
ax.set_ylabel("Posição")
ax.set_title("Gráfico do Encoder posição")








canvas2 = FigureCanvasTkAgg(fig, master=root)
canvas2.get_tk_widget().place(x=800, y=180, width=600, height=300)

# Botão para sair
rodando = True
def sair():
    global rodando
    rodando = False
    root.destroy()

ttk.Button(root, text="Sair", command=sair).pack()







# Thread para atualizar gráfico
threading.Thread(target=atualizar_grafico1, daemon=True).start()


root.mainloop()