import numpy as np


def estimate_pi(n):
    """
    Returns estimated value of pi.

    Funkcja szacuje wartość pi metodą probabilistyczną.
    Wygenerujmy m punktów z obszaru [-1,1]^2. Niech k określa liczbę punktów
    odległych od punku (0,0) o nie więcej niż 1. Proporcja 4k/m
    powinna szacować wartość pi.
    (1pkt).

    :param n: Number of points to made estimation.
    :type xy: int
    :return: Estimated Pi value
    :rtype: float
    """
    x = np.random.random(size=(2, n)) * 2 - 1
    return np.sum(np.sqrt(x[0] ** 2 + x[1] ** 2) < 1) / n * 4


if __name__ == "__main__":
    np.testing.assert_approx_equal(estimate_pi(int(1e2)), np.pi, 1)
    np.testing.assert_approx_equal(estimate_pi(int(1e3)), np.pi, 2)
