class Complex(object):
    def __init__(self, coefc):
        if type(coefc) == str:
            self.real, self.imaginary = tuple(map(float, coefc.split()))
        else:
            self.real, self.imaginary = coefc

    def __add__(self, other):
        return Complex((self.real + other.real, self.imaginary + other.imaginary))

    def __sub__(self, other):
        return Complex((self.real - other.real,self.imaginary - other.imaginary))

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        image = self.real * other.imaginary - other.real * self.imaginary
        return Complex((real, image))

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / \
               (other.real ** 2 + other.imaginary ** 2)
        image = (self.imaginary * other.real - self.real * other.imaginary) / \
                (other.real ** 2 + other.imaginary ** 2)
        return Complex((real, image))

    def __abs__(self):
        return Complex(((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0))

    def __str__(self):
        if self.imaginary >= 0:
            sign = '+'
        else:
            sign = ''
        return \
            f"{format(self.real, '.2f')}{sign}{format(self.imaginary, '.2f')}i"


if __name__ == '__main__':
    a = Complex(input())
    b = Complex(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(abs(a))
    print(abs(b))
