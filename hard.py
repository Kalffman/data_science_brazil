import numpy as np

print('\n#1- Calcule a pontuação softmax de ‘sepal length’:')
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

print(sepallength)
