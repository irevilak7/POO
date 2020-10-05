"""
14.- Dado el cálculo de Montecarlo, 
muestre el número de puntos que se 
situaron fuera de la circunferencia.
"""

import random

Max = 100000
Sum = 0
Sum2 = 0
for N in range (0, Max):
    X = random.random()
    Y = random.random()
    if X*X + Y*Y <= 1:
        Sum += 1
    else:
        Sum2 += 1
#for
print(Sum*4/Max)
print(Sum2)
print(Max - Sum)












