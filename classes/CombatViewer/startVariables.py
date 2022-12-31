import tkinter as tk
from tkinter import Toplevel, Label
from win32api import GetSystemMetrics
from PIL import ImageTk

lastClickX = 0
lastClickY = 0
buttonWidth =  str(int(float(GetSystemMetrics(0)) / 9 / 20 ))
buttonHeight = "100"
activeColor="#808be0"
buttomForeground = ('#c0c7ff')
buttomBackgorund = ('#04080d')
customFont = ("Aerial 20") 
EspecialFont = ("Aerial 20 underline")
paisvermelho = False
selectedDraw = False
defaultSide = tk.LEFT


from classes.CombatViewer.settingsLoader import *
#Cria as janelas tk.Tk()
window = tk.Tk()
#Cria uma outra janela a partir da window, isso significa que são "filhas"
imageLayer = Toplevel(window)
menus = Toplevel(window)
root = Toplevel(window)
#Define que a janela é praticamente transparente apenas pra receber os cliques
root.attributes('-alpha', 0.01)
root.attributes('-topmost', True)

#Define tamanho e posição da janela para obter os cliques:
root.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),GetSystemMetrics(1),secondMonitor,0))
imageLayer.attributes('-alpha', 0.5)
imageLayer.configure(background='black')    

#bg o diretório de onde será carregado a imagem topográfica
bg = ImageTk.PhotoImage(file="./kalunguinhas/background/imagem.jpg")
#bg canvas é o canvas com a imagem topográfica
bgCanvas = tk.Canvas(imageLayer, bg='black')
bgCanvas.pack(fill=tk.BOTH, expand=True)
bgCanvas.create_image(0, 0, image=bg, anchor='nw')

transparent_color = 'grey15'
#Can2 sera o canvas com a imagem dos mapa
can2 = tk.Canvas(root, bg='black', height=400, width=300,highlightthickness=0)
can2.pack(side=tk.RIGHT,fill="both", expand=True)
#Can sera o canvas com a janela transparente para captar movimentos dos kalunguinhas
can = tk.Canvas(window, bg=transparent_color, height=400, width=300,highlightthickness=0)
can.pack(side=tk.RIGHT,fill="both", expand=True)
