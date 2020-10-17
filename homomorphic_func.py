import random


def key_gen():
    global p, q, r, y, n
    n = 10
    q, r, y = [0] * n, [0] * n, [0] * n

    p = random.getrandbits(512)

    for i in range(n):
        q[i] = random.getrandbits(512)  # Choose big ints
        r[i] = random.getrandbits(10)  # Choose small ints
        y[i] = p * q[i] + 2 * r[i]


def get_pk():
    return y


def get_sk():
    return p


def enc(m):
    # Choose random number of elements in y
    s = random.sample(y, random.randint(1, n))

    sum = 0
    for i in range(len(s)):
        sum += s[i]

    return m + sum


def dec(c):
    return (c % p) % 2


def evaluate(x, y, c1):
    level_4, level_3, level_2, level_1 = [0] * 3, [0] * 3, [0] * 3, [0]

    level_4[0] = xor_HE(y[2], c1[0])
    level_4[1] = xor_HE(y[1], c1[1])
    level_4[2] = xor_HE(y[0], c1[2])

    level_3[0] = and_HE(level_4[0], x[2])
    level_3[1] = and_HE(level_4[1], x[1])
    level_3[2] = and_HE(level_4[2], x[0])

    level_2[0] = xor_HE(level_3[0], c1[3])
    level_2[1] = xor_HE(level_3[1], c1[4])
    level_2[2] = xor_HE(level_3[2], c1[5])

    level_1 = and_HE(level_2[0], level_2[1])

    level_0 = and_HE(level_1, level_2[2])

    return level_0


def xor_HE(c1, c2):
    return c1 + c2


def and_HE(c1, c2):
    return c1 * c2


def get_bit(byte_val, idx):
    """ Returns bit on index 'idx' of integer bit-representation. """
    return (byte_val & (1 << idx)) != 0
