import random
import numpy as np
import hashlib


def get_bits(byte_in):
    tmp = []
    for i in range(3):
        tmp.insert(0, int((byte_in & (1 << i)) != 0))
    return tmp


def create_128_bit_string(bit=None):
    """ Creates a string of random bits that is of length n. """
    final_bit_str = ""

    for i in range(16):
        if bit is None:
            temp = str(random.randint(0, 1))
        else:
            temp = str(bit)
        final_bit_str += temp

    # return int(final_bit_str, 2)
    return final_bit_str


def garble_circuit(bit_string, circuit):
    F = []
    e_x = []
    e_y = []
    d = []

    F, e_x, e_y, d = None, None, None, None
    return F, e_x, e_y, d


def create_circuit_labels():
    left = [create_128_bit_string(), create_128_bit_string()]
    right = [create_128_bit_string(), create_128_bit_string()]
    c = [create_128_bit_string(), create_128_bit_string()]

    return left, right, c


def nand_gate(left, right, c):
    row_1 = np.array([left, right, c[1]])
    row_2 = np.array([left, right, c[1]])
    row_3 = np.array([left, right, c[1]])
    row_4 = np.array([left, right, c[0]])

    return np.array([row_1, row_2, row_3, row_4])


def hash(left_key, right_key, input):
    h = hashlib.shake_256()
    h.update(left_key)
    h.update(right_key)
    h.update(input)

    return h.hexdigest(32)


def enc_y(e_y, y_in):
    Y = e_y
    return Y


def enc_x(e_x, x):
    # TODO: 2-1-OT protocol
    e_x_0 = [0]
    e_x_1 = [1]
    X = [e_x_0, e_x_1]
    return X
