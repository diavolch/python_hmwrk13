class SquareException(Exception):

    def __init__(self, message='Такой треугольник невозможен!'):
        self.message = message
        super().__init__(self.message)


class NegativeSideException(Exception):

    def __init__(self, message='Стороны не могут быть отрицательными!'):
        self.message = message
        super().__init__(self.message)


class Square:

    def __init__(self, a, b=None):
        if a < 0 or b < 0:
            raise NegativeSideException()
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self._a + other._a, self._b + other._b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other._a > self._b or other._b > self._b:
                raise SquareException()
            return Square(self._a - other._a, self._b - other._b)
        return NotImplemented

    def get_area(self):
        return self._a * self._b

    def get_perimetr(self):
        return 2*(self._a+self._b)

    def __repr__(self):
        return f"Square({self._a}, {self._b})"

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise NegativeSideException()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise NegativeSideException()

obj_a = Square(5,600)
print(obj_a)

