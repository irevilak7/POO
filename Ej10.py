"""
10.- Genere e imprima un número aleatorio entre 2 y 10. 
El ciclo debe romper si es cinco. 
(Hágalo con do - while)
"""

import random

while True:
    Num = random.randrange(2, 10)
    print(Num)
    if Num == 5:
        break






