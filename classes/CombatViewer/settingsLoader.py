
#Carrega estado das configurações passadas no settings.txt
arquivo = open('settings.txt', 'r')
try:
    linhas = arquivo.readlines()
    secondMonitor = int(linhas[0].replace("\n", "").split(":")[1])
finally:
                #Fecha o arquivo
                arquivo.close ()