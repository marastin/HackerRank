import math

# Doc:
# https://diveintopython3.net/iterators.html#defining-classes

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    def __mul__(self, no):
        r1 = self.real
        r2 = no.real
        i1 = self.imaginary
        i2 = no.imaginary
        return Complex(r1*r2 - i1*i2, r1*i2 + r2*i1)

    def __truediv__(self, no):
        r1 = self.real
        r2 = no.real
        i1 = self.imaginary
        i2 = no.imaginary
        return(Complex((r1*r2 + i1*i2) / (r2**2 + i2**2), (i1*r2 - r1*i2) / (r2**2 + i2**2)))

    def mod(self):
        return(Complex(round(((self.real**2) + (self.imaginary**2))**0.5, 2), 0))
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')