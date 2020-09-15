import bedoza_dealer as dealer


def __init(y_in, y_a_in):
    global y, u, v, w, y_b, y_a, x_b
    y = y_in
    y_b, y_a, x_b = [0, 0, 0], [0, 0, 0], [0, 0, 0]
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


def __get_w(i):
    return w[i]


def get_y_a():
    return int(' '.join([str(elem) for elem in y_b]), 2)


def set_x_b(x_b_in, i):
    x_b[i] = x_b_in


def get_x_b(i):
    return x_b[i]


def send_y_a_to_alice(i):
    return y_a[i]
