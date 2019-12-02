import numpy as np


def generate_neighbours_boards(board):
    shape = board.shape
    false_column = np.zeros((shape[0], 1), dtype=bool)
    false_row = np.zeros((1, shape[1]), dtype=bool)
    vectorized_board = board

    left_neighbours = np.delete(vectorized_board, -1, axis=1)
    left_neighbours = np.hstack((false_column, left_neighbours))

    right_neighbours = np.delete(vectorized_board, 0, axis=1)
    right_neighbours = np.hstack((right_neighbours, false_column))

    up_neighbours = np.delete(vectorized_board, -1, axis=0)
    up_neighbours = np.vstack((false_row, up_neighbours))

    down_neighbours = np.delete(vectorized_board, 0, axis=0)
    down_neighbours = np.vstack((down_neighbours, false_row))

    up_left_neighbours = np.delete(up_neighbours, -1, axis=1)
    up_left_neighbours = np.hstack((false_column, up_left_neighbours))

    up_right_neighbours = np.delete(up_neighbours, 0, axis=1)
    up_right_neighbours = np.hstack((up_right_neighbours, false_column))

    down_left_neighbours = np.delete(down_neighbours, -1, axis=1)
    down_left_neighbours = np.hstack((false_column, down_left_neighbours))

    down_right_neighbours = np.delete(down_neighbours, 0, axis=1)
    down_right_neighbours = np.hstack((down_right_neighbours, false_column))

    return up_neighbours, up_right_neighbours, right_neighbours, down_right_neighbours, down_neighbours, down_left_neighbours, left_neighbours, up_left_neighbours


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """

    neighbours_board = np.zeros(board.shape)

    list_neighbours_boards = generate_neighbours_boards(board.astype(bool))
    for neighbours in list_neighbours_boards:
        neighbours_board[neighbours] += 1

    return neighbours_board


def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """

    neighbours_board = calculate_neighbours(board.astype(bool))

    life_cells = board
    life_cells[np.where(neighbours_board < 2)] = False
    life_cells[np.where(neighbours_board > 3)] = False

    dead_cells = board
    dead_cells[np.where(neighbours_board == 3)] = True

    return np.logical_and(life_cells, dead_cells)


if __name__ == '__main__':
    _board = np.array([
        [False, False, False, True, False, True],
        [True, False, True, False, False, True],
        [True, True, False, True, True, True],
        [False, True, True, False, False, True],
        [False, False, False, True, False, False],
        [False, True, True, True, False, True]
    ])
    _board2 = np.zeros(_board.shape)
    _board2[_board] = 1

    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1, ],
        [2, 4, 3, 4, 6, 3, ],
        [3, 5, 5, 3, 4, 3, ],
        [3, 3, 4, 4, 5, 2, ],
        [2, 4, 6, 3, 4, 2, ],
        [1, 1, 3, 2, 3, 0, ],
    ])).all()
    assert (iterate(_board) == np.array([
        [False, False, False, False, True, False],
        [True, False, True, False, False, True],
        [True, False, False, True, False, True],
        [True, True, False, False, False, True],
        [False, False, False, True, False, False],
        [False, False, True, True, True, False],
    ])).all()
