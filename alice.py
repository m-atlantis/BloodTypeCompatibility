import dealer


def __init_variables():
    global x, r, n, matrix_a, u
    x = dealer.create_random_bit_string(n)
    r, n, matrix_a = dealer.to_alice()
    u = __compute_u()


def __compute_u():
    return x + r % 2 ** n


def send():
    """ Send (u) to Bob. """
    return u


def receive(var1, var2):
    global v, z_b
    v = var1
    z_b = var2


def output_z():
    """ Return z, which is the resulting bit. """
    # TODO: Make sure z is in {0,1}
    return matrix_a[u, v] ^ z_b
