from task_1 import parse_input
from collections import defaultdict


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
    result = []
    operation_value_pairs = parse_input(input)
    working_dictionary = defaultdict(int)
    for operation, value in operation_value_pairs:
        if operation == 1:
            working_dictionary[operation] += value
        elif operation == 2:
            if value in working_dictionary and working_dictionary[operation] > 0:
                working_dictionary[operation] += -1
        elif operation == 3:
            result.append(working_dictionary[value])
    return result


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
if __name__ == "__main__":
    assert check_frequency(_input) == [0, 0]
