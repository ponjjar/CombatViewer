import tkinter as tk

from tkinter import Toplevel, Label
from win32api import GetSystemMetrics

from PIL import Image,ImageTk
#import win32gui
#import win32con
secondMonitor=1920
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

#Salva ultima posição do mouse
'''
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
'''
#move a janela
'''def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))
'''

window = tk.Tk()
def setColor(color):
    global line_options
    line_options = {
            'width': 10,
            'fill': color,
             }
imageLayer = Toplevel(window)
menus = Toplevel(window)
root = Toplevel(window)
root.attributes('-alpha', 0.01)
root.attributes('-topmost', True)

root.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),GetSystemMetrics(1),secondMonitor,0))
imageLayer.attributes('-alpha', 0.5)
imageLayer.configure(background='black')    

bg = ImageTk.PhotoImage(file="./kalunguinhas/background/imagem.jpg")
bgCanvas = tk.Canvas(imageLayer, bg='black')
bgCanvas.pack(fill=tk.BOTH, expand=True)
bgCanvas.create_image(0, 0, image=bg, anchor='nw')
# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("./kalunguinhas/background/imagem.jpg")
   # resize the image with width and height of root
   resized = image.resize((int(e.width), int(e.width * image.height / image.width)), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   bgCanvas.create_image(0, 0, image=image2, anchor='nw')
bgCanvas.bind("<Configure>", resize_image)
def drag2(event):   
    event.widget.place(x=event.x_root, y=str(int(event.y_root)-int(buttonHeight)),anchor=tk.NW)

# Desenhar formas no canvas
def click(event):
    if object_id is not None:
        coord = can.coords(object_id)
        print(str(coord))
        width = customWidth
        height = customHeight

        can.coords(object_id, event.x, event.y)


def delete():
       can.delete(captured)

def shiftdelete():
    can.delete(tk.ALL)
customHeight = 75
customWidth = 120  
#carregando imagens

cias= [
    #color red
 ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec.png").resize((int(float(customWidth )* 1.2),int(float(customHeight )* 1.2)), Image.ANTIALIAS)),
ImageTk.PhotoImage((Image.open("./kalunguinhas/28bimec/cias/1.png")).resize((customWidth, customHeight), Image.ANTIALIAS)),
 ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/2.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/3.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap.png").resize((customWidth,customHeight), Image.ANTIALIAS)),

ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/1pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/2pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/3pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/4pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),


ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/1pel/1gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/1pel/2gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/1/1pel/3gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/com.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/exp.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/mort.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/pmt.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/saude.png").resize((customWidth,customHeight), Image.ANTIALIAS))]

ciasVermelho= [
    #color red
 ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec.png").resize((int(float(customWidth )* 1.2),int(float(customHeight )* 1.2)), Image.ANTIALIAS)),
ImageTk.PhotoImage((Image.open("./kalunguinhas-vermelho/28bimec/cias/1.png")).resize((customWidth, customHeight), Image.ANTIALIAS)),
 ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/2.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/3.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/ccap.png").resize((customWidth,customHeight), Image.ANTIALIAS)),

ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/1pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/2pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/3pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/4pel.png").resize((customWidth,customHeight), Image.ANTIALIAS)),


ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/1pel/1gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/1pel/2gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/1/1pel/3gc.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/ccap/com.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/ccap/exp.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/ccap/mort.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas/28bimec/cias/ccap/pmt.png").resize((customWidth,customHeight), Image.ANTIALIAS)),
ImageTk.PhotoImage(Image.open("./kalunguinhas-vermelho/28bimec/cias/ccap/saude.png").resize((customWidth,customHeight), Image.ANTIALIAS))]


global object_id
def create28bimec():
        global object_id
        global paisvermelho
        if paisvermelho == False:
            object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[0], anchor=tk.NW)
        #color red
        else:
            object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[0], anchor=tk.NW)
        print(str(object_id))
def create_1cia():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[1], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[1], anchor=tk.NW)

def create_2cia():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[2], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[2], anchor=tk.NW)
def create_3cia():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[3], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[3], anchor=tk.NW)
def create_ccap():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[4], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[4], anchor=tk.NW)


def create_1pelotao():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[5], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[5], anchor=tk.NW)
    
def create_2pelotao():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[6], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[6], anchor=tk.NW)
    
def create_3pelotao():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[7], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[7], anchor=tk.NW)
    
def create_4pelotao():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[8], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[8], anchor=tk.NW)
def create_1gc():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[9], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[9], anchor=tk.NW)
    
def create_2gc():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[10], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[10], anchor=tk.NW)
    
def create_3gc():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[11], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[11], anchor=tk.NW)

def bimecMenu():
    destroyFirstMenu
    createCiasMenu()

def create_pelcom():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[12], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[12], anchor=tk.NW)
def create_pelmort():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[14], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[14], anchor=tk.NW)
def create_pelexp():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[13], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[13], anchor=tk.NW)
def create_pmt():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[15], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[15], anchor=tk.NW)

def create_saude():
    global object_id
    global paisvermelho
    if paisvermelho == False:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=cias[16], anchor=tk.NW)
    #color red
    else:
        object_id = can.create_image(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 3),image=ciasVermelho[16], anchor=tk.NW)
# --- main ---

def create_line():
    global object_id

    object_id = can.create_line(200, 200, 100, 100, fill='red', width=5)

def create_circle():
    global object_id

    object_id = can.create_oval(10, 10, 70, 70, fill='orange', outline='blue')

object_id = None

transparent_color = 'grey15'
'''
def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)
        '''
can2 = tk.Canvas(root, bg='black', height=400, width=300,highlightthickness=0)

can = tk.Canvas(window, bg=transparent_color, height=400, width=300,highlightthickness=0)

def fail_click(evt):
    print(evt.x)
can.bind('<Button-1>', fail_click)
def capture(event):
    global captured
    global object_id
  #  event.y = int(event.y) + int(buttonHeight)
    if selectedDraw == False:
        if object_id is not None:
            
                captured = object_id
                x0, y0, x1, y1 = can.bbox(captured)
                xt, yt = event.x + (x0 - x1 ) // 2, event.y + (y0 - y1) // 2      # 1st square movement coords
                can.coords(captured, xt, yt)
        else:
            print('captured')
            
            captured = can.find_closest(event.x, event.y)
    else:
        set_first(event)
    


def release(event):
    global object_id
    object_id = None
    clear_list(event)
    print('released')

captured = None

def drag(event):   # drag by holding mouse button 1
    
    global object_id
    global captured
    event.y = int(event.y)
    if selectedDraw == False:
        if captured is None:
                print(f'captured {can.find_closest(event.x, event.y)}')
                captured = can.find_closest(event.x, event.y)
                print(f'captured: {captured}')
                
                x0, y0, x1, y1 = can.bbox(captured)
                xt, yt = event.x + (x0 - x1 ) // 2, event.y + (y0 - y1) // 2      # 1st square movement coords
                can.coords(captured, xt, yt)
                
        else:
                x0, y0, x1, y1 = can.bbox(captured)
                xt, yt = event.x + (x0 - x1 ) // 2, event.y + (y0 - y1) // 2      # 1st square movement coords
                can.coords(captured, xt, yt)
    else:
        append_and_draw(event)
#window.wm_attributes("-alpha", 0.5)
can.pack(side=tk.RIGHT,fill="both", expand=True)

can2.pack(side=tk.RIGHT,fill="both", expand=True)

def close(e):
 window.destroy()
window.bind('<Escape>', close)

root.bind('<Escape>', close)
imageLayer.bind('<Escape>', close)
menus.bind('<Escape>', close)

def toggleWindows():
    # create the class instance
    menus.overrideredirect(False)
   # window.attributes('-transparentcolor', 'green', '-topmost', 1)
window.bind('<KeyPress-shift>', toggleWindows())
'''
can.bind('<Button-1>', capture)

can.bind('<ButtonRelease-1>', release)
can.bind('<B1-Motion>', drag) '''
root.bind('<Button-1>', capture)
root.bind('<ButtonRelease-1>', release)
root.bind('<B1-Motion>', drag)


imageLayer.bind('<Button-1>', capture)
imageLayer.bind('<ButtonRelease-1>', release)
imageLayer.bind('<B1-Motion>', drag)

window.bind('<Button-1>', capture)
window.bind('<ButtonRelease-1>', release)
window.bind('<B1-Motion>', drag)

'''
btn_line = tk.Button(window, text='Line', width=buttonWidth, height=buttonHeight,command=create_line)
btn_line.pack()
'''
'''
btn_circle = tk.Button(window, text='Circle', width=buttonWidth, command=create_circle)
btn_circle.pack()
'''

btn_delete = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Apagar \nSelecionado', font= customFont, width=buttonWidth, height=buttonHeight, command=delete)
btn_apagartudo = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Apagar \nTudo', font= customFont, width=buttonWidth, height=buttonHeight, command=shiftdelete)

btn_delete.grid(row=0, column=1, padx=10, pady=10)

btn_delete.pack(side=tk.RIGHT,fill="both")
btn_apagartudo.pack(side=tk.RIGHT,fill="both")
btn_28bimec = tk.Button()
btn_paisvermelho = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Apagar \nSelecionado', font= customFont, width=buttonWidth, height=buttonHeight, command=delete)
btn_patrulha = tk.Button()

btn_1cia = tk.Button()
btn_2cia = tk.Button()
btn_3cia = tk.Button()

def setSelectedDraw(Verificador):
    global selectedDraw
    if(Verificador == True):
        selectedDraw = True
    elif(Verificador == False):
        selectedDraw = False
    else:
        selectedDraw = not selectedDraw
def transformRed():
    global paisvermelho
    paisvermelho=True
def transformBlue():
    global paisvermelho
    paisvermelho=False
def createFirstMenu():
    btn_28bimec = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground,text='28bimec',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [createCiasMenu(), btn_itirenarios.destroy(), btn_28bimec.destroy(), btn_paisvermelho.destroy(),btn_patrulha.destroy()])
    btn_28bimec.pack(side=defaultSide,expand=tk.YES, fill="both")
    
    btn_itirenarios = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground,  text='Itirenarios',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [createItirenariosMenu(), btn_itirenarios.destroy(), btn_28bimec.destroy(), btn_paisvermelho.destroy(),btn_patrulha.destroy()])
    btn_itirenarios.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_paisvermelho = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground,text='Pais vermelho',   font= customFont, width=buttonWidth, height=buttonHeight,  command=lambda: [transformRed(),createCiasMenu(), btn_itirenarios.destroy(), btn_28bimec.destroy(), btn_paisvermelho.destroy(),btn_patrulha.destroy()])
    btn_paisvermelho.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_patrulha = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Patrulha',   font= customFont, width=buttonWidth, height=buttonHeight,)
    btn_patrulha.pack(side=defaultSide,expand=tk.YES,fill="both")


def createItirenariosMenu():
    
    #btn_drawitirenarios = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Criar Itinerário',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True)])
    #btn_drawitirenarios.pack()
    
    btn_corvermelha = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg="#c45e6a", text='Vermelho',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True), setColor("red")])
    btn_corvermelha.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_corazul = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg="#5e61c4", text='Azul',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True), setColor("blue")])
    btn_corazul.pack(side=defaultSide,expand=tk.YES,fill="both")

    btn_corverde = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg="green", text='Verde',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True), setColor("green")])
    btn_corverde.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_coramarela = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg="#c4b65e", text='Amarelo',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True), setColor("yellow")])
    btn_coramarela.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_corpreta = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg="lightgray", text='Preto',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(True), setColor("black")])
    btn_corpreta.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_undoItirenarios = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Desfazer',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [undo_listDraw()])
    btn_undoItirenarios.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_limpar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Limpar',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [deleteAllDraw()])
    btn_limpar.pack(side=tk.RIGHT,expand=tk.YES,fill="both")
    btn_voltar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Voltar', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda: [setSelectedDraw(False),createFirstMenu(), btn_coramarela.destroy(),btn_corvermelha.destroy(),btn_corverde.destroy(),btn_corpreta.destroy(),btn_corazul.destroy(), btn_limpar.destroy(),btn_undoItirenarios.destroy(),btn_voltar.destroy()])
    btn_voltar.pack(side=tk.BOTTOM, expand=tk.YES,fill="both")
    

   

createFirstMenu()
def destroyFirstMenu():

    btn_28bimec.destroy
    btn_paisvermelho.destroy()
    btn_patrulha.destroy()

def createCiasMenu():
    
    btn_28bimec = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='28bimec', font= customFont,  width=buttonWidth, height=buttonHeight, command=create28bimec)
    btn_1cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='1° Cia',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [createPelMenu(1),  btn_28bimec.destroy(),btn_ccap.destroy(),btn_1cia.destroy(), btn_2cia.destroy(),btn_3cia.destroy(), btn_voltar.destroy()])
    btn_2cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='2° Cia',  font= customFont, width=buttonWidth, height=buttonHeight, command=lambda: [createPelMenu(2),  btn_28bimec.destroy(),btn_ccap.destroy(),btn_1cia.destroy(), btn_2cia.destroy(),btn_3cia.destroy(), btn_voltar.destroy()])
    btn_3cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='3° Cia', font= customFont,  width=buttonWidth,height=buttonHeight, command=lambda: [createPelMenu(3),  btn_28bimec.destroy(),btn_ccap.destroy(),btn_1cia.destroy(), btn_2cia.destroy(),btn_3cia.destroy(), btn_voltar.destroy()])
    btn_ccap = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='CCAP', font= customFont,  width=buttonWidth,height=buttonHeight, command=lambda: [createCAPmenu(),btn_28bimec.destroy(),btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy(),btn_ccap.destroy(),btn_voltar.destroy()])
    btn_voltar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Voltar', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda: [ transformBlue(),createFirstMenu(), btn_28bimec.destroy(), btn_ccap.destroy(),btn_1cia.destroy(), btn_2cia.destroy(),btn_3cia.destroy(), btn_voltar.destroy()])
    
    btn_28bimec.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_1cia.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_2cia.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_3cia.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_ccap.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_voltar.pack(side=tk.RIGHT,expand=tk.YES,fill="both")
    

line = None  # this is a reference to the current line (id)
points = []  # list to keep track of current line coordinates
line_options = {}
def set_first(event):
    points.extend([event.x, event.y])
    global line_options

lines = []

lastmetter = 0

def append_and_draw(event):
    global lastmetter
    global line
    global line_options
# dictionary to allow easier change of line options
    points.extend([event.x, event.y])
    print ((line))
    if len(points) - lastmetter > 100:
        lastmetter = len(points)
       # label_disance = Label(can, text=str(lastmetter) + "m", font= ('Aerial 10'))
       # label_disance.place(x = event.x,y = event.y)
       # lines.append(label_disance)
    if len(points) == 4:
  
        lastmetter=0
        line = can.create_line(points, **line_options)
        lines.append(line)
    else:
        can.coords(line, points)

def undo_listDraw(event=None):
    global lines
    print (lines)
    try :
        can.delete(lines[len(lines) - 1])
    except:
        lines[len(lines) - 1].destroy()
    lines.pop()

def deleteAllDraw(event=None):
    global lines
    print (lines)
    for i in range(len(lines)):
        try :
            can.delete(lines[len(lines) - 1])
        except:
            lines[len(lines) - 1].destroy()
        lines.pop()
def clear_list(event=None):
    global line
    points.clear()
    line = None
def createCAPmenu():
    
    btn_ccap = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='CCAP', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_ccap)
    btn_pelcom = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pel Com', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda: [create_pelcom()])
    btn_pelrec = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pel Rec', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda: [create_pelexp()])
    btn_pelmort = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pel Mort', font= customFont,  width=buttonWidth,height=buttonHeight, command=lambda: [create_pelmort()])
    btn_pelsau = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pel Sau', font= customFont,  width=buttonWidth,height=buttonHeight, command=lambda: [create_saude()])
    btn_pmt = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='PMT', font= customFont, width=buttonWidth,height=buttonHeight, command=lambda: [create_pmt()])
    btn_voltar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Voltar', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda: [createCiasMenu(), btn_28bimec.destroy(), btn_ccap.destroy(),btn_pmt.destroy(),btn_pelcom.destroy(),btn_pelsau.destroy(), btn_pelrec.destroy(),btn_pelmort.destroy(), btn_voltar.destroy()])
    
    btn_ccap.pack(side=defaultSide,expand=tk.YES,fill="both")   
    btn_pelcom.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_pelrec.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_pelmort.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_pelsau.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_pmt.pack(side=defaultSide,expand=tk.YES,fill="both") 
    btn_voltar.pack(side=tk.RIGHT,expand=tk.YES,fill="both")
def createPelMenu(posicao):

    btn_1cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='1° Cia', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_1cia)
    btn_2cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='2° Cia', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_2cia)
    btn_3cia = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='3° Cia', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_3cia)
    if(posicao == 1):
        btn_1cia.pack(side=defaultSide,expand=tk.YES,fill="both")
    elif(posicao == 2):
        btn_2cia.pack(side=defaultSide,expand=tk.YES,fill="both")
    elif(posicao == 3):
        btn_3cia.pack(side=defaultSide,expand=tk.YES,fill="both")

    btn_1pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='1° Pelotão', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda:[createGC(posicao, 1),btn_voltar.destroy(),btn_1pelotao.destroy(),btn_2pelotao.destroy(),btn_3pelotao.destroy(),btn_4pelotao.destroy(),btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy()])
    btn_2pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='2° Pelotão', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda:[createGC(posicao, 2),btn_voltar.destroy(),btn_1pelotao.destroy(),btn_2pelotao.destroy(),btn_3pelotao.destroy(),btn_4pelotao.destroy(),btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy()])
    btn_3pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='3° Pelotão', font= customFont, width=buttonWidth, height=buttonHeight, command=lambda:[createGC(posicao, 3),btn_voltar.destroy(),btn_1pelotao.destroy(),btn_2pelotao.destroy(),btn_3pelotao.destroy(),btn_4pelotao.destroy(),btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy()])
    btn_4pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pelotão de apoio', font= customFont,  width=buttonWidth, height=buttonHeight, command=lambda:[createGC(posicao, 4),btn_voltar.destroy(),btn_1pelotao.destroy(),btn_2pelotao.destroy(),btn_3pelotao.destroy(),btn_4pelotao.destroy(),btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy()])
    btn_1pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_2pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_3pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_4pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_voltar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Voltar',font= customFont, width=buttonWidth, height=buttonHeight, command=lambda:[createCiasMenu(), btn_voltar.destroy(),btn_1pelotao.destroy(), btn_2pelotao.destroy(),btn_3pelotao.destroy(), btn_4pelotao.destroy(), btn_1cia.destroy(),btn_2cia.destroy(),btn_3cia.destroy(), btn_voltar.destroy()])
    btn_voltar.pack(side=tk.RIGHT,expand=tk.YES)
def createGC(posicao, pel):
    btn_1pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='1° Pelotão', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_1pelotao)
    btn_3pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='3° Pelotão', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_3pelotao)
    btn_2pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='2° Pelotão', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_2pelotao)
    btn_4pelotao = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Pelotão de apoio', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_4pelotao)
    if(pel == 1):
        btn_1pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    elif(pel == 2):
        btn_2pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    elif(pel == 3):
        btn_3pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    elif(pel == 4):
        btn_4pelotao.pack(side=defaultSide,expand=tk.YES,fill="both")
    
    btn_1gc = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='1° GC', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_1gc)
    btn_2gc = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='2° GC', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_2gc)
    btn_3gc = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='3° GC', font= customFont,  width=buttonWidth, height=buttonHeight, command=create_3gc)
    btn_1gc.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_2gc.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_3gc.pack(side=defaultSide,expand=tk.YES,fill="both")
    btn_voltar = tk.Button(menus,bg=buttomBackgorund,activebackground = activeColor, relief=tk.SOLID,fg=buttomForeground, text='Voltar', width=buttonWidth, font= customFont,  height=buttonHeight, command=lambda: [createPelMenu(posicao),btn_1pelotao.destroy(),btn_2pelotao.destroy(),btn_3pelotao.destroy(),btn_4pelotao.destroy(), btn_1gc.destroy(),btn_2gc.destroy(), btn_3gc.destroy(), btn_voltar.destroy()])
    btn_voltar.pack(side=tk.RIGHT,expand=tk.YES,fill="both")
def destroyCiasMenu(btn_1cia,btn_2cia,btn_3cia):

    btn_1cia.destroy()
    btn_2cia.destroy()
    btn_3cia.destroy()

#window.overrideredirect(True)
menus.resizable(True, True)
menus.configure(bg="black")
#menus.geometry("400x400+500+300")
#menus.geometry('{}x{}+{}+{}'.format(menus.winfo_width(), menus.winfo_height(), 10, 10))

menus.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),str(int(float(buttonHeight) *1.0)),0 + secondMonitor,str(int(float(GetSystemMetrics(1))) - int(float(buttonHeight) *1.0))))
root.attributes('-transparentcolor', transparent_color)
def resize(event):
        global rect
        global x, y, ht
        x = imageLayer.winfo_pointerx() - imageLayer.winfo_rootx()
        y = imageLayer.winfo_pointery() - imageLayer.winfo_rooty()
        if x > 0:
                fx = imageLayer.winfo_rootx()
                fy = imageLayer.winfo_rooty() + y
                ht = imageLayer.winfo_height() - y
                if ht > 0:
                        imageLayer.geometry(f"{x}x{ht}+{fx}+{fy}")

imageLayer.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0),str(int(float(GetSystemMetrics(1)) - float(buttonHeight))), secondMonitor,0))
imageLayer.attributes('-transparentcolor', transparent_color)
window.attributes('-transparentcolor', transparent_color)


window.attributes('-topmost', True)
menus.attributes('-topmost', True)
root.attributes('-topmost', False)
root.configure(bg="black")
side = Label(bgCanvas, text=' - ', background="gray")
side.bind("<B1-Motion>", resize)
def move_imagelayer(event):
    imageLayer.geometry(f'+{event.x_root}'+f'+{event.y_root}')
imageLayer.bind("<i>", move_imagelayer)
#imageLayer.winfo_rootx()
           #     fy = imageLayer.winfo_rooty()
           
#imageLayer.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(1)- 50,GetSystemMetrics(1) - 100,700,50))
side.place(relx=1, y=0, anchor=tk.NE)
imageLayer.overrideredirect(True)
menus.overrideredirect(True)
window.overrideredirect( True)   

wth,hgh = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry('{}x{}+{}+{}'.format(GetSystemMetrics(0) ,GetSystemMetrics(1),secondMonitor,0))



def move_window(event):
    menus.geometry(f'+0+{event.y_root}')


#transparent background
#window.wm_attributes('-alpha',0.5  )
menus.bind("<space>", move_window)
window.mainloop()
