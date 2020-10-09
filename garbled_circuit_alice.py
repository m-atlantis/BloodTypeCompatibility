import garbled_circuit_func as func
import elgamal


def init(x_in):
    global public_keys, blood_type_index, x
    x = func.get_bits(x_in)

    public_keys = [[0] * 2] * 3

    blood_type_index = x

    for i in range(3):
        for j in range(2):
            if j == x[i]:
                public_keys[i][j] = elgamal.gen()
            else:
                public_keys[i][j] = elgamal.o_gen()


def get_public_keys():
    return public_keys


def decrypt(ciphertexts):
    e_x = []

    for i in range(3):
        c1, c2 = ciphertexts[i][x[i]]
        dec = elgamal.decrypt(c1, c2)
        e_x.append(dec)

    return e_x
