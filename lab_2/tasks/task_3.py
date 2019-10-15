def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """
    response_dict = {}
    for value in values:
        response_dict[value] = 1

    return [*response_dict]


if __name__ == "__main__":
    assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])