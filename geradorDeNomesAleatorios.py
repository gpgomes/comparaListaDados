from random import randrange
import time
import datetime

def log(mensagem):
    hora_atual = time.time()
    st = datetime.datetime.fromtimestamp(hora_atual).strftime('%Y-%m-%d %H:%M:%S')
    print('[%s] %s' % (st, mensagem))

def leArquivos(arquivo):
    listaDados = []
    with open(arquivo) as f:
        for linha in f:
            listaDados.append(linha[0:-1])

    return listaDados

def escreveArquivo(lista, arquivo):
    arquivo = open(arquivo, 'w')
    for item in lista:
        arquivo.write(item + '\n')
    arquivo.close()

def montaDado(nome, segundoNome, sobrenome, idade):
    return ('%s %s %s,%d,%s.%s@gmail.com' % (nome, segundoNome, sobrenome, idade, nome, sobrenome))

if __name__ == "__main__":
    log("Inicio")

    sobrenomes = leArquivos('names.txt')
    nomes = leArquivos('first-names.txt')
    segundoNome = leArquivos('middle-names.txt')

    totalNomes = 1000000 # quantidade nome a serem gerados
    i = 0

    lista1 = []
    lista2 = []

    while i < totalNomes:
        dado = montaDado(nomes[randrange(len(nomes))], segundoNome[randrange(len(segundoNome))],
                        sobrenomes[randrange(len(sobrenomes))], randrange(60))
        if (i % 2):
            lista1.append(dado)
        elif (i % 3):
            lista2.append(dado)
        else:
            lista1.append(dado)
            lista2.append(dado)
        i+=1

    escreveArquivo(lista1, 'input1.txt')
    escreveArquivo(lista2, 'input2.txt')

    log("Fim")





