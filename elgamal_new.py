import random


def init_g_p_q():
    global g, p, q
    # q = 455
    # p = 2 * q + 1

    p = 2691467
    q = int((p - 1) / 2)

    g_0 = get_generator()
    g = g_0 ** 2 % p


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
    o_h = r ** 2 % p
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
    c2 = m * pow(pk, r, p)

    return c1, c2


def decrypt(c1, c2, sk):
    mod_inv_c1 = pow(c1, p - 2, p)

    return int(c2) * pow(mod_inv_c1, sk) % p


# init_g_p_q()
# sk = create_sk()
# pk = gen(sk)
# bin_val = int('1110110010000010', 2)
# print("Expected value: " + str(bin_val))
# c1, c2 = encrypt(bin_val, pk)
# print("Got: " + str(decrypt(c1, c2, sk)))
