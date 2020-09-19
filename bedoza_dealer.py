import random


def init():
    randomness_a = [[0] * 3] * 5
    randomness_b = [[0] * 3] * 5

    for i in range(5):
        u = random.getrandbits(1)
        uA = random.getrandbits(1)
        uB = u ^ uA

        v = random.getrandbits(1)
        vA = random.getrandbits(1)
        vB = v ^ vA

        w = u & v
        wA = random.getrandbits(1)
        wB = w ^ wA

        randomness_a[i][0] = uA
        randomness_b[i][0] = uB
        randomness_a[i][1] = vA
        randomness_b[i][1] = vB
        randomness_a[i][2] = wA
        randomness_b[i][2] = wB
    return randomness_a, randomness_b
