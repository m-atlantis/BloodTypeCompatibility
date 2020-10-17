from homomorphic_func import enc, dec, get_bit


def init(x):
    global encrypted_x
    encrypted_x = []

    for i in range(3):
        encrypted_x.append(enc(get_bit(x, 2 - i)))


def get_encrypted_x():
    return encrypted_x


def output(c):
    return dec(c)
