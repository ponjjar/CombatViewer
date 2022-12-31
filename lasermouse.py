import cv2
import mouse
import keyboard
import time
import pyautogui
from PIL import Image,ImageTk
import PIL
import threading 
import os
from tkinter import *

PROJECTOR_RESOLUTION_WIDTH = 1920 # A largura do projetor
PROJECTOR_RESOLUTION_HEIGHT = 1280 # The height of your projector
secondMonitor=0

# Create object
splash_root = Tk()
 
# Adjust size
splash_root.geometry("700x230")
w = 700
h = 230
ws = splash_root.winfo_screenwidth()
hs = splash_root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
splash_root.geometry('+%d+%d' % (x, y))
# Set Label
#splash_label = Label(splash_root, text="Splash Screen", font=18)
#splash_label.pack()

canvas = Canvas(splash_root)

splash_root.focus_set()
splash_root.overrideredirect(1)


canvas.pack(fill=BOTH, expand=True)
image = PIL.Image.open("./kalunguinhas/combatViewerSplash.png")
resized = image.resize((int(700), int(230)), PIL.Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized,  master=splash_root)
canvas.create_image(0, 0, image=bg, anchor='nw')


#canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.pack()
canvas.configure(background='black')
# main window function

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
        # By default, it is kept as the geometry of the main window, but you can change it.
        # Create an Entry widget
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
    # b=Entry(top, width=35)
        lab = Label(top, text="Dica: Full HD (alta definição total), é uma resolução de tela muito comum com a largura de 1920 x 1080 pixels.\n  Utilize 0 na resolução do primeiro monitor caso não esteja estendido.")
        lab.pack(pady=2)
        def changeresolutions():
            global secondMonitor, PROJECTOR_RESOLUTION_WIDTH, PROJECTOR_RESOLUTION_HEIGHT
            t1=int(a.get())
            t2=int(b.get())
            t3=int(c.get())
            PROJECTOR_RESOLUTION_WIDTH = t2
            PROJECTOR_RESOLUTION_HEIGHT = t3
            #Abrir um arquivo para escrita
            arquivo = open('settings.txt', 'w')
            try:
                #Escrever no arquivo
                arquivo.write (" FIRSTMONITOR_RESOLUTION_WIDTH: " + str(t1) + "\n PROJECTOR_RESOLUTION_WIDTH: " + str(t2) + "\n PROJECTOR_RESOLUTION_HEIGHT: "+ str(t3))
            finally:
                #Fechar o arquivo
                arquivo.close ()


            secondMonitor = t1 # The width of your projector
        Button(top, text="Confirmar", font=  ("Aerial 12"), command=lambda:[changeresolutions(),quittop(), quit()]).pack()
    
    l = Label(win, text="Deseja alterar as configurações de resolução?",font=  ("Aerial 15"))
    l.pack(padx=10, pady=3)
    w = win.winfo_reqwidth()
    h = win.winfo_reqheight()
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    win.geometry('+%d+%d' % (x, y))
    def quit():
        win.destroy()
        
    def LoadConfigs():
            global secondMonitor, PROJECTOR_RESOLUTION_WIDTH, PROJECTOR_RESOLUTION_HEIGHT
            #Carrega estado das configurações passadas no settings.txt
            arquivo = open('settings.txt', 'r')
            try:
                #Escrever no arquivo
                linhas = arquivo.readlines()
                secondMonitor = int(linhas[0].replace("\n", "").split(":")[1])
                PROJECTOR_RESOLUTION_WIDTH = int(linhas[1].replace("\n", "").split(":")[1])   
                PROJECTOR_RESOLUTION_HEIGHT = int(linhas[2].replace("\n", "").split(":")[1]) 
            finally:
                #Fechar o arquivo
                arquivo.close ()
    Button(win, text="Sim",font=  ("Aerial 12"), command=lambda:[new_window()]).pack(side=LEFT,fill="both", expand=True)
    Button(win, text="Não",font=  ("Aerial 12"), command=lambda: [LoadConfigs(), quit()]).pack(side=RIGHT,fill="both", expand=True)
    win.mainloop()
   

# Set Interval
splash_root.after(3000, win)
 
splash_root.mainloop()

# Execute tkinter
# If you are mirroring, just use 0. 
# Otherwise, figure out where your projector is compared to your 
# main monitor's top left. Negative values are allowed, and
# represent the projector being to the left of your main monitor.
# For example, my projector is to the right of my main monitor,
# and my main monitor has an X resolution of 1920, so I would
# set PROJECTOR_X_OFFSET to 1920.
# This represents the position of the left size of the projector.
# Not sure? Run print_position.py and move your mouse to the left side
# of the projector screen and use that X coordinate.
PROJECTOR_X_OFFSET = 0
PROJECTOR_Y_OFFSET = 0 # Same as above, but for the Y axis.

CAMERA_INDEX = 0 # 0 indexed, often the built-in webcam on a laptop
LEFT_CLICK_MAPPING = 'pagedown' # Figure out what your presenter's buttons use
RIGHT_CLICK_MAPPING = 'up' # Figure out what your presenter's buttons use

drawing = False 
print("Iniciando...")
def calibrate():
    def onThresholdTrackbarChanged(value):
        pass

    def finish(dotsX, dotsY):
        threshold = cv2.getTrackbarPos("Brilho", "calibration")
        cv2.destroyWindow('calibration')

        lowXpos = min(dotsX)
        lowYpos = min(dotsY)
        highXpos = max(dotsX)
        highYpos = max(dotsY)
        return lowXpos, lowYpos, highXpos, highYpos, threshold


    cv2.namedWindow('calibration')

    cv2.createTrackbar('Brilho', 'calibration', 255, 255, onThresholdTrackbarChanged)

    print("Contorne as bordas do projetor e depois aperte F")
    dotsX = []
    dotsY = []
    def click_event(event, x, y, flags, params):
        global drawing

        if event == cv2.EVENT_LBUTTONDOWN:
         drawing = True
         ix,iy = x,y
        elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
 
            # displaying the coordinates
            # on the Shell
            dotsX.append(x)
            dotsY.append(y)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
        elif event == cv2.EVENT_RBUTTONDOWN:
            #drawing = False
            dotsX.clear()  
            dotsY.clear() 

            
    backSub = cv2.createBackgroundSubtractorMOG2( history=25, varThreshold=150, detectShadows=False)
    restTime = time.time()
    pastTrackbar =  cv2.getTrackbarPos("Brilho", "calibration")
    newTrack =  0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        '''  if float(time.time()) - float(restTime) > 50 :
            backSub = cv2.createBackgroundSubtractorKNN(cv2.COLOR_BGR2GRAY) 
            print(float(time.time()) - float(restTime))
            restTime = time.time()'''
        frameClone = frame
        original = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frameClone, cv2.COLOR_BGR2GRAY)
        mask = backSub.apply(frameClone)
        new_image = cv2.bitwise_and(gray,mask)
        thresh = cv2.inRange(new_image, cv2.getTrackbarPos("Brilho", "calibration"), 255)
        dilated = thresh
        
        
        #cv2.rectangle(dilated, (10, 25), (100,20), (255,255,255), -1)
        #cv2.putText(dilated, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (1, 1),cv2.FONT_HERSHEY_SIMPLEX, 0.1 , (0,0,0))
        contours = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        
        newTrack =  cv2.getTrackbarPos("Brilho", "calibration")

        if(len(dotsX) > 10 and len(dotsY) > 10):
                    c1 = min(dotsX), min(dotsY)
                    c2 = max(dotsX), max(dotsY)
                
                    #cria as bordas do retangulo na imagem processada
                    cv2.rectangle(dilated, (int(c1[0]), int(c1[1])), (int(c2[0]), int(c2[1])), (255, 0, 0), 2)
                    #Cria um retangulo escuro na imagem original
                    cv2.rectangle(original, (int(c1[0]), int(c1[1])), (int(c2[0]), int(c2[1])), (0, 0, 0), -1)
   
        if(newTrack != pastTrackbar):
                pastTrackbar = newTrack
                dotsX.clear()  
                dotsY.clear() 
        finalImg = thresh.copy()
        if(dotsX == [] or dotsY == []):
                 cv2.putText(finalImg, "{}".format('Contorne as bordas com o Laser'), (15, 25), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 3)
                 cv2.putText(finalImg, "{}".format('-> use o Botao esquerdo para Selecionar area'), (15, 55), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 3)        
        elif(len(dotsX) > 7 and len(dotsY) > 7):
                 cv2.putText(finalImg, "{}".format('Pressione F para finalizar'), (15, 25), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 3)
                 cv2.putText(finalImg, "{}".format('-> use o Botao direito para Limpar area'), (15, 55), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 3)
        
        elif(len(dotsX) <= 7 and len(dotsY) <= 7):
                    cv2.putText(finalImg, "Status: {}".format('Contornando a area: ' + str(int((len(dotsX) * 100) /8)) + " %"), (15, 25), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 3)
 
        for contour in contours:     
            area = cv2.contourArea(contour)
            if area > 10 :
                x, y, w, h = cv2.boundingRect(contour)
                #cv2.rectangle(thresh, (x, y), (x+w, y+h), (0, 255, 0), 2)
                dotsX.append(x + w / 2)
                dotsY.append(y + h / 2)

                    #cv2.rectangle(dilated, lowXpos,lowYpos,highXpos,highYpos , (255,255,255), -1)
        cv2.setMouseCallback('calibration', click_event)
        # Display the resulting frame
        
        new_image = cv2.bitwise_or(original,finalImg)
        cv2.imshow('calibration', new_image)

        if cv2.waitKey(1) == ord('f'):
                    
            return finish(dotsX, dotsY)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
def onOffsetYTrackbarChanged(value):
        global PROJECTOR_Y_OFFSET
        PROJECTOR_Y_OFFSET =int(value)
        pass
def onOffsetXTrackbarChanged(value):
        global PROJECTOR_X_OFFSET
        PROJECTOR_X_OFFSET =int(value)
        pass
def onOffsetXTrackbarChanged(value):
        global PROJECTOR_X_OFFSET
        PROJECTOR_X_OFFSET =int(value)
        pass
def preview():
    
   
    while True:
        
        
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.putText(frame, "C - {}".format('Pressione C para calibrar'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 3)
        cv2.imshow('preview', frame)

        
        if cv2.waitKey(1) == ord('c'):
            break
    
    main(calibrate())

def move_mouse(dotX, dotY, top_left, bottom_right):
    def get_size(top_left, bottom_right):
        return bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]

    def offset_laser_pos(dotX, dotY):
        return dotX - top_left[0], dotY - top_left[1]

    def translate_size(x, y, hsize, vsize, display_width, display_height):
        x = (x * display_width) / hsize
        y = (y * display_height) / vsize
        return x, y
    
    hsize, vsize = get_size(top_left, bottom_right)
    offsetX, offsetY = offset_laser_pos(dotX, dotY)
    
    x, y = translate_size(offsetX, offsetY, hsize, vsize, PROJECTOR_RESOLUTION_WIDTH, PROJECTOR_RESOLUTION_HEIGHT)
    if(x + PROJECTOR_X_OFFSET < PROJECTOR_RESOLUTION_WIDTH and x + PROJECTOR_X_OFFSET> 0 and y + PROJECTOR_Y_OFFSET < PROJECTOR_RESOLUTION_HEIGHT and y> 0):
        mouse.move(x+secondMonitor+PROJECTOR_X_OFFSET, y+PROJECTOR_Y_OFFSET, absolute=True, duration=0.02)
# Prints Cursor position
def cursor_track():# Prints Cursor position
    timeStartMovement = 0.0
    while True:
        #print("oi")
        mouseLeft = False
        if keyboard.is_pressed("pagedown"):
                        timeStartMovement = time.time()
                        if(mouseLeft == False): 
                            pyautogui.mouseDown(button='left') 
                            mouseLeft = True      
                    # print (float(time.time()) - float(timeStartMovement))
        elif(float(time.time()) - float(timeStartMovement) > 0.12 and float(time.time()) - float(timeStartMovement) < 0.5 ):
                    # print (float(time.time()) - float(timeStartMovement))
                        pyautogui.mouseUp(button='left')  
                        mouseLeft = False
        if cv2.waitKey(1) == ord('q')  : break
done1 = 0
def bat1():
    global done1, res1
    res1 = os.system("pythonCombatViewer.bat")
    done1 = 1
def main(calibration):
    # keyboard.on_press_key(LEFT_CLICK_MAPPING, lambda: mouse.down(button='left'), suppress=True)
    # keyboard.on_release_key(LEFT_CLICK_MAPPING, lambda: mouse.click(button='right'), suppress=True)

   # timeStartMovement = 0.0

    top_left = (int(calibration[0]), int(calibration[1]))
    bottom_right = (int(calibration[2]), int(calibration[3]))
    threshold = calibration[4]
    backSub = cv2.createBackgroundSubtractorMOG2( history=25, varThreshold=150, detectShadows=True)
   
 
    p2 = threading.Thread(target=bat1)
    p1 = threading.Thread(target=cursor_track)
    p1.start() 
    p2.start()
    #os.system("C:/Users/leroma/AppData/Local/Microsoft/WindowsApps/python3.10.exe CombateViewer.py 2")
    #subprocess.call("C:/Users/leroma/AppData/Local/Microsoft/WindowsApps/python3.10.exe CombateViewer.py", shell=True)
    cv2.namedWindow('MouseViewer')

    cv2.createTrackbar('DeslocamentoY', 'MouseViewer', 0, 500, onOffsetYTrackbarChanged)
    cv2.setTrackbarMin('DeslocamentoY', 'MouseViewer', -500)
    cv2.createTrackbar('DeslocamentoX', 'MouseViewer', 0, 500, onOffsetXTrackbarChanged)
    cv2.setTrackbarMin('DeslocamentoX', 'MouseViewer', -500)
    def onThresholdTrackbarChanged(value):
        pass
    cv2.createTrackbar('Brilho', 'MouseViewer', threshold   , 255, onThresholdTrackbarChanged)
    cv2.createTrackbar('BrilhoMax', 'MouseViewer', 255, 255, onThresholdTrackbarChanged)
    
    while not (done1):
        threshold=  cv2.getTrackbarPos("Brilho", "MouseViewer")
        brilhoMax=  cv2.getTrackbarPos("BrilhoMax", "MouseViewer")

        ret, frame = cap.read()
        #cap.set(cv2.CAP_PROP_POS_FRAME)
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        output = frame.copy()

        # Process the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = backSub.apply(frame)
        new_image = cv2.bitwise_and(gray,mask)
        thresh = cv2.inRange(new_image, threshold, brilhoMax)
        
        dilated = thresh
        
        
       # cv2.rectangle(dilated, (10, 25), (100,20), (255,255,255), -1)
        #cv2.putText(dilated, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (5, 5),cv2.FONT_HERSHEY_SIMPLEX, 0.1    , (0,0,0))
       
        #----
        dotX = []
        dotY = []
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        max_area = 0
        for contour in contours:    
            area = cv2.contourArea(contour)
            if area > 10:
                    max_area = area
                    x, y, w, h = cv2.boundingRect(contour)

                    #cv2.rectangle(dilated, (x, y), (x + w, y + h), (255, 255, 255), 2)
                    #find the biggest cv2.boundingRect
                    
                    dotX = [(x + w / 2)]
                    dotY = [(y + h / 2)]
                    

                  #  rectangleArea = w * h
                  #  if rectangleArea > 0:
                  #      cv2.rectangle(outputmasked, (x, y), (x + w, y + h), (255, 255, 255), 2)
                  #      cv2.putText(outputmasked, str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.1, (255, 255, 255))
                  #      cv2.putText(outputmasked, str(rectangleArea), (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.1, (255, 255, 255))
        for i in range(len(dotX)):
            move_mouse(dotX[i] , dotY[i], top_left, bottom_right)
            

        output = cv2.rectangle(dilated, top_left, bottom_right, (255,255,255), 2)
        outputmasked = cv2.bitwise_or(output, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        cv2.imshow('MouseViewer', outputmasked)
        if cv2.waitKey(1) == ord('q')  : break

preview()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 
