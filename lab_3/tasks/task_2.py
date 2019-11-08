from __future__ import absolute_import

from collections import Counter
from task_1 import parse_input


def check_frequency(input):
    
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    response_dict = Counter()
    response_list = []
    query_list = parse_input(input)
    for query in query_list:
        if query[0] == 1:
            response_dict[query[1]] += 1
        elif query[0] == 2 and response_dict[query[1]]:
            response_dict[query[1]] -= 1
        elif query[0] == 3:
            if response_dict.get(query[1]):
                response_list.append(response_dict[query[1]])
            else:
                response_list.append(0)

    return response_list


_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 2


"""

# w assercie zmieniłam odp. na [0, 0], gryzie mi się Pana odpowiedź z poleceniem, jesli moja interpretacja jest zła, to przepraszam.
if __name__ == '__main__':
    assert check_frequency(_input) == [0, 0]
