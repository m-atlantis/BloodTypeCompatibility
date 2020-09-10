def init(x_in, r_in, n_in, matrix_a_in, ):
    global x, r, n, matrix_a, u
    x = x_in
    r = r_in
    n = n_in
    matrix_a = matrix_a_in
    u = __compute_u()


def __compute_u():
    return (x + r) % (2 ** n)


def send():
    """ Send (u) to Bob. """
    return u


def receive(v_in, z_b_in):
    global v, z_b
    v = v_in
    z_b = z_b_in


def output_z():
    """ Return z, which is the resulting bit. """
    return matrix_a[u, v] ^ z_b
