import random
import numpy as np
from garbled_circuit_extra_func import *


def xor_gate(labels_a, labels_b, labels_c):
    # row_1 = np.array(["b \ a", labels_a[0], labels_a[1]])
    # row_2 = np.array([labels_b[0], labels_c[1], labels_c[0]])
    # row_3 = np.array([labels_b[1], labels_c[1], labels_c[0]])

    c = []
    one_power_128_string = create_128_bit_string(0)


    c.append(string_xor(hash(labels_a[0], labels_b[1]), (labels_c[1] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[1]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[0], labels_b[0]), (labels_c[1] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[0]), (labels_c[0] + one_power_128_string)))

    # Shuffle the list
    random.shuffle(c)

    return c


def and_gate(labels_a, labels_b, labels_c):
    # row_1 = np.array(["b \ a", labels_a[0], labels_a[1]])
    # row_2 = np.array([labels_b[0], labels_c[1], labels_c[0]])
    # row_3 = np.array([labels_b[1], labels_c[1], labels_c[0]])

    c = []
    one_power_128_string = create_128_bit_string(0)

    c.append(string_xor(hash(labels_a[0], labels_b[0]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[0], labels_b[1]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[0]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[1]), (labels_c[1] + one_power_128_string)))

    # Shuffle the list
    random.shuffle(c)

    return c


def init_garbled_circuit(y):
    labels = [[""] * 2] * 23
    for i in range(23):
        labels[i] = create_labels_e()

    F = []

    F.append([xor_gate(labels[0], labels[1], labels[2])])
    F.append([and_gate(labels[2], labels[3], labels[4])])
    F.append([xor_gate(labels[4], labels[5], labels[6])])

    F.append([xor_gate(labels[7], labels[8], labels[9])])
    F.append([and_gate(labels[9], labels[10], labels[11])])
    F.append([xor_gate(labels[11], labels[12], labels[13])])

    F.append([and_gate(labels[6], labels[13], labels[14])])

    F.append([xor_gate(labels[15], labels[16], labels[17])])
    F.append([and_gate(labels[17], labels[18], labels[19])])
    F.append([xor_gate(labels[19], labels[20], labels[21])])

    F.append([and_gate(labels[14], labels[21], labels[22])])

    d = labels[22]

    e_x = [labels[3], labels[10], labels[18]]
    e_y = enc_y([labels[0], labels[7], labels[15]], y)
    e_xor = [labels[1], labels[8], labels[16], labels[5], labels[12], labels[20]]

    return F, e_x, e_y, e_xor, d


def create_labels_e():
    wire_0 = create_128_bit_string()
    wire_1 = create_128_bit_string()

    return [wire_0, wire_1]


def enc_y(e_y_labels, y_in):
    y_in_bits = get_bits(y_in)
    Y = []

    for i in range(3):
        Y.append(e_y_labels[i][y_in_bits[i]])

    return Y


def evaluate_gate(garbled_gate, l_a, r_b):
    one_power_128_string = create_128_bit_string(0)

    for i in range(4):
        k = string_xor(garbled_gate[i], hash(l_a, r_b))

        if k[16:] == one_power_128_string:
            return k[:16]

    raise Exception("No correct decryption found for the given keys.")
