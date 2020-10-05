
a = 4

b = 4

if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual a b")
    
a = 5

print("A") if a > b else print("B")

# (a > b ? "A" : "B")

c = 7

if a > b and b < c:
    print("algo")

print("------")

i = 1
while i < 11:
    print(i*2)
    i += 1

print("----")
    
# do - while
    
i = 1
while True:
    print(i*2)
    i += 1
    if i > 10:
        break
    
print("------")

Frutas = ["manzana", "naranja", "sandia"]
for F in Frutas:
    #print(F)
    if F == "naranja":
        continue
    print(F)
    print("Algo")

print("------")

for i in range(1, 11, 3):
    print(i)

#000
#999















