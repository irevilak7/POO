"""
01.- Generar 10 números aleatorios y obtener el menor de ellos.
"""

import random

Min = 2
for N in range (1, 11):
    Num = random.random()
    print(Num)
    if Num < Min:
        Min = Num
#for
print("------")
print(Min)

Min = 100
for N in range (1, 11):
    Num = random.randrange(20, 101)
    print(Num)
    if Num < Min:
        Min = Num
#for
print("------")
print(Min)








