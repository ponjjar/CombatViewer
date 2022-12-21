from PIL import Image,ImageTk
customHeight = 75
customWidth = 120  

#1cia CCAP = 1, 4 - 1 pel 1gc -> 5,9 - pelcom -> 12- pelmort -> 14 - pelexp -> 13 - pmt -> 15 - saude -> 16

ImagePathPais = [
"./kalunguinhas/28bimec.png", 
"./kalunguinhas/28bimec/cias/1.png",
"./kalunguinhas/28bimec/cias/2.png",
"./kalunguinhas/28bimec/cias/3.png",
"./kalunguinhas/28bimec/cias/ccap.png",
"./kalunguinhas/28bimec/cias/1/1pel.png",
"./kalunguinhas/28bimec/cias/1/2pel.png",
"./kalunguinhas/28bimec/cias/1/3pel.png",
"./kalunguinhas/28bimec/cias/1/4pel.png",
"./kalunguinhas/28bimec/cias/1/1pel/1gc.png",
"./kalunguinhas/28bimec/cias/1/1pel/2gc.png",
"./kalunguinhas/28bimec/cias/1/1pel/3gc.png",
"./kalunguinhas/28bimec/cias/ccap/com.png",
"./kalunguinhas/28bimec/cias/ccap/exp.png",
"./kalunguinhas/28bimec/cias/ccap/mort.png",
"./kalunguinhas/28bimec/cias/ccap/pmt.png",
"./kalunguinhas/28bimec/cias/ccap/saude.png"]

ImagePathPaisVermelho = [
"./kalunguinhas-vermelho/28bimec.png", 
"./kalunguinhas-vermelho/28bimec/cias/1.png",
"./kalunguinhas-vermelho/28bimec/cias/2.png",
"./kalunguinhas-vermelho/28bimec/cias/3.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap.png",
"./kalunguinhas-vermelho/28bimec/cias/1/1pel.png",
"./kalunguinhas-vermelho/28bimec/cias/1/2pel.png",
"./kalunguinhas-vermelho/28bimec/cias/1/3pel.png",
"./kalunguinhas-vermelho/28bimec/cias/1/4pel.png",
"./kalunguinhas-vermelho/28bimec/cias/1/1pel/1gc.png",
"./kalunguinhas-vermelho/28bimec/cias/1/1pel/2gc.png",
"./kalunguinhas-vermelho/28bimec/cias/1/1pel/3gc.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap/com.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap/exp.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap/mort.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap/pmt.png",
"./kalunguinhas-vermelho/28bimec/cias/ccap/saude.png"]

def OpenPhotoImagePais (imageNumber):
    global ImagePathPais,customWidth,customHeight

    print("Criado " + ImagePathPais[imageNumber])
    return ImageTk.PhotoImage(Image.open(ImagePathPais[imageNumber]).resize((customWidth,customHeight), Image.ANTIALIAS))

def OpenPhotoImagePaisVermelho (imageNumber):
    return ImageTk.PhotoImage(Image.open(ImagePathPaisVermelho[imageNumber]).resize((customWidth,customHeight), Image.ANTIALIAS))
#Carrega as imagens inicialmente
imagesPais = []
imagesPaisVermelho = []
for i in range(len(ImagePathPais)):
        imagesPais.append(OpenPhotoImagePais(i))
        imagesPaisVermelho.append(OpenPhotoImagePaisVermelho(i))
bimec= OpenPhotoImagePaisVermelho(0)
OpenPhotoImagePaisVermelho(0)

#Cores das linhas do itirenário

