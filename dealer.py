import random
import numpy as np

import alice
import bob


def __init():
    global s, r, truth_table, matrix_a, matrix_b, n_size

    # We work with bloodtypes, and there's 8 different ones, so to get 2**n = 8, n = 3.
    n_size = 3

    r = create_random_bit_string()
    s = create_random_bit_string()

    # Initialize matrix M_b \in {0,1}^(2^n x 2^n) uniformly random
    matrix_b = np.random.randint(2, size=(2 ** n_size, 2 ** n_size))

    # Initialize matrix M_a as a 2^n x 2^n matrix with zeroes
    matrix_a = np.zeros((2 ** n_size, 2 ** n_size)).astype(int)

    truth_table = __get_truth_table()

    for index, _ in np.ndenumerate(matrix_a):
        i = index[0]
        j = index[1]
        matrix_a[i, j] = __create_matrix_a(i, j, n_size, matrix_b[i, j])


def create_random_bit_string():
    """ Creates a string of random bits that is of length n. """
    final_bit_str = ""

    for i in range(n_size):
        temp = str(random.randint(0, 1))
        final_bit_str += temp

    return int(final_bit_str, 2)


def __create_matrix_a(i, j, n, matrix_b_index):
    """ Creates index M_A[i,j] as defined in the one-time-truth-table protocol. """
    return matrix_b_index ^ truth_table[(i - r) % (2 ** n), (j - s) % (2 ** n)]


def __get_truth_table():
    row_1 = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    row_2 = np.array([1, 1, 0, 0, 0, 0, 0, 0])
    row_3 = np.array([1, 0, 1, 0, 0, 0, 0, 0])
    row_4 = np.array([1, 1, 1, 1, 0, 0, 0, 0])
    row_5 = np.array([1, 0, 0, 0, 1, 0, 0, 0])
    row_6 = np.array([1, 1, 0, 0, 1, 1, 0, 0])
    row_7 = np.array([1, 0, 1, 0, 1, 0, 1, 0])
    row_8 = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    return np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8])


def init_alice(x):
    """ Returns (r, n, M_A). """
    alice.init(x, r, n_size, matrix_a)


def init_bob(y):
    """ Returns (s, n, M_B). """
    bob.init(y, s, n_size, matrix_b)
