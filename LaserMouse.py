#Importa as janelas inciais a serem abertas ( configuração de resolução, splash image e entre outras ... )
from classes.LaserMouse.WindowsLoader import *
#Importa as funções e os valores a serem carregados. 
from classes.LaserMouse.FunctionsLoader import *

def main ():
    print("Iniciando...")
    LoadConfigs()
    preview()
    
main()
# Quando tudo feito, solte a captura e destrua todas as janela
cap.release()
cv2.destroyAllWindows() 
exit()
