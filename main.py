from matriz import Matriz

z = [[3, 1, 2], [4, 5, 6], [8, 9, 7], [10, 11, 12]]
m = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


def procurar_matriz(inicial, alvo, linha_atual):
    for i in inicial.matriz[0]:
        if linha_atual == len(inicial.matriz) - 1:
            if inicial.compare(alvo):
                return True
            else:
                inicial.rotate(linha_atual)
        else:
            if procurar_matriz(inicial, alvo, linha_atual + 1):
                return True
            else:
                inicial.rotate(linha_atual)


