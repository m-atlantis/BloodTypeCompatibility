import numpy as np
import elgamal


def init(y):
    global blood_type_index, encrypted_messages
    blood_type_index = y

    truth_table = __get_truth_table()
    encrypted_messages = []

    for i in range(8):
        encrypted_messages.append(elgamal.encrypt(truth_table[i][blood_type_index], public_keys[i]))


def set_public_keys(pk_in):
    global public_keys
    public_keys = pk_in


def get_encrypted_messages():
    return encrypted_messages


def __get_truth_table():
    row_1 = np.array([1, 2, 2, 2, 2, 2, 2, 2])
    row_2 = np.array([1, 1, 2, 2, 2, 2, 2, 2])
    row_3 = np.array([1, 2, 1, 2, 2, 2, 2, 2])
    row_4 = np.array([1, 1, 1, 1, 2, 2, 2, 2])
    row_5 = np.array([1, 2, 2, 2, 1, 2, 2, 2])
    row_6 = np.array([1, 1, 2, 2, 1, 1, 2, 2])
    row_7 = np.array([1, 2, 1, 2, 1, 2, 1, 2])
    row_8 = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    return np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8])
