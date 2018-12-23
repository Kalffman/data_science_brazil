import numpy as np


def impares_negativos(array):
    copy = array.copy()
    copy[copy % 2 != 0] = -1
    return copy


print('\n# 1- Substitua todos os números ímpares em arr com -1 sem alterar arr')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(impares_negativos(arr))

print(arr)

print('\n# 2- Converta uma matriz 1D para uma matriz 2D com 2 linhas:')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr.reshape((2, -1)))

print('\n# 3- Empilhe matrizes verticalmente:')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
concat = np.vstack((a, b))
print(concat)

print('\n# 4- Empilhe as matrizes horizontalmente:')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
concat = np.hstack((a, b))
print(concat)

print('\n# 5- Crie o seguinte padrão sem codificação, usando apenas funções numpy e a matriz de entrada abaixo ‘a’')
a = np.array([1, 2, 3])
a1 = np.repeat(a, len(a))
a2 = np.tile(a, len(a))
print(np.hstack((a1, a2)))


