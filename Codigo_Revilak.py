
#9
import random
lista=[]
suma=0;
mayor=0;
for i in range (1, 20):
    Nue = random.randrange(7, 38)
    lista.append(Nue)
    suma += Nue
print(lista)
prom=suma/19
if Nue>prom:
    Nue=mayor
print('Promedio de todos: ', prom)
print("mayor: ", mayor)
print("-----")
#10
Nume = int(input("Ingresa un numero: "))

while Nume != 1:
    if Nume % 2 == 0:
        print("%d," % (Nume), end = "")
        Nume = Nume / 2
    else:
        print("%d," % (Nume), end = "")
        Nume = (Nume * 3) + 1

    if Nume == 1:
        print("1")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    