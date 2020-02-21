# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата

class Complex:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        if self.real != 0:
            return f'{self.real} + {self.imaginary}i' if self.imaginary != 0 else str(self.real)
        else:
            return f'{self.imaginary}i' if self.imaginary != 0 else str(self.real)

print(Complex(3) + Complex(2, 3))
print(Complex(3) * Complex(4))
print(Complex(0, 1) * Complex(0, 1))
print(Complex(1, 1) * Complex(2, 2))
