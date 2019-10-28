"""
Część 1 (1 pkt): Uzupełnij klasę Calculator
tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (memory, atrybut klasy) z interfejsem: dodaj do pamięci , wyczyść pamięć.
Atrybut memory ma być nienadpisywalny.
Część 2 (1 pkt): jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obsłuż przypadki skrajne.
"""


def check_arg2(dim1, dim2):
    try:
        if dim1 is not dim2:
            raise ValueError
        return True
    except ValueError:
        print("Niezgodność wymiarów")


class Calculator:
    def __init__(self):
        self._memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji, tak by metoda memorize przypisywała
        # wynik zapisany w tym atrybucie

        # short_memory uzywamy gdy uzytokonik nie podał argunetu i wykonujemy
        # operacje z poprzednią wartością
        # zasze zapamietuje ostatni wynik
        self._short_memory = None
        self.operations_dict = {'+': self.__add__, '-': self.__sub__, '*': self.__mul__, '/': self.__divmod__}

    def __add__(self, arg1, arg2):
        return arg1 + arg2

    def __sub__(self, arg1, arg2):
        return arg1 - arg2

    def __divmod__(self, arg1, arg2):
        return arg1 / arg2

    def __mul__(self, arg1, arg2):
        return arg1 * arg2

    def run(self, operator, arg1, arg2=None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """

        try:
            if not self.operations_dict.get(operator):
                raise ValueError
            elif arg2 is None and self._short_memory is None:
                raise ValueError
            elif arg2 is None:
                arg2 = self._short_memory
            elif operator == '/' and not arg2:
                raise ValueError

            self._short_memory = self.operations_dict.get(operator)(arg1, arg2)
            return self._short_memory

        except ValueError:
            print("Nie można wykonać diałania ")

    def memorize(self):
        self._memory = self._short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._memory = None

    def in_memory(self):
        """Prints memorized value."""
        print(f"Zapamiętana wartość: {self._memory}")


if __name__ == '__main__':
    calc = Calculator()
    calc.memorize()
    calc.in_memory()
    calc.run('*', 0, 1)
    c = calc.run('/', 9)
    assert c == 3
