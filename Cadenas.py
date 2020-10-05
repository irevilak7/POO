
Programa = "Primos"
Comentario="""
asd asd
a sdasd
a sdasd
"""
print(Comentario)

Com2='''
asd asd
a sdasd
a sdasd
'''
print(Com2)

Cadena="Hola Mundo"
print(Cadena[1])
print(Cadena[5:8])
print(Cadena[5:])
print(len(Cadena))
Cadena="     Hola Mundo     "
print(Cadena)
print(Cadena.strip())
print(Cadena.upper())
print(Cadena.replace("o","0"))

Frutas="uvas, naranjas, manzanas, kiwis"
print(Frutas.split(","))

print("manzana" in Frutas)
print("coco" not in Frutas)

print(Cadena + "; " + Frutas)
print(Cadena, "; ", Frutas)

Cuantos=5

print(Cadena + str(Cuantos))

Cadena= "    Hola Mundo    {}"
print(Cadena.format(Cuantos))

print("    Hola Mundo    {}".format(Cuantos))
print(f"    Hola Mundo    {Cuantos}")

a=1
b=2
c=3

print("El valor de a es {}, el de b es {} y el de c es {}".format(a,b,c))
print("El valor de c es {2}, el de b es {1} y el de aes {0}".format(a,b,c))

print("El caballo de Don Quijote se llmaba \"Rosinante\"")

for letra in Cadena:
    print(letra)
    
lIdx=0
lLen=len(Cadena)
while lIdx < lLen:
    print(Cadena[lIdx])
    lIdx += 1
    
"""
Palindrome:
    anita lava la tina
    oxxo
    ojo
    somos o no somos
    isaac no ronca asi
    yo hago yoga hoy
"""

print("Ingrese la palabra")
palabra=input()
palabra=(palabra.lower())
palindrome=(palabra.replace("",""))
new=palindrome[::-1]
if(new==palindrome):
    print("Es palindrome")
else:
    print("No es palindrome")













