"""
20.- 
* Genere un procedimiento 
? recursivo 
que muestre los primeros n elementos 
* de la serie de Fibonacci.

1 1 2 3 5 8 13 ...
1 2 3
n3 = n2 + n1

nx = nx-1 + nx-2

L1 pN01 pN02 print pL pM
1   1    1    2    3  17
2   1    2    3    4  17
3   2    3    5    5  17
...

"""

def Fibo(pN01, pN02, pL, pM):
    if (pL < pM):
        lN03 = pN02 + pN01
        print(lN03)
        pL += 1
        Fibo(pN02, lN03, pL, pM)
# Fibo

print(1)
print(1)
Fibo(1, 1, 2, 17)












