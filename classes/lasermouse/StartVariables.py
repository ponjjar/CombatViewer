# Se você estiver espelhando, use apenas 0.
# Caso contrário, descubra onde seu projetor está comparado ao seu
# canto superior esquerdo do monitor principal. Valores negativos são permitidos e
# representa o projetor à esquerda do monitor principal.
# Por exemplo, meu projetor está à direita do meu monitor principal,
# e meu monitor principal tem uma resolução X de 1920, então eu
# defina PROJECTOR_X_OFFSET para 1920.
# Isso representa a posição do tamanho esquerdo do projetor.
# Não tenho certeza? Execute print_position.py e mova o mouse para o lado esquerdo
# da tela do projetor e use essa coordenada X.
PROJECTOR_X_OFFSET = 0 # Offset Coordenada X
PROJECTOR_Y_OFFSET = 0 # Mesma coisa de cima, mas pra coordenada Y.
CAMERA_INDEX = 1 # id da camera a ser conectada (pode ser aleatório, geralmente 2 = droidcam e 0 ou 1 = webcam)
LEFT_CLICK_MAPPING = 'pagedown' # Botão a ser pressionado com click do mouse
RIGHT_CLICK_MAPPING = 'up' # click com o botão direito
PROJECTOR_RESOLUTION_WIDTH = 1920  # Largura da resolução da projeção ( isso será configurado no programa )
PROJECTOR_RESOLUTION_HEIGHT = 1280 # Mesma coisa que de cima, só que com a altura
SECONDMONITOR=0 # Largura da resolução da tela primaria ( isso será configurado no programa )
drawing = False 

#Carrega as configurações definidas na janela inicial
def LoadConfigs():
            global SECONDMONITOR, PROJECTOR_RESOLUTION_WIDTH, PROJECTOR_RESOLUTION_HEIGHT, CAMERA_INDEX
            #Carrega estado das configurações passadas no settings.txt
            arquivo = open('settings.txt', 'r')
            try:
                #Escrever no arquivo
                linhas = arquivo.readlines()
                SECONDMONITOR = int(linhas[0].replace("\n", "").split(":")[1])
                PROJECTOR_RESOLUTION_WIDTH = int(linhas[1].replace("\n", "").split(":")[1])   
                PROJECTOR_RESOLUTION_HEIGHT = int(linhas[2].replace("\n", "").split(":")[1]) 
                CAMERA_INDEX = int(linhas[3].replace("\n", "").split(":")[1]) 
                print("Loading Configs: "+ str(linhas))
            finally:
                #Fechar o arquivo
                arquivo.close ()
LoadConfigs()