"""
19.- 
Genere 10 números aleatorios e insértelos en un arreglo. 
Para ellos calcule el promedio. 
En otro arreglo calcule la diferencia de cada número con su promedio. 
Ahora calcule la sumatoria del cuadrado de cada celda del segundo arreglo. 
A ese número divídalo entre 10 y obtenga su raíz cuadrada. 
Muestre la lista de números y su desviación estándar, 
que fue el número calculado.
"""


import random
import math

Nums = []
Sum = 0
for Idx in range (1, 11):
    #print(random.random())
    N = random.randrange(1, 101)
    #print(N)
    Nums.append(N)
    Sum += N
# for
print(Nums)
Prom = Sum/10
print('Sum: ', Sum)
print('Prom: ', Prom)

Dif = []
for N in Nums:
    Dif.append(N - Prom)
print(Dif)

Sum2 = 0
for D in Dif:
    Sum2 += D*D
print('Sum2: ', Sum2)

DS = math.sqrt(Sum2/10)
print('DS: ', DS)

    
    








