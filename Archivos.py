
import os

Ruta = "C://temp/POO/Prueba.txt"

if os.path.exists(Ruta):    
    Arch = open(Ruta, "rt")
    # r = read
    # w = write
    # x = create, error si existe
    # a = append
    # t = text
    # b = binary
    
    #print(Arch.read())
    #print(Arch.readline())
    #print("---")
    #print(Arch.readline())
    for Linea in Arch:
        print(Linea.strip())
    Arch.close()

print("---")

Arch = open(Ruta, "at")
Arch.write("Escribo desde Python\r")
Arch.close()

print("---")

Arch = open(Ruta, "rt")
print(Arch.read())
Arch.close()

print("---")

os.remove(Ruta)


#####
#Arch = open("C://temp/POO/PruebaII.txt", "rt")
#for Linea in Arch:
#    if len(Linea) > 0:
#        Codigo = Linea.strip()
#        print(Codigo)
#        if len(Codigo) > 0:
#            eval(Codigo)
#Arch.close()




