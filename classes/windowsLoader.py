#importação dos menus com as funções junto com as bibliotecas
from classes.menusFunction import *

from win32 import win32api
#binds do canvas
window.bind('<Escape>', close)
root.bind('<Escape>', close)
imageLayer.bind('<Escape>', close)
menus.bind('<Escape>', close)

#função para desativar o redirecionamento de tela
def toggleWindows():
    # create the class instance
    menus.overrideredirect(False)

#bind para ativar a função acima
window.bind('<KeyPress-shift>', toggleWindows())

#binds para arrastar a tela
root.bind('<Button-1>', capture)
root.bind('<ButtonRelease-1>', release)
root.bind('<B1-Motion>', drag)
imageLayer.bind('<Button-1>', capture)
imageLayer.bind('<ButtonRelease-1>', release)
imageLayer.bind('<B1-Motion>', drag)
window.bind('<Button-1>', capture)
window.bind('<ButtonRelease-1>', release)
window.bind('<B1-Motion>', drag)

#lista para guardar as linhas
lines = []

#variavel para guardar a ultima medida
lastmetter = 0

#configurações da janela de menus
menus.resizable(True, True)
menus.configure(bg="black")

#posição da janela de menus
menus.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),str(int(float(buttonHeight) *1.0)),0 + secondMonitor,str(int(float(GetSystemMetrics(1))) - int(float(buttonHeight) *1.0))))

#configurações da janela principal
root.attributes('-transparentcolor', transparent_color)

#posição da janela principal
imageLayer.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),str(int(float(GetSystemMetrics(1)) - float(buttonHeight))), secondMonitor,0))

#configurações da janela principal
imageLayer.attributes('-transparentcolor', transparent_color)

#configurações da janela de menus
window.attributes('-transparentcolor', transparent_color)

#configurações da janela de menus
window.attributes('-topmost', True)

#configurações da janela de menus
menus.attributes('-topmost', True)

#configurações da janela principal
root.attributes('-topmost', False)

#configurações da janela principal
root.configure(bg="black")

#criação do botão para redimensionar a tela
side = Label(bgCanvas, text=' - ', background="gray")

#bind para redimensionar a tela
side.bind("<B1-Motion>", resize)

#posição do botão
side.place(relx=1, y=0, anchor=tk.NE)

#configurações da janela principal
imageLayer.overrideredirect(True)

#configurações da janela de menus
menus.overrideredirect(True)

#configurações da janela de menus
window.overrideredirect( True)
wth,hgh = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0) ,GetSystemMetrics(1),secondMonitor,0))
menus.bind("<space>", move_window)