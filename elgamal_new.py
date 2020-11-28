import random


def init_g_p_q():
    global g, p, q
    # q = 455
    # p = 2 * q + 1

    # p = 2691467
    p = 365627
    # p = 405683
    q = int((p - 1) / 2)

    g_0 = get_generator()
    g = pow(g_0, 2, p)


def get_generator():
    """ Creates the generator g_0 of z_p^* using lemma 8.8 """
    generator = random.randint(1, p - 1)

    while int(pow(generator, ((p - 1) / q))) % p == 1:
        generator = random.randint(1, p - 1)

    return generator


def gen(sk):
    return int(pow(g, sk, p))


def o_gen():
    # r = random.randint(2, (2 ** 2 * (p.bit_length()))) % p
    r = random.randint(1, p)
    o_h = pow(r, 2, p)  # r ** 2 % p
    return o_h


def get_group_elements():
    init_g_p_q()
    group_elements = []

    for i in range(q):
        group_elements.append(pow(g, i, p))
    return group_elements


def create_sk():
    sk = random.randint(1, q - 1)

    return sk


def encrypt(m, pk):
    r = random.randint(1, q - 1)
    c1 = int(pow(g, r, p))
    c2 = int(m) * pow(pk, r, p)

    return c1, c2


def decrypt(c1, c2, sk):
    mod_inv_c1 = pow(c1, p - 2, p)

    return int(c2) * pow(mod_inv_c1, sk) % p


def test_elgamal():
    init_g_p_q()
    sk = create_sk()
    pk = gen(sk)

    e_x = [[123456, 123456], [0, 123456], [1, 123456]]
    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (encrypt(e_x[i][0], pk))
        encrypted_e_x[i][1] = (encrypt(e_x[i][1], pk))

    out = []
    x = [0, 0, 1]
    for i in range(3):
        c1, c2 = encrypted_e_x[i][x[i]]
        dec = decrypt(c1, c2, sk)
        out.append(dec)

    print(out)


def test_elgamal_bin():
    ''' Used for testing the El-Gamal encryptions on specific input. '''
    e_x = [['0011001011100111', '1001000000000110'], ['1010101001110110', '0111100001110011'],
           ['0011100011010101', '0010010110000000']]
    init_g_p_q()

    x = [1, 0, 0]
    sks = []
    pks = []
    for i in range(3):
        sk = create_sk()
        sks.append(sk)
        keys = [0, 0]

        keys[x[i]] = gen(sk)
        keys[1 - x[i]] = o_gen()

        pks.append(keys)

    print("PKs: ", pks)
    print("SKs: ", sks)
    # bin_val = int('1110110010000010', 2)
    # print("Expected value: " + str(bin_val))
    # c1, c2 = encrypt(bin_val, pk)
    # print("Got: " + str(decrypt(c1, c2, sk)))
    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]
    expected = []

    for i in range(3):
        encrypted_e_x[i][0] = (encrypt(int(e_x[i][0], 2), pks[i][0]))
        encrypted_e_x[i][1] = (encrypt(int(e_x[i][1], 2), pks[i][1]))

    out = []
    for i in range(3):
        c1, c2 = encrypted_e_x[i][x[i]]
        dec = decrypt(c1, c2, sks[i])
        out.append(dec)
        expected.append(int(e_x[i][x[i]], 2))

    print("Expected: " + str(expected))
    print("Got: ", out)

# test_elgamal_bin()
