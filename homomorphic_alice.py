from homomorphic_func import enc, dec, get_bit, evaluate


def init(x):
    global encrypted_1s, encrypted_x
    encrypted_1s, encrypted_x = [], []

    for i in range(6):
        encrypted_1s.append(enc(1))

    for i in range(3):
        encrypted_x.append(enc(get_bit(x, 2 - i)))


def set_encrypted_y(y_in):
    global encrypted_y
    encrypted_y = y_in


def get_output():
    return dec(evaluate(encrypted_x, encrypted_y, encrypted_1s))
