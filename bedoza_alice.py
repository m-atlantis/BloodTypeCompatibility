import bedoza_bob
import bedoza_dealer as dealer


def __init(x_in, x_b_in):
    global x, u, v, w, x_a, x_b, y_a
    x = x_in
    x_a, x_b, y_a = [0, 0, 0], [0, 0, 0], [0, 0, 0]
    x_b = x_b_in
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


def __get_w(i):
    return w[i]


def set_y_a(y_a_in, i):
    y_a[i] = y_a_in


def get_y_a(i):
    return y_a[i]


def send_x_b_to_bob(i):
    return x_b[i]


def output_x():
    return int(' '.join([str(elem) for elem in x_a]), 2)
