import garbled_circuit_func as func
import elgamal


def init(x_in):
    global public_keys, blood_type_index, x
    x = func.get_bits(x_in)

    public_keys = [[0] * 2] * 3

    blood_type_index = x

    for i in range(3):
        public_keys[i][x[i]] = elgamal.gen()
        public_keys[i][1 - x[i]] = elgamal.o_gen()


def get_public_keys():
    return public_keys


def set_values_from_bob(F_in, Y_in, d_in, ciphertexts):
    global F, d, e_x, e_y, e_xor
    F, d = F_in, d_in
    e_y, e_xor = Y_in
    e_x = decrypt(ciphertexts)


def test():
    Z = func.evaluate_circuit(F, e_x, e_y, e_xor)
    if Z == d[0]:
        return 0
    elif Z == d[1]:
        return 1


def decrypt(ciphertexts):
    e_x = []

    # TODO: This would be used to decrypt if OT worked.
    # for i in range(3):
    #     c1, c2 = ciphertexts[i][x[i]]
    #     dec = elgamal.decrypt(c1, c2)
    #     e_x.append(dec)

    # TODO: This is used because OT doesn't decrypt correctly.
    for i in range(3):
        e_x.append(ciphertexts[i][x[i]])

    return e_x
