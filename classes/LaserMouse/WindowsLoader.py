from PIL import Image,ImageTk
import PIL
from tkinter import *
import os.path

def win():    
    splash_root.destroy()
    win=Tk()
    def new_window():
        top = Toplevel()
        w = top.winfo_reqwidth()
        h = top.winfo_reqheight()
        ws = top.winfo_screenwidth()
        hs = top.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        top.geometry('+%d+%d' % (x, y))
        def quittop():
            top.destroy()
        top.title("Definir Resolução")
        Label(top, text="Resolução da Largura da Primeira tela", font=  ("Aerial 15")).pack()
        a=Entry(top, font=  ("Aerial 15"),width=10)
        a.insert(END, '1280')
        a.pack()
        Label(top, text="Resolução da Largura da Segunda tela", font=  ("Aerial 15")).pack()
        c=Entry(top, font=  ("Aerial 15"),width=10)
        c.insert(END, '1920')
        c.pack()
        Label(top, text="Resolução da Altura da Segunda tela", font=  ("Aerial 15")).pack()
        b=Entry(top, font=  ("Aerial 15"),width=10)
        b.insert(END, '1080')
        b.pack()
        Label(top, text="Dica: Full HD (alta definição total), é uma resolução de tela muito comum com a largura de 1920 x 1080 pixels.\n  Utilize 0 na resolução do primeiro monitor caso não esteja estendido.").pack(pady=2)
        Label(top, text="Camera ID", font=  ("Aerial 15")).pack()
        d=Entry(top, font=  ("Aerial 15"),width=10)
        d.insert(END, '2')
        d.pack() 
        Label(top, text="Identificador da camera a ser utilizada, esse numero pode ser variavel, geralmente 2 é utilizado para o droidCam e 0 ou 1 para web cam").pack(pady=2)
        
        def changeresolutions():
            t1=int(a.get())
            t2=int(b.get())
            t3=int(c.get())
            t4=int(d.get())
            #Abrir um arquivo para escrita
            arquivo = open('settings.txt', 'w')
            try:
                #Escrever no arquivo
                arquivo.write (" FIRSTMONITOR_RESOLUTION_WIDTH: " + str(t1) + "\n PROJECTOR_RESOLUTION_WIDTH: " + str(t2) + "\n PROJECTOR_RESOLUTION_HEIGHT: "+ str(t3)+ "\n CAMERA_INDEX: "+ str(t4))
            finally:
                #Fechar o arquivo
                arquivo.close ()


        Button(top, text="Confirmar", font=  ("Aerial 12"), command=lambda:[changeresolutions(),quittop(), quit()]).pack()
    
    if(os.path.exists("settings.txt")):
        #Caso tenha configurado antes, pergunta se deseja configurar dnv
        l = Label(win, text="Deseja alterar as configurações de resolução?",font=  ("Aerial 15")).pack(padx=10, pady=3)       
        Button(win, text="Sim",font=  ("Aerial 12"), command=lambda:[new_window()]).pack(side=LEFT,fill="both", expand=True)
        Button(win, text="Não",font=  ("Aerial 12"), command=lambda: [quit()]).pack(side=RIGHT,fill="both", expand=True)

        
        w = win.winfo_reqwidth()
        h = win.winfo_reqheight()
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win.geometry('+%d+%d' % (x, y))
    else:
        #Caso não tenha configurado antes, manda a janela de pergunta para o espaço
        win.geometry('+-999+-999')
        new_window()
 
    def quit():
        win.destroy()
    win.mainloop()
   
splash_root = Tk()
 
splash_root.geometry("700x230")
w = 700
h = 230
ws = splash_root.winfo_screenwidth()
hs = splash_root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
splash_root.geometry('+%d+%d' % (x, y))
canvas = Canvas(splash_root)

splash_root.focus_set()
splash_root.overrideredirect(1)


canvas.pack(fill=BOTH, expand=True)
image = PIL.Image.open("./kalunguinhas/combatViewerSplash.png")
resized = image.resize((int(700), int(230)), PIL.Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized,  master=splash_root)
canvas.create_image(0, 0, image=bg, anchor='nw')

canvas.pack()
canvas.configure(background='black')
splash_root.after(3000, win)
splash_root.mainloop()
