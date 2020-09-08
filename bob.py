import dealer


def __init_variables():
    global y, s, n, matrix_b
    y = dealer.create_random_bit_string(n)
    s, n, matrix_b = dealer.to_bob()


def __compute_v():
    return y + s % 2 ** n


def receive(var):
    """ Get u from Alice. """
    global u
    u = var


def send():
    """ Send (v, z_b) to Alice. """
    v = __compute_v()
    z_b = matrix_b[u, v]
    return v, z_b
