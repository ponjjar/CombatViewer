import cv2
import mouse
import keyboard
import time
import pyautogui

import threading 
import os
PROJECTOR_RESOLUTION_WIDTH = 1920 # The width of your projector
PROJECTOR_RESOLUTION_HEIGHT = 1280 # The height of your projector

secondMonitor=1920

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

print("Starting...")

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

    print("Trace the corners of the screen and press 'f' when finished.")
    dotsX = []
    dotsY = []
    
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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = backSub.apply(frame)
        new_image = cv2.bitwise_and(gray,mask)
        thresh = cv2.inRange(new_image, cv2.getTrackbarPos("Brilho", "calibration"), 255)
        dilated = cv2.dilate(thresh, None, iterations=3)
        
        
        cv2.rectangle(dilated, (10, 25), (100,20), (255,255,255), -1)
        cv2.putText(dilated, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (1, 1),
               cv2.FONT_HERSHEY_SIMPLEX, 0.1 , (0,0,0))
        contours = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        
        newTrack =  cv2.getTrackbarPos("Brilho", "calibration")
        
        if(dotsX == [] or dotsY == []):
                 cv2.putText(thresh, "F - {}".format('Contorne a area'), (20, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 3)
        if(newTrack != pastTrackbar):
                pastTrackbar = newTrack
                dotsX.clear()  
                dotsY.clear() 
        for contour in contours:     
            area = cv2.contourArea(contour)
            if area > 10 :
                
                x, y, w, h = cv2.boundingRect(contour)
                #cv2.rectangle(thresh, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(thresh, "Status: {}".format('Laser Detectado'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 3)
                dotsX.append(x + w / 2)
                dotsY.append(y + h / 2)

        # Display the resulting frame
        cv2.imshow('calibration', thresh)

        if cv2.waitKey(1) == ord('f'):
                    
            return finish(dotsX, dotsY)

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap.set(3, 1920)
cap.set(4, 1280)

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

                    cv2.rectangle(dilated, (x, y), (x + w, y + h), (255, 255, 255), 2)
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