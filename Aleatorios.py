import random
max=10000000
cont=0
for loop in range(1, max):
    #print(random.randrange(1,11))
    x=random.random()
    y=random.random()
    #print(x,y)
    if x*x + y*y<= 1:
        cont+=1
print(cont)
print(cont/max * 4)
    
    
    
    
    