import random
import numpy as np


def __init(n):
    global s, r, truth_table, matrix_a, matrix_b, n_size
    # T[i,j] = f(i,j) and a truth table

    n_size = n

    r = create_random_bit_string(n)
    s = create_random_bit_string(n)

    # Initialize matrix M_b \in {0,1}^(2^n x 2^n) uniformly random
    matrix_b = np.random.randint(2, size=(2 ** n, 2 ** n))

    # Initialize matrix M_a as a 2^n x 2^n matrix with zeroes
    matrix_a = np.zeros((2 ** n, 2 ** n)).astype(int)

    # TODO: What should truth table be? Here it's just a full zeroes matrix
    truth_table = np.zeros((2 ** n, 2 ** n)).astype(int)

    for index, _ in np.ndenumerate(matrix_a):
        i = index[0]
        j = index[1]
        matrix_a[i, j] = __create_matrix_a(i, j, n, matrix_b[i, j])
        print(matrix_a[i, j])


def create_random_bit_string(n):
    """ Creates a string of random bits that is of length n. """
    final_bit_str = ""

    for i in range(n):
        temp = str(random.randint(0, 1))
        final_bit_str += temp

    return int(final_bit_str, 2)


def __create_matrix_a(i, j, n, matrix_b_index):
    """ Creates index M_A[i,j] as defined in the one-time-truth-table protocol. """
    return matrix_b_index ^ truth_table[i - r % (2 ** n), j - s % (2 ** n)]


# TODO: Make it so that Alice and Bob can't call each others functions, like make function random_matrix_a(),
#  random_matrix_b().
def to_alice():
    """ Returns (r, n, M_A). """
    return r, n_size, matrix_a


def to_bob():
    """ Returns (s, n, M_B). """
    return s, n_size, matrix_b

