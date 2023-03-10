# Thiago Santos - 21012009
# Kevin Silva - 21007836
# Elias Fausto - 21004040
from matriz import Matriz

estados = 0
target = [['b', 'c', 'a'], ['e', 'f', 'd'], ['h', 'i', 'g']]
start = Matriz([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])


def procurar_matriz(inicial, alvo, linha_atual):
    for i in range(len(inicial.matriz[linha_atual])):
        if linha_atual == len(inicial.matriz) - 1:
            if inicial.compare(alvo):
                return True
            else:
                inicial.estados += 1
                inicial.rotate(linha_atual)
        else:
            if inicial.compare(alvo):
                return True
            else:
                inicial.estados += 1
                if procurar_matriz(inicial, alvo, linha_atual + 1):
                    return True
                else:
                    inicial.rotate(linha_atual)


if procurar_matriz(start, target, 0):
    for i in range(len(start.rotacoes)):
        if start.rotacoes[i] != 0:
            print('{0} rotacoes na linha {1}'.format(start.rotacoes[i], i + 1))

    print(start.estados)
else:
    print('Impossivel')
    print(start.estados)
