
Frutas = {"manzana", "naranja", "piña", "cereza"}
print(Frutas)

for F in Frutas:
    print(F)
    if "naranja" in Frutas:
        print("Naranja está")
    else:
        print("Naranja no está")
    
Frutas.add("caña")
print(Frutas)

Frutas.add("caña")
print(Frutas)

Frutas.update(["durazno", "nectarina"])
print(Frutas)

print(len(Frutas))

Frutas.remove("caña")
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

FrutasII = {"manzana", "durazno","plátano"}
print('FrutasII', FrutasII)

FIII = Frutas.union(FrutasII)
print('FIII', FIII)

FIV = Frutas.intersection(FrutasII)
print('FIV', FIV)

print("-----")

Autos = set( ("Vocho", "Ferrari", "AstonMartin") )
print(Autos)










