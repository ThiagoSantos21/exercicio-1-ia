import copy
from matriz import Matriz
z = [[1,2,3,4],[5,6,7,8],[10,11,12,9]]
m = Matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(m.rotacoes)

m.rotate(2)
if z == m.matriz:
    print('true')
else:
    print('false')
m.rotate(2)
if z == m.matriz:
    print('true')
else:
    print('false')
m.rotate(2)
if z == m.matriz:
    print('true')
else:
    print('false')



