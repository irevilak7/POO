
import numpy as np

arreglo = np.arange(27).reshape(3, 3, 3)
print(arreglo)
print(arreglo.ndim)
print(arreglo.shape)
print(arreglo.itemsize)
print(arreglo[2,0,2])

arreglo2 = np.arange(27).reshape(3,3,3)

suma=arreglo*arreglo2
print(suma)

arr = [1, 2, 3]
arr2 = [1, 2, 3]
arrsuma = arr + arr2
print(arrsuma)





