
"""
    Z  = X + Yi
    Z' = N L A
    
    N = math.sqrt(X**2 + Y**2)
    A = math.atan2(Y, X)
    
    X = math.cos(A) * N
    Y = math.sin(A) * N
"""
import math

class MyCplx:
    
    def __init__(self):
        self.__aX = 0
        self.__aY = 0
        self.__aN = 0
        self.__aA = 0
    # Constructor
    
    def _CalcPolar(self):
        self.__aN = math.sqrt(self.__aX ** 2 + self.__aY ** 2)
        self.__aA = math.atan2(self.__aY, self.__aX)
    # _CalcPolar
    
    def _CalcCarte(self):
        self.__aX = math.cos(self.__aA) * self.__aN
        self.__aY = math.sin(self.__aA) * self.__aN
    # _CalcPolar
    
    def limpia(self):
        self.__aX = 0
        self.__aY = 0
        self.__aN = 0
        self.__aA = 0
    # limpia
    
    @property
    def aX(self):
        return self.__aX
    # aX.getter
    
    @aX.setter
    def aX(self, pX):
        self.__aX = pX
        self._CalcPolar()
    # aX.setter
    
    @property
    def aY(self):
        return self.__aY
    # aX.getter
    
    @aY.setter
    def aY(self, pY):
        self.__aY = pY
        self._CalcPolar()
    # aX.setter
    
    @property
    def aN(self):
        return self.__aN
    # aN.getter
    
    @aN.setter
    def aN(self, pN):
        self.__aN = pN
        self._CalcCarte()
    # aX.setter
    
    @property # sale valor ->
    def aA(self):
        return self.__aA
    # aA.getter
    
    @aA.setter # entra valor <-
    def aA(self, pA):
        self.__aA = pA
        self._CalcCarte()
    # aA.setter

    def __repr__(self):
        return "{:.3f} {} {:.3f} i | {:.3f} L {:.3f}".format(
                self.__aX,
                "+" if self.__aY >= 0 else "",
                self.__aY,
                self.__aN,
                self.__aA)
    # __repr__

# MyCplx
    
    
lCplx = MyCplx()
lCplx.aX = 10
print(lCplx)
print("--")
lCplx.aY = 10
print(lCplx)
print("--")
lCplx.aN = lCplx.aN + 1
print(lCplx)
print("--")
lCplx.aA = lCplx.aA - 1.5
print(lCplx)

print("--")
lCplx.limpia()
lCplx.aN = 1
lAng = 0
while (lAng < math.pi/2):
    lCplx.aA = lAng
    print(lCplx)    
    lAng += 0.005























