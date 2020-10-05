"""
    # Primo: divisible entre 1 y sí mismo.
    7
    X ? ? ?
    1 2 3 4 5 6 7
    lim =  int(n/2) + 1
    lim =  int(3.5) + 1 = 3 + 1 = 4
             X
          _____
    lIdx | lNum
             R   
    Si R == 0: Que lIdx es factor de lNum

"""
lNum = 3

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
