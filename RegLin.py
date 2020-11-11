import matplotlib.pyplot as plt
from scipy import stats

x = [5,	7,	8,	7,	2,	17,	2,	9,	4,	11,	12,	9,	6]							
y = [99,	86,	87,	88,	111,	86,	103,	87,	94,	78,	77,	85,	86]
#y'= 98
#e =  1
#   m      b    
# pend, ord org, 
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept
# myfunc

# y = mx + b
print(slope, 'x ', intercept)
#print(r)
print('R^2= ', r*r)
#print(p)
#print(std_err)
print(3, myfunc(3))

lMap = map(myfunc, x)
mymodel = list(lMap)

print("----")
print(lMap)
print("----")
print(mymodel)
print("----")

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

