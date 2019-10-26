import math

"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


def check_dim(dim1, dim2):
    try:
        if dim1 is not dim2:
            raise ValueError
        return True
    except ValueError:
        print("Niezgodność wymiarów")


class Vector:

    def __init__(self, *args):
        self.vector = tuple(args)
        self._dim = len(self.vector)

    @property
    def dim(self):
        return self._dim

    def __eq__(self, other):
        return self.dim == other.dim and self.vector == other.vector

    def __add__(self, other):
        check_dim(self.dim, other.dim)
        response_vector = []
        for i in range(0, self.dim):
            response_vector.append(self.vector[i] + other.vector[i])

        return Vector(*response_vector)

    def __sub__(self, other):
        check_dim(self.dim, other.dim)
        response_vector = []
        for i in range(0, self.dim):
            response_vector.append(self.vector[i] - other.vector[i])

        return Vector(*response_vector)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            response_vector = [element * other for element in self.vector]
            return Vector(*response_vector)
        else :
            check_dim(self.dim, other.dim)
            response_int = 0
            for i in range(0, self.dim):
                response_int += self.vector[i]*other.vector[i]
            return response_int

    def __len__(self):
        response_len = 0.0
        for element in self.vector:
            response_len += element**2

        return int(math.sqrt(response_len))




    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        check_dim(len(beg), len(end))
        response_points_list = []
        for i in range(0, len(beg)):
            response_points_list.append(end[i] - beg[i])

        return tuple(response_points_list)




    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.
    
        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        vector = cls.calculate_vector(beg, end)
        return Vector(*vector)



if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    assert v1 + v2 == Vector(2, 4, 6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    #Jak zrobić żeby len zwracało float??
    assert len(Vector(3,4)) == 5

    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
