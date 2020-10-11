import random


def create_g_p_q():
    global g, p, q
    p = None
    q = None

    primes = [i for i in range(300, 1400) if is_prime(i)]
    q = random.choice(primes)

    p = 2 * q + 1
    while not is_prime(p):
        q = random.choice(primes)
        p = 2 * q + 1
    g = random.randrange(1, p)


def create_sk():
    global sk
    sk = random.randint(1, q)


def create_pk():
    set_h(pow(g, sk, p))
    # print(h)


def set_h(h_in):
    global h
    h = h_in


def get_values():
    return sk, p, g


def init():
    create_g_p_q()
    create_sk()
    create_pk()


def gen():
    return h


def o_gen():
    global o_h

    r = random.randint(2, (2 ** 2 * (p.bit_length()))) % p
    o_h = r ** 2 % p
    return o_h


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def encrypt(m, pk):
    r = random.randint(2, q)

    c1 = pow(g, r, p)
    c2 = m * pow(pk, r, p)

    return c1, c2


def encrypt_for_garbled_circuits(m, pk, prime, generator):
    new_q = (prime - 1) / 2
    r = random.randint(2, new_q)
    c1 = pow(generator, r, prime)
    c2 = m * pow(pk, r, prime)

    return c1, c2


def decrypt(c1, c2):
    s = pow(c1, sk, p)
    inv = pow(s, p - 2, p)
    return c2 * inv % p


def decrypt_for_garbled_circuit(c1, c2, secret_key, prime_p):
    s = pow(c1, secret_key, prime_p)
    inv = pow(s, prime_p - 2, prime_p)
    return int(c2) * inv % prime_p
