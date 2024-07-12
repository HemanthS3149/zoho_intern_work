class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs=coeffs

    def __call__(self,x):#call allows an instance of the class to be called as a function
        result=0
        #enumerate provides both index('power') and value ('coeff') of each coefficient
        for power,coeff in enumerate(self.coeffs):
            result+=coeff*(x**power)
        return result
p=Polynomial(1,0,-2,3)
print(p(10))