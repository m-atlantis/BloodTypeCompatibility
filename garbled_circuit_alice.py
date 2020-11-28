import garbled_circuit_func as func
import elgamal_new as elgamal


def init(x_in):
    global public_keys, secret_keys, x
    x = func.get_bits(x_in)

    public_keys, secret_keys = [], []

    elgamal.init_g_p_q()
    for i in range(3):
        create_keys(i)


def create_keys(i):
    sk = elgamal.create_sk()
    secret_keys.append(sk)

    keys = [0, 0]

    keys[x[i]] = elgamal.gen(sk)
    keys[1 - x[i]] = elgamal.o_gen()

    public_keys.append(keys)


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

    for i in range(3):
        c1, c2 = ciphertexts[i][x[i]]
        dec = elgamal.decrypt(c1, c2, secret_keys[i])
        e_x.append(str(bin(dec))[2:].zfill(16))

    return e_x
