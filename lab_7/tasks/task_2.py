import numpy as np


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
    number_of_neighbors = np.zeros(shape=board.shape, dtype=np.uint8)
    number_of_neighbors[:, :-1] += board[:, 1:]  # neighbors to the right
    number_of_neighbors[:, 1:] += board[:, :-1]  # neighbors to the left
    number_of_neighbors[:-1, :] += board[1:, :]  # neighbors below
    number_of_neighbors[1:, :] += board[:-1, :]  # neighbors above
    number_of_neighbors[:-1, :-1] += board[1:, 1:]  # neighbors across down right
    number_of_neighbors[1:, 1:] += board[:-1, :-1]  # neighbors across top left
    number_of_neighbors[:-1, 1:] += board[1:, :-1]  # neighbors across down left
    number_of_neighbors[1:, :-1] += board[:-1, 1:]  # neighbors across top right
    return number_of_neighbors


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
    number_of_neighbors = calculate_neighbours(board)
    is_dead = board == False
    is_alive = board

    # rule 2
    become_alive = (number_of_neighbors == 3) & is_dead

    # rule 3 a)
    has_2_or_3_neighbors = (2 <= number_of_neighbors) & (number_of_neighbors <= 3)
    stay_alive = has_2_or_3_neighbors & is_alive

    return become_alive | stay_alive


if __name__ == "__main__":
    _board = np.array(
        [
            [False, False, False, True, False, True],
            [True, False, True, False, False, True],
            [True, True, False, True, True, True],
            [False, True, True, False, False, True],
            [False, False, False, True, False, False],
            [False, True, True, True, False, True],
        ]
    )
    assert (
        calculate_neighbours(_board)
        == np.array(
            [
                [1, 2, 2, 1, 3, 1],
                [2, 4, 3, 4, 6, 3],
                [3, 5, 5, 3, 4, 3],
                [3, 3, 4, 4, 5, 2],
                [2, 4, 6, 3, 4, 2],
                [1, 1, 3, 2, 3, 0],
            ]
        )
    ).all()
    assert (
        iterate(_board)
        == np.array(
            [
                [False, False, False, False, True, False],
                [True, False, True, False, False, True],
                [True, False, False, True, False, True],
                [True, True, False, False, False, True],
                [False, False, False, True, False, False],
                [False, False, True, True, True, False],
            ]
        )
    ).all()
