import numpy as np

lShape = (3,4)
lMat= np.zeros(lShape, dtype='i')
print(lMat)
print(lMat.shape)

print("-----")

lArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(lArr)
lMat = lArr.reshape(4, 3) #.copy()
print(lMat)
lArr[1] = 20
print(lArr)
print(lMat)

print("--")

lMat = lArr.reshape(2, 3, 2) #.copy()
print(lMat)

print("--")

lMat = lArr.reshape(2, 2, -1) #.copy()
print(lMat)

print("-----")

lArr01 = np.array((1, 2, 3))
lArr02 = np.array((4, 5, 6))

lArr = np.concatenate( (lArr01, lArr02) )

print(lArr)

print("--")

lArr = np.stack( (lArr01, lArr02) )

print(lArr)

print("--")

lArr = np.hstack( (lArr01, lArr02) )

print(lArr)

print("--")

lArr = np.vstack( (lArr01, lArr02) )

print(lArr)

print("--")

lArr = np.dstack( (lArr01, lArr02) )

print(lArr)

print("-----")

lArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(lArr)

lAs = np.array_split(lArr, 3)
print(lAs)

print("-----")

lArr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(lArr)

lAs = np.array_split(lArr, 3)
print(lAs)

print("-----")

#                0  1  2  3  4  5  6  
lArr = np.array([1, 2, 3, 4, 5, 4, 4])
print(lArr)

lPos = np.where(lArr == 4)
print(lPos)

for lP in lPos[0]:
    print(lP, lArr[lP])

print("-----")

lArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(lArr)

lPos = np.where(lArr % 2 == 0)
print(lPos)

print("-----")

lArr = np.array([45, 3, -1, 34, 10, 1, 5, 20])
print(lArr)

lSorted = np.sort(lArr)
print(lSorted)

print("--")

lArr = np.array([[45, 3, 1, 34], [10, -1, 5, 20]])
print(lArr)

lSorted = np.sort(lArr)
print(lSorted)

print("-----")

lArr = np.array([45, 3, -1, 34])
print(lArr)

lMask = [True, False, True, False]

lNArr = lArr[lMask]
print(lNArr)

print("--")

lArr = np.array([45, 3, -1, 34])
print(lArr)

lMask = []

for lNum in lArr:
    if (lNum > 10):
        lMask.append(True)
    else:
        lMask.append(False)
# for
print(lMask)

lNArr = lArr[lMask]
print(lNArr)

print("--")

lArr = np.array([45, 3, -1, 34])
print(lArr)

lMask = lArr > 0
print(lMask)

lNArr = lArr[lMask]
print(lNArr)


