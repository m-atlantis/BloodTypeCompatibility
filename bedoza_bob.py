import bedoza_dealer as dealer


def __init(y_in, y_a_in):
    global y, u, v, w, y_b, y_a
    y = y_in
    y_b, y_a = [0, 0, 0], [0, 0, 0]
    y_a = y_a_in
    u = [0, 0, 0, 0, 0]
    v = [0, 0, 0, 0, 0]
    w = [0, 0, 0, 0, 0]

    for i in range(5):
        dealer.__init_triple()
        while not dealer.triple_check():
            dealer.__init_triple()
        u[i], v[i], w[i] = dealer.get_triple_b()
    for i in range(3):
        __create_y_b_and_y_a(i)


def __create_y_b_and_y_a(i):
    y_b[i] = y ^ y_a[i]


def __get_u(i):
    return u[i]


def __get_v(i):
    return v[i]


def __get_w():
    return w


# TESTING this
def set_y_b(y_b_in):
    y_b = y_b_in


def get_y_b():
    return y_b


def set_z(z_in):
    global z
    z = z_in


def get_z():
    return z


# def get_y_a():
#    return int(' '.join([str(elem) for elem in y_a]), 2)


def set_x_b(x_b_in):
    global x_b
    x_b = [0, 0, 0]
    x_b = x_b_in


def get_x_b():
    return x_b


def get_y_a():
    return y_a
