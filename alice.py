def init(x_in, r_in, n_in, matrix_a_in, ):
    global x, r, n, matrix_a, u
    x = format(x_in, 'b')
    r = format(r_in, 'b')
    n = n_in
    matrix_a = matrix_a_in
    u = __compute_u()


def __compute_u():
    print("x: " + str(x))
    print("r: " + str(r))
    return (int(str(x), 2) + int(str(r), 2)) % (2 ** n)


def send():
    """ Send (u) to Bob. """
    return u


def receive(v_in, z_b_in):
    global v, z_b
    v = v_in
    z_b = z_b_in


def output_z():
    """ Return z, which is the resulting bit. """
    # TODO: Make sure z is in {0,1}
    return matrix_a[u, v] ^ z_b
