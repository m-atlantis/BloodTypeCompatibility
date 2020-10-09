import random
import numpy as np
from garbled_circuit_extra_func import *


def garble_circuit():
    F = []
    e_x = []
    e_y = []
    d = []

    labels = [[""] * 2] * 23
    for i in range(23):
        labels[i] = create_labels_e()

    F, e_x, e_y, d = None, None, None, None
    return F, [e_x, e_y], d


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


def circuit(x, y, g):
    labels = [[""] * 2] * 23
    for i in range(23):
        labels[i] = create_labels_e()

    eval_of_current_gate = evaluate_gate(g[i], x[i], y[i])
    if i == len(g):
        return eval_of_current_gate

    # TODO:
    # if g is XOR
    # return circuit(eval_of_current_gate, evaluate_gate(g[i + 1], eval_of_current_gate, y[i + 1]), i, g)

    return circuit(eval_of_current_gate, evaluate_gate(g[i + 1], eval_of_current_gate, y[i + 1]), i, g)


def create_labels_e():
    wire_0 = create_128_bit_string()
    wire_1 = create_128_bit_string()

    return [wire_0, wire_1]


def enc_y(e_y, y_in):
    Y = e_y
    return Y


def evaluate_gate(garbled_gate, l_a, r_b):
    one_power_128_string = create_128_bit_string(0)

    for i in range(4):
        k = string_xor(garbled_gate[i], hash(l_a, r_b))

        if k[16:] == one_power_128_string:
            return k[:16]

    raise Exception("No correct decryption found for the given keys.")
