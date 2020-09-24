import random


def create_g_p_q():
    global g, p, q
    p = None
    q = None

    primes = [i for i in range(1, 1000) if is_prime(i)]
    q = random.choice(primes)
    g = random.randint(2, q)

    p = 2 * q + 1
    while not is_prime(p):
        q = random.choice(primes)
        p = 2 * q + 1


def create_sk():
    global sk
    sk = random.randint(1, q)
    while gcd(sk, q) != 1:
        sk = random.randint(1, q)


def create_pk():
    global h
    h = mod_exp(g, sk, p)


def create_r():
    r = random.randint(1, q)
    while gcd(r, q) != 1:
        r = random.randint(1, q)
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
    return pow(base, exp, modulus)


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
