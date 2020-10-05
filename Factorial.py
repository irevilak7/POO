"""
Factorial =>
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!
n! = n*(n-1)!
0! = 1//se define
lNum=5
lProd=1
for lIdx in range(1, lNum + 1):
    // lIdx = 1, 2, 3, 4, 5
    lProd = lProd * lIdx
lIdx lProd
1     1
2     2
3     6
4     24
5     120
"""
def Fact(pN):
    if pN==0:
        return 1
    else:
        return pN*Fact(pN-1)
#Fact
"""
pN     pN*Fact(pN-1)
4       4*Fact(3)=6 -> 24
3       3*Fact(2)=2 -> 6
2       2*Fact(1)=1 -> 2
1       1*Fact(0)=1 -> 1
0       1
"""    
lNum=4
"""
lProd=1
for lIdx in range(1, lNum + 1):
    lProd = lProd * lIdx
print(lProd)
"""
print(Fact(lNum))