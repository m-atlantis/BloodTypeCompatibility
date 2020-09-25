import elgamal


def init(x):
    global public_keys, blood_type_index
    public_keys = []

    blood_type_index = x

    for i in range(8):
        if i == blood_type_index:
            public_keys.append(elgamal.gen())
        else:
            public_keys.append(elgamal.o_gen())


def get_public_keys():
    return public_keys


def decrypt(ciphertexts):
    c1, c2 = ciphertexts[blood_type_index]

    dec = elgamal.decrypt(c1, c2)
    if dec == 2:
        return False
    return dec
