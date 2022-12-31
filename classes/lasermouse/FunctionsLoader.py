# importando bibliotecas
import cv2, mouse, keyboard,  time, pyautogui, threading, os
from classes.lasermouse.StartVariables import *
 
# iniciando a camera
cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# verificando se a camera foi iniciada
if not cap.isOpened():
    print("Não foi possivel carregar esse Camera_ID")
    exit()

# função de calibração
def calibrate():
    # função para mudar o brilho
    def onThresholdTrackbarChanged(value):
        pass

    # função para finalizar a calibração
    def finish(dotsX, dotsY):
        threshold = cv2.getTrackbarPos("Brilho", "calibration")
        cv2.destroyWindow('calibration')

        lowXpos = min(dotsX)
        lowYpos = min(dotsY)
        highXpos = max(dotsX)
        highYpos = max(dotsY)
        return lowXpos, lowYpos, highXpos, highYpos, threshold


    # criando a janela de calibração
    cv2.namedWindow('calibration')

    # criando o trackbar de brilho
    cv2.createTrackbar('Brilho', 'calibration', 255, 255, onThresholdTrackbarChanged)

    # printando instruções
    print("Contorne as bordas do projetor e depois aperte F")
    dotsX = []
    dotsY = []
    # função para capturar os clicks do mouse
    def click_event(event, x, y, flags, params):
        global drawing

        if event == cv2.EVENT_LBUTTONDOWN:
         drawing = True
         ix,iy = x,y
        elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
            dotsX.append(x)
            dotsY.append(y)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
        elif event == cv2.EVENT_RBUTTONDOWN:
            dotsX.clear()  
            dotsY.clear() 

            
    # criando o background subtractor
    backSub = cv2.createBackgroundSubtractorMOG2( history=25, varThreshold=150, detectShadows=False)
    restTime = time.time()
    pastTrackbar =  cv2.getTrackbarPos("Brilho", "calibration")
    newTrack =  0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não é possível receber o quadro (fim da stream?). saindo ...")
            break
        frameClone = frame
        original = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frameClone, cv2.COLOR_BGR2GRAY)
        mask = backSub.apply(frameClone)
        new_image = cv2.bitwise_and(gray,mask)
        thresh = cv2.inRange(new_image, cv2.getTrackbarPos("Brilho", "calibration"), 255)
        dilated = thresh
        contours = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        
        newTrack =  cv2.getTrackbarPos("Brilho", "calibration")

        if(len(dotsX) > 10 and len(dotsY) > 10):
                    c1 = min(dotsX), min(dotsY)
                    c2 = max(dotsX), max(dotsY)
                    cv2.rectangle(dilated, (int(c1[0]), int(c1[1])), (int(c2[0]), int(c2[1])), (255, 0, 0), 2)
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
                dotsX.append(x + w / 2)
                dotsY.append(y + h / 2)

        cv2.setMouseCallback('calibration', click_event)
        
        new_image = cv2.bitwise_or(original,finalImg)
        cv2.imshow('calibration', new_image)

        if cv2.waitKey(1) == ord('f'):
                    
            return finish(dotsX, dotsY)
# função para mudar o offset do eixo Y
def onOffsetYTrackbarChanged(value):
        global PROJECTOR_Y_OFFSET
        PROJECTOR_Y_OFFSET =int(value)
        pass
# função para mudar o offset do eixo X
def onOffsetXTrackbarChanged(value):
        global PROJECTOR_X_OFFSET
        PROJECTOR_X_OFFSET =int(value)
        pass
# função para mudar o offset do eixo X
def onOffsetXTrackbarChanged(value):
        global PROJECTOR_X_OFFSET
        PROJECTOR_X_OFFSET =int(value)
        pass
# função para mostrar a camera
def preview():
    
   
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não é possível receber o quadro (fim da stream?). saindo ...")
            break

        cv2.putText(frame, "C - {}".format('Pressione C para calibrar'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 3)
        cv2.imshow('preview', frame)

        
        if cv2.waitKey(1) == ord('c'):
            break
    
    main(calibrate())

# função para mover o mouse
def move_mouse(dotX, dotY, top_left, bottom_right):
    # função para pegar o tamanho da tela
    def get_size(top_left, bottom_right):
        return bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]

    # função para pegar o offset do laser
    def offset_laser_pos(dotX, dotY):
        return dotX - top_left[0], dotY - top_left[1]

    # função para traduzir o tamanho da tela
    def translate_size(x, y, hsize, vsize, display_width, display_height):
        x = (x * display_width) / hsize
        y = (y * display_height) / vsize
        return x, y
    
    # pegando o tamanho da tela
    hsize, vsize = get_size(top_left, bottom_right)
    # pegando o offset do laser
    offsetX, offsetY = offset_laser_pos(dotX, dotY)
    
    # traduzindo o tamanho da tela
    x, y = translate_size(offsetX, offsetY, hsize, vsize, PROJECTOR_RESOLUTION_WIDTH, PROJECTOR_RESOLUTION_HEIGHT)
    # verificando se o mouse está dentro da tela
    if(x + PROJECTOR_X_OFFSET < PROJECTOR_RESOLUTION_WIDTH and x + PROJECTOR_X_OFFSET> 0 and y + PROJECTOR_Y_OFFSET < PROJECTOR_RESOLUTION_HEIGHT and y> 0):
        # movendo o mouse
        mouse.move(x+SECONDMONITOR+PROJECTOR_X_OFFSET, y+PROJECTOR_Y_OFFSET, absolute=True, duration=0.02)
# função para rastrear o cursor
def cursor_track():
    timeStartMovement = 0.0
    while True:
        mouseLeft = False
        if keyboard.is_pressed("pagedown"):
                        timeStartMovement = time.time()
                        if(mouseLeft == False): 
                            pyautogui.mouseDown(button='left') 
                            mouseLeft = True      
        elif(float(time.time()) - float(timeStartMovement) > 0.12 and float(time.time()) - float(timeStartMovement) < 0.5 ):
                        pyautogui.mouseUp(button='left')  
                        mouseLeft = False
        if cv2.waitKey(1) == ord('q')  : break
done1 = 0
# função para executar o bat
def bat1():
    global done1, res1
    res1 = os.system("python ./CombatViewer.py")
    done1 = 1
# função principal
def main(calibration):

    top_left = (int(calibration[0]), int(calibration[1]))
    bottom_right = (int(calibration[2]), int(calibration[3]))
    threshold = calibration[4]
    backSub = cv2.createBackgroundSubtractorMOG2( history=25, varThreshold=150, detectShadows=True)
    # criando as threads
    p2 = threading.Thread(target=bat1)
    p1 = threading.Thread(target=cursor_track)
    # iniciando as threads
    p1.start() 
    p2.start()
    # criando a janela
    cv2.namedWindow('MouseViewer')
    # criando o trackbar de offset do eixo Y
    cv2.createTrackbar('DeslocamentoY', 'MouseViewer', 0, 500, onOffsetYTrackbarChanged)
    cv2.setTrackbarMin('DeslocamentoY', 'MouseViewer', -500)
    # criando o trackbar de offset do eixo X
    cv2.createTrackbar('DeslocamentoX', 'MouseViewer', 0, 500, onOffsetXTrackbarChanged)
    cv2.setTrackbarMin('DeslocamentoX', 'MouseViewer', -500)
    # função para mudar o brilho
    def onThresholdTrackbarChanged(value):
        pass
    # criando o trackbar de brilho
    cv2.createTrackbar('Brilho', 'MouseViewer', threshold   , 255, onThresholdTrackbarChanged)
    # criando o trackbar de brilho máximo
    cv2.createTrackbar('BrilhoMax', 'MouseViewer', 255, 255, onThresholdTrackbarChanged)
    
    while not (done1):
        threshold=  cv2.getTrackbarPos("Brilho", "MouseViewer")
        brilhoMax=  cv2.getTrackbarPos("BrilhoMax", "MouseViewer")
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break
        output = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = backSub.apply(frame)
        new_image = cv2.bitwise_and(gray,mask)
        thresh = cv2.inRange(new_image, threshold, brilhoMax)
        dilated = thresh
        dotX = []
        dotY = []
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        for contour in contours:    
            area = cv2.contourArea(contour)
            if area > 10:
                    x, y, w, h = cv2.boundingRect(contour)

                    dotX = [(x + w / 2)]
                    dotY = [(y + h / 2)]
        for i in range(len(dotX)):
            move_mouse(dotX[i] , dotY[i], top_left, bottom_right)
        output = cv2.rectangle(dilated, top_left, bottom_right, (255,255,255), 2)
        outputmasked = cv2.bitwise_or(output, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        cv2.imshow('MouseViewer', outputmasked)
        if cv2.waitKey(33) == 27 or done1 == 1 :
            break
