class Matriz():
    matriz = []
    rotacoes = []

    def __init__(self,matriz):
        self.matriz = matriz
        for i in self.matriz:
            self.rotacoes.append(0)

    def __str__(self):
        return str(self.matriz)

    def add(self,linha,elemento):
        self.matriz[linha].append(elemento)

    def rotate(self,linha):
        self.matriz[linha].insert(0,self.matriz[linha][len(self.matriz[linha])-1])
        self.matriz[linha].pop(len(self.matriz[linha])-1)
        self.rotacoes[linha] += 1


