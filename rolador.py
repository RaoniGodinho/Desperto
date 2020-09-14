import random

random.seed(None)

def rolar():
    return random.randrange(1,10)

def sucessos(array):
    qtdeSucessos = 0
    for x in array:
        if (x >=6): 
            qtdeSucessos = qtdeSucessos + 1
        elif (x == 1):
            qtdeSucessos = qtdeSucessos - 1
    if (qtdeSucessos < 0):
        qtdeSucessos = 0
    return qtdeSucessos

def explodir(array):
    for x in array:
        if (x == 10):
            array.append(rolar())
    return array

def formatarResposta(array):
    resposta = "Resultado: "
    strSucessos = "Sucessos: " + str(sucessos(array)) + "."
    contador = 0
    tamanho = len(array)
    while (contador < tamanho):
        resposta = resposta + str(array[contador]) 
        if (contador < tamanho - 1):
            resposta = resposta + ", "
        else:
            resposta = resposta + ". "
        contador = contador + 1
    resposta = resposta + strSucessos
    return resposta

def rolard10(qtde):
    array = ([rolar()])
    contador = 1
    while (contador < qtde):
        array.append(rolar())
        contador = contador + 1
    array = explodir(array)
    return array

def interpretadorDado(messageArray):
    if messageArray[0] != '!d':
        return 'Comando incorreto.'
    if (len(messageArray) > 1 and messageArray[1].isnumeric()):
        messageArray = rolard10(int(messageArray[1]))
    else:
        messageArray = rolard10(1)
    return formatarResposta(messageArray)



