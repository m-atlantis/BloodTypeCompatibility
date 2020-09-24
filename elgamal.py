import random


def create_g_p_q():
    global g, p, q
    p = None
    q = None

    primes = [i for i in range(3, 1000) if is_prime(i)]
    q = random.choice(primes)
    g = random.randint(2, q)

    p = 2 * q + 1
    while not is_prime(p):
        q = random.choice(primes)
        p = 2 * q + 1


def create_sk():
    global sk
    sk = random.randint(1, q)


def create_pk():
    global h
    h = pow(g, sk, p)
    print(h)


def gen():
    create_g_p_q()
    create_sk()
    create_pk()
    return h


def o_gen():
    global o_h
    # TODO: s should be random between 1 - p using random string r
    # TODO: pick number r between 1 - 2^(2n) and output (r mod p) = s
    # r = (# bits in p + 1) mod p

    r = random.randint(2, (2 ** 2 * (p.bit_length()))) % p
    print(r ** 2)
    # s = 1
    # o_h = mod_exp(s, 2, p)


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def encrypt(m):
    r = random.randint(2, q)

    c1 = pow(g, r, p)
    c2 = m * pow(h, r, p)

    return c1, c2


def decrypt(c1, c2):
    s = pow(c1, sk, p)

    return int(c2 / s)


gen()
o_gen()
c1, c2 = encrypt(111)
print(decrypt(c1, c2))
