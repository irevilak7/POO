
def EsPrimo(pNum):
    lRes = False
    if pNum % 2 == 0: #Verifica si es par
        if pNum == 2:
            lRes = True
    else:
        lCont = 0;
        lLim = pNum // 2 + 1
        #print(lLim)
        #                [Inicio, Fin)
        for lIdx in range(2,      lLim + 1):
            #print(lIdx)
            if pNum % lIdx == 0:
                lCont += 1
                #lCont = lCont + 1
        if lCont == 0:
            lRes = True
    return lRes
# EsPrimo
#           (2, 3, 4, ... 50)   
for lNum in range(2, 51):
    if EsPrimo(lNum) == True:
        print(lNum, "Es primo")
print("-----")

lNum = 2
while lNum < 51:
    if EsPrimo(lNum) == True:
        print(lNum, "Es primo")
    lNum += 1
print("----")

lCont=1
lNum=1
while lCont <= 100:
    lNum += 1
    if EsPrimo(lNum) == True:
        print(lNum, "Es primo", lCont)
        lCont += 1

"""
if lNum % 2 == 0: #Verifica si es par
    if lNum == 2:
        print(lNum, "Es primo")
    else:
        print(lNum, "No es primo, por ser par")
else:
    lCont = 0;
    lLim = lNum // 2 + 1
    #print(lLim)
    #                [Inicio, Fin)
    for lIdx in range(2,      lLim + 1):
        #print(lIdx)
        if lNum % lIdx == 0:
            lCont += 1
            #lCont = lCont + 1
    if lCont == 0:
        print(lNum, "Es primo")
    else:
        print(lNum, "No es primo")
"""
