class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        product = 1
        i = 0
       
        while i in range(abs(n)):
            product *= x
            i +=  1
            
        if n > 0:
            return product
        if n <  0:
            print (1 / product)
            return 1/product
