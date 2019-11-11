"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""
import math
from numbers import Number



class Figure:

    def area(self, *args):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @staticmethod
    def check_instance(arg):
        try:
            if not isinstance(arg, Number):
                raise ValueError
        except ValueError:
            print('Argument musi być liczbą')


    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):
    def __init__(self, r):
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.check_instance(r)
        self.__r = r


    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @staticmethod
    def get_area(r):
        if isinstance(r, Number):
            return math.pi * r ** 2
        else:
            return None

    @staticmethod
    def get_perimeter(r):
        if isinstance(r, Number):
            return 2 * math.pi * r
        else:
            return None

class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @staticmethod
    def get_area(a, b):
        if isinstance([a, b], Number):
            return a * b
        else:
            return None

    @staticmethod
    def get_perimeter(a, b):
        if isinstance([a, b], Number):
            return 2 * (a + b)
        else:
            return None

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.check_instance(a)
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.check_instance(b)
        self.__b = b


class Diamond(Figure):

    def __init__(self, e, f):
        self.__e = e
        self.__f = f

    @property
    def area(self):
        return (self.e * self.f) / 2

    @property
    def perimeter(self):
        a = math.sqrt((self.e / 2) ** 2 + (self.f / 2) ** 2)
        return 4 * a

    @staticmethod
    def get_area(e, f):
        if isinstance([e,f], Number):
            return (e * f) / 2
        else:
            return None

    @staticmethod
    def get_perimeter(e, f):
        if isinstance([e,f], Number):
            a = math.sqrt((e / 2) ** 2 + (f / 2) ** 2)
            return 4 * a
        else:
            return None

    def are_diagonals_equal(self):
        return self.e == self.f

    def to_square(self):
        if self.are_diagonals_equal():
            return Square(self.e/math.sqrt(2))
        else:
            return None

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, e):
        self.check_instance(e)
        self.__e = e

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, f):
        self.check_instance(f)
        self.__f = f


class Square(Rectangle, Diamond):
    def __init__(self, a):
        Rectangle.__init__(self, a, a)
        self.__e = a*math.sqrt(2)
        self.__f = self.e

    @property
    def b(self):
        return super().b

    @property
    def a(self):
        return super().a

    @b.setter
    def b(self, b):
        super(Square, self.__class__).b.fset(self, b)
        super(Square, self.__class__).a.fset(self, b)
        super(Square, self.__class__).e.fset(self, b * math.sqrt(2))
        super(Square, self.__class__).f.fset(self, b * math.sqrt(2))

    @a.setter
    def a(self, a):
        super(Square, self.__class__).b.fset(self, a)
        super(Square, self.__class__).a.fset(self, a)
        super(Square, self.__class__).e.fset(self, a * math.sqrt(2))
        super(Square, self.__class__).f.fset(self, a * math.sqrt(2))

    @property
    def e(self):
        return Diamond.e

    @property
    def f(self):
        return Diamond.f

    @e.setter
    def e(self, e):
        super(Square, self.__class__).e.fset(self, e)
        super(Square, self.__class__).f.fset(self, e)
        super(Square, self.__class__).a.fset(self, e / math.sqrt(2))
        super(Square, self.__class__).b.fset(self, e / math.sqrt(2))

    @f.setter
    def f(self, f):
        super(Square, self.__class__).f.fset(self, f)
        super(Square, self.__class__).e.fset(self, f)
        super(Square, self.__class__).a.fset(self, f / math.sqrt(2))
        super(Square, self.__class__).b.fset(self, f / math.sqrt(2))

    @staticmethod
    def get_area(a):
        if isinstance(a, Number):
            return a ** 2
        else:
            return None

    @staticmethod
    def get_perimeter(a):
        if isinstance(a, Number):
            return 4 * a
        else:
            return None


if __name__ == '__main__':


    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'