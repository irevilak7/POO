
Ciudades = ["Tokyo", "NY", "Denver", "Florencia"]

print(Ciudades)
print(Ciudades[2])
print(Ciudades[-2])
print(Ciudades[1:3])
print(Ciudades[:3])
print(Ciudades[1:])

print("\n-----\n")

Ciudades[2] = "Boston"
print(Ciudades)

print("\n-----\n")

for lC in Ciudades:
    print(lC)
    
print("\n-----\n")

if "Lisboa" in Ciudades:
    print("Raquel está presente")
else:
    print("Raquel no está")

print("\n-----\n")

print(len(Ciudades))

print("\n-----\n")

Ciudades.append("Moscú")
print(Ciudades)

print("\n-----\n")

Ciudades.insert(1, "Berlín")
print(Ciudades)

print("\n-----\n")

Ciudades.remove("Florencia")
print(Ciudades)

print("\n-----\n")

del Ciudades[0]
print(Ciudades)

print("\n-----\n")

#del Ciudades

# ---------------------
#x = 1
#print(eval('x + 1'))
# ---------------------

print("\n-----\n")

Ciudades.clear()
print(Ciudades)

print("\n-----\n")

Ciudades = ["Tokyo", "NY", "Denver", "Florencia"]
Cs = Ciudades
print(Ciudades)
print(Cs)
Cs.append("Lisboa")
print(Ciudades)
print(Cs)

print("---")

Ciudades = ["Tokyo", "NY", "Denver", "Florencia"]
Cs = Ciudades.copy()
print(Ciudades)
print(Cs)
Cs.append("Lisboa")
print(Ciudades)
print(Cs)

print("\n-----\n")

Cs = list(Ciudades)
print(Cs)
Cs.append("Lisboa")
print(Ciudades)
print(Cs)

print("\n-----\n")

MC = Ciudades + Cs
print(MC)

print("\n-----\n")

Ciudades.extend(Cs)
print(Ciudades)
















