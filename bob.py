def init(y_in, s_in, n_in, matrix_b_in):
    global y, s, n, matrix_b, v
    y = y_in
    s = s_in
    n = n_in
    matrix_b = matrix_b_in
    v = __compute_v()


def __compute_v():
    return (y + s) % (2 ** n)


def receive(u_in):
    """ Get u from Alice. """
    global u
    u = u_in


def send():
    """ Send (v, z_b) to Alice. """
    z_b = matrix_b[u, v]
    return v, z_b
