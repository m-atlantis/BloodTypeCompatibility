import bedoza_bob
import bedoza_dealer as dealer


def __init(x_in, x_b_in):
    global x, u, v, w, x_a, x_b
    x = x_in
    x_a, x_b = [0, 0, 0], [0, 0, 0]
    x_b = x_b_in
    # TODO : 5 * 3 u, v, w values needed?
    u = [0, 0, 0, 0, 0]
    v = [0, 0, 0, 0, 0]
    w = [0, 0, 0, 0, 0]

    for i in range(5):
        dealer.__init_triple()
        while not dealer.triple_check():
            dealer.__init_triple()
        u[i], v[i], w[i] = dealer.get_triple_a()
    for i in range(3):
        __create_x_a(i)


def __create_x_a(i):
    x_a[i] = x ^ x_b[i]


def __get_u(i):
    return u[i]


def __get_v(i):
    return v[i]


def __get_w():
    return w


def set_z(z_in):
    global z
    z = z_in


def get_z():
    return z


def set_y_a(y_a_in):
    global y_a
    y_a = [0, 0, 0]
    y_a = y_a_in


def get_y_a():
    return y_a


def set_x_a(x_a_in):
    x_a = x_a_in


def get_x_a():
    return x_a


def set_x_b(x_b_in):
    x_b = x_b_in


def get_x_b():
    return x_b


def output_x():
    return int(' '.join([str(elem) for elem in x_a]), 2) ^ x_b
