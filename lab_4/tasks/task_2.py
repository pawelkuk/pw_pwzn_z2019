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
import math


class Vector:

    @property
    def dim(self):
        return self._dim  # Wymiar vectora

    def __init__(self, *args):
        self.components = args
        self._dim = len(args)

    def __add__(self, vector):
        t = (i + j for i,j in zip(self.components, vector.components))
        return Vector(*t)
    
    def __str__(self):
        return f'Vector{self.components}'
    
    def __eq__(self, vector):
        flags = [True for i, j in zip(self.components, vector.components) if i != j]
        return not bool(flags)

    def __sub__(self, vector):
        t = (i - j for i,j in zip(self.components, vector.components))
        return Vector(*t)
    
    def __mul__(self, val):
        if isinstance(val, Vector):
            return sum(i * j for i, j in zip(self.components, val.components))
        else:
            return Vector(*(i * val for i in self.components))

    def __len__(self):
        return int(math.sqrt(sum(i**2 for i in self.components)))
        

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
        return tuple(j - i for i, j in zip(beg, end))

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
        return Vector(*Vector.calculate_vector(beg, end))


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
