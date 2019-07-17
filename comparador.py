import time
import datetime

class Pessoa:
    def __init__(self, dado):
        self.nome = ''
        self.idade = ''
        self.email = ''
        self.processaDado(dado)

    def processaDado(self, dado):
        dados = dado[0:-1].split(',')
        self.nome = dados[0]
        self.idade = dados[1]
        self.email = dados[2]

    def getDados(self):
        return ('%s,%s,%s' % (self.nome, self.idade, self.email))

def leArquivos(arquivo):
    listaDados = []
    with open(arquivo) as f:
        for linha in f:
            listaDados.append(linha)
    return listaDados

def escreveArquivo(lista, arquivo):
    arquivo = open(arquivo, 'w')
    for pessoa in lista:
        arquivo.write('%s\n' % (pessoa.getDados()))
    arquivo.close()

def log(mensagem):
    hora_atual = time.time()
    st = datetime.datetime.fromtimestamp(hora_atual).strftime('%Y-%m-%d %H:%M:%S')
    print('[%s] %s' % (st, mensagem))

if __name__ == "__main__":
    log("Inicio")

    listaDados1 = leArquivos("input1.txt")
    listaDados2 = leArquivos("input2.txt")

    log('Lista 1: %d' % len(listaDados1))
    log('Lista 2: %d' % len(listaDados2))

    listafinal = list(set(listaDados1) & set(listaDados2))

    log('Dados repetidos : %d' % len(listafinal))

    del listaDados1
    del listaDados2

    conjuntoDados = []

    for linha in listafinal:
        conjuntoDados.append(Pessoa(linha))

    del listafinal

    escreveArquivo(conjuntoDados, 'output.txt')
    log("Fim")




