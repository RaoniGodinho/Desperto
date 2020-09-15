import random

random.seed(None)

especializado = False
target = 6


def rolar():
    return random.randint(1,10)

def sucessos(array):
    qtdeSucessos = 0
    for x in array:
        if ((x == 10) and especializado): 
            qtdeSucessos = qtdeSucessos + 2
        elif (x >= target): 
            qtdeSucessos = qtdeSucessos + 1
    
    qtdeFalhas = array.count(1)

    if (qtdeFalhas > qtdeSucessos):
        if (qtdeSucessos == 0):
            qtdeSucessos = 0 - qtdeFalhas
        else:
            qtdeSucessos = 0
    elif (qtdeFalhas == qtdeSucessos):
        qtdeSucessos = 0
    elif (qtdeFalhas < qtdeSucessos):
        qtdeSucessos = qtdeSucessos - qtdeFalhas

    return qtdeSucessos

def explodir(array):
    for x in array:
        if (x == 10):
            array.append(rolar())
    return array

def formatarResposta(array):
    resposta = "Resultado: "
    qtdeSucessos = sucessos(array)
    strSucessos = "Sucessos: " + str(qtdeSucessos) + "."
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
    if (qtdeSucessos == 0):
        resposta = resposta + " Falha!"
    elif (qtdeSucessos < 0):
        resposta = resposta + " FALHA CRÍTICA!!"

    return resposta

def rolard10(qtde):
    array = ([rolar()])
    contador = 1
    while (contador < qtde):
        array.append(rolar())
        contador = contador + 1
    #array = explodir(array)
    return array

def dificuldade(array):
    global target
    for x in array:
        if (x.count("-t")):
            target = x
    target = int(target.replace("-t",""))

def interpretadorDado(messageArray):
    try:
        if messageArray[0] != '!d':
            return 'Comando incorreto.'
        if (messageArray.count("-s")):
            global especializado 
            especializado = True
        dificuldade(messageArray)
        if (len(messageArray) > 1 and messageArray[1].isnumeric()):
            messageArray = rolard10(int(messageArray[1]))
        else:
            messageArray = rolard10(1)
        return formatarResposta(messageArray)
    except:
        return 'Comando incorreto.'
        


