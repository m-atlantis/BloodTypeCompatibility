import random


def init_g_p_q():
    """ Initializes the parameters g, p, q.
        The prime p will be set to a precalculated safe-prime,
        and q will be computed from this. """
    global g, p, q

    p = 365627
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
    """ Generates a public key given a secret key."""
    return int(pow(g, sk, p))


def o_gen():
    """ Generates a fake public key, that is indistinguishable from a real one. """
    # r = random.randint(2, (2 ** 2 * (p.bit_length()))) % p
    r = random.randint(1, p)
    o_h = pow(r, 2, p)
    return o_h


def create_sk():
    """ Generates a secret key. """
    sk = random.randint(1, q - 1)

    return sk


def encrypt(m, pk):
    """ Encrypts the message using a given public key. """
    r = random.randint(1, q - 1)
    c1 = int(pow(g, r, p))
    c2 = int(m) * pow(pk, r, p)

    return c1, c2


def decrypt(c1, c2, sk):
    """ Decrypts a given ciphertext (c_1, c_2) using a given secret key. """
    mod_inv_c1 = pow(c1, p - 2, p)

    return int(c2) * pow(mod_inv_c1, sk) % p
