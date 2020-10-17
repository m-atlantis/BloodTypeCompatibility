from homomorphic_func import enc, get_bit, evaluate


def init(y):
    global encrypted_y, encrypted_1s
    encrypted_y, encrypted_1s = [], []

    for i in range(6):
        encrypted_1s.append(enc(1))

    for i in range(3):
        encrypted_y.append(enc(get_bit(y, 2 - i)))


def set_encrypted_x(x):
    global encrypted_x
    encrypted_x = x


def get_eval_output():
    return evaluate(encrypted_x, encrypted_y, encrypted_1s)
