import random
import numpy


def create_g_p_q():
    global g, p, q
    p = None
    q = None
    random_bits = random.randint(pow(10, 20), pow(10, 50))

    # while p == None or not is_prime(p):
    #     q = random.randint(pow(10, 20), pow(10, 50))
    #     p = q.multiply(new
    #     BigInteger("2")).add(BigInteger.ONE)

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    # TODO: Check that p is prime
    p = 2 * q + 1


def create_sk():
    global sk
    sk = random.randint(pow(10, 20), q)
    while gcd(sk, q) != 1:
        sk = random.randint(pow(10, 20), q)


def create_pk():
    global h
    h = mod_exp(g, sk, p)


def create_r():
    r = random.randint(pow(10, 20), q)
    while gcd(r, q) != 1:
        r = random.randint(pow(10, 20), q)
    return r


def gen():
    create_g_p_q()
    create_sk()
    create_pk()
    return h


def o_gen(r):
    global o_h
    # TODO: s should be random between 1 - p using random string r
    # TODO: pick number r between 1 - 2^(2n) and output (r mod p) = s
    s = 1
    o_h = mod_exp(s, 2, p)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def mod_exp(base, exp, modulus):
    # return pow(base, exp, modulus)
    x = 1
    y = base

    while exp > 0:
        if exp % 2 == 0:
            x = (x * y) % modulus
        y = (y * y) % modulus
        exp = int(exp / 2)

    return x % modulus


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def encrypt(m):
    r = create_r()

    c1 = mod_exp(g, r, p)
    c2 = m * mod_exp(h, r, p)

    return c1, c2


def decrypt(c1, c2):
    s = mod_exp(c1, sk, p)

    return int(c2 / s)


gen()
c1, c2 = encrypt(3)
print(decrypt(c1, c2))
