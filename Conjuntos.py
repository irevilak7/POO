
Frutas = {"manzana", "naranja", "pi�a", "cereza"}
print(Frutas)

for F in Frutas:
    print(F)
    if "naranja" in Frutas:
        print("Naranja est�")
    else:
        print("Naranja no est�")
    
Frutas.add("ca�a")
print(Frutas)

Frutas.add("ca�a")
print(Frutas)

Frutas.update(["durazno", "nectarina"])
print(Frutas)

print(len(Frutas))

Frutas.remove("ca�a")
print(Frutas)

Frutas.discard("uva")
print(Frutas)

F = Frutas.pop()
print(F)
print(Frutas)

F = Frutas.pop()
print(F)
print('Frutas', Frutas)

#Frutas.clear()
#print(Frutas)

#del Frutas
#print(Frutas)

FrutasII = {"manzana", "durazno","pl�tano"}
print('FrutasII', FrutasII)

FIII = Frutas.union(FrutasII)
print('FIII', FIII)

FIV = Frutas.intersection(FrutasII)
print('FIV', FIV)

print("-----")

Autos = set( ("Vocho", "Ferrari", "AstonMartin") )
print(Autos)










