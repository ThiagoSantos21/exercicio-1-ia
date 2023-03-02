#Thiago Santos - 21012009
#Kevin Silva - 21007836
#Elias Fausto - 21004040
from matriz import Matriz

estados = 0
target = [[3, 1, 2], [4, 5, 6], [8, 9, 7]]
start = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def procurar_matriz(inicial, alvo, linha_atual):
    for i in inicial.matriz[0]:
        if linha_atual == len(inicial.matriz) - 1:
            if inicial.compare(alvo):
                return True
            else:
                inicial.estados += 1
                inicial.rotate(linha_atual)

        else:
            if procurar_matriz(inicial, alvo, linha_atual + 1):
                return True
            else:
                inicial.rotate(linha_atual)


if procurar_matriz(start, target, 0):
    for i in range(len(start.rotacoes)):
        if start.rotacoes[i] != 0:
            print('{0} rotacoes na linha {1}'.format(start.rotacoes[i],i+1))

    print(start.estados)
else:
    print('Impossivel')
    print(start.estados)
