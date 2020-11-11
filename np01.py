
import numpy as np

lA0 = [1, 2, 3]
print(lA0)
print(type(lA0))

lArr = np.array(lA0)
print(lArr)
print(type(lArr))

lA1 = (1, 2, 3)
print(lA1)
print(type(lA1))

lArr = np.array(lA1)
print(lArr)
print(type(lArr))
print('Dim: ', lArr.ndim)

print("----")

lArr = np.array(2020)
print(lArr)
print('Dim: ', lArr.ndim)

print("----")

lArr = np.array( [ [1, 2, 3, 4, 5] , [6, 7, 8, 9, 10] ]  )
print(lArr)
print('Dim: ', lArr.ndim)

print("----")

lArr = np.array( [ ['1', '2', '3', '4', '5'] , ['6', '7', '8', '9', '10'] ]  )
print(lArr)
print('Dim: ', lArr.ndim)

print("----")

lArr = np.array([1, 2, 3, 4, 5])
print(lArr)
print(lArr[1])

print("----")

lArr = np.array( [ ['1', '2', '3', '4', '5'] , ['6', '7', '8', '9', '10'] ]  )
print(lArr)
print(lArr[1])
print(lArr[1, 1])

print("----")

#                0  1  2  3  4
lArr = np.array([1, 2, 3, 4, 5])
print(lArr)
print(lArr[1:3])
print(lArr[:3])
print(lArr[1:])
print(lArr[1::2])

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

print("----")

lArr = np.array([1, 2, 3, 4, 5])
print(lArr)
print(lArr.dtype)

lArr = np.array(['1', '2', '3', '4', '5'])
print(lArr)
print(lArr.dtype)

lArr = np.array([1, 2, 3, 4, 5], dtype='U')
print(lArr)
print(lArr.dtype)

lArr = np.array([1, 2, 3, 4, 5], dtype='i2')
print(lArr)
print(lArr.dtype)

print("----")

lArr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(lArr)
print(type(lArr))
print(lArr.dtype)

lNArr = lArr.astype('i')
print(lNArr)
print(type(lNArr))
print(lNArr.dtype)

lNArr = np.array(lArr, dtype='i')
print(lNArr)
print(type(lNArr))
print(lNArr.dtype)

print("----")

lArr = np.array([1, 2, 3, 4, 5])
print('Arr: ', lArr)

lNums = lArr
#lNums = lArr.view()
print('Nums: ', lNums)

lNums[0] = 100
print('Arr: ', lArr)
print('Nums: ', lNums)
print('Nums.base: ', lNums.base)

lNums = lArr.copy()
print('Nums: ', lNums)

lNums[0] = -100
print('Arr: ', lArr)
print('Nums: ', lNums)
print('Nums.base: ', lNums.base)

print("----")

lArr = np.array([1, 2, 3, 4, 5])

for lNum in lArr:
    print(lNum)

lArr = np.array([[1, 2, 3], [4, 5, 6]])

for lNum in lArr:
    print(lNum)

for lRow in lArr:
    for lNum in lRow:
        print(lNum)

"""
rnd [5,25]
a
|O..|
|...|
|...|

b
|O..|
|...|
|...|

c = a+b, a-b, a*b, a/b
|X..|
|...|
|...|
"""






