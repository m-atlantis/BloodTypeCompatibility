import garbled_circuit_func as func
import elgamal


def init(x_in):
    global public_keys, secret_keys, primes, generators, blood_type_index, x
    x = func.get_bits(x_in)

    # public_keys = [[0] * 2] * 3
    public_keys = []

    blood_type_index = x

    secret_keys, primes, generators = [], [], []
    for i in range(3):
        create_public_keys(i)


def create_public_keys(i):
    elgamal.init()

    sk, p, g = elgamal.get_values()
    secret_keys.append(sk)
    primes.append(p)
    generators.append(g)

    keys = [0, 0]
    keys[x[i]] = elgamal.gen()
    keys[1 - x[i]] = elgamal.o_gen()

    public_keys.append(keys)


def get_public_keys():
    return public_keys, generators, primes


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
    #     dec = elgamal.decrypt_for_garbled_circuit(c1, c2, secret_keys[i], primes[i])
    #     e_x.append(dec)
    # TODO: This is used because OT doesn't decrypt correctly.
    for i in range(3):
        e_x.append(ciphertexts[i][x[i]])

    return e_x

