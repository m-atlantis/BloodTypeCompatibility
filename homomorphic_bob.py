from homomorphic_func import enc, get_bit


def init(y):
    global encrypted_y
    encrypted_y = []

    for i in range(3):
        encrypted_y.append(enc(get_bit(y, 2 - i)))


def get_encrypted_y():
    return encrypted_y
