import random
from bedoza_func import get_bits, xor_with_1, calc_d_e_shares
import bedoza_bob as bob
import bedoza_dealer as dealer


def __init(x_in, u_v_w_in):
    global x, u, v, w, x_a, x_b, u_v_w
    u_v_w = u_v_w_in
    x = get_bits(x_in)
    x_b = [random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)]
    x_a = __create_x_a()


def __create_x_a():
    tmp = []

    for i in range(len(x_b)):
        tmp.append(x[i] ^ x_b[i])
    return tmp


def set_y_share(y_in):
    global y_share
    y_share = y_in


def get_y_share():
    return y_share


def send_x_share_to_bob():
    return x_b


def layer_1():
    new_y = []

    for i in range(3):
        new_y.append(xor_with_1(get_y_share()[i]))
    set_y_share(new_y)


def set_e_d_shares(d, e):
    global d_shares, e_shares
    e_shares = e
    d_shares = d


def set_u_v_w(i):
    global u, v, w
    u = u_v_w[i][0]
    v = u_v_w[i][1]
    w = u_v_w[i][2]


def layer_2_0():
    global w_2
    w_2 = []
    set_e_d_shares([0, 0, 0], [0, 0, 0])

    for i in range(3):
        set_u_v_w(i)
        w_2.append(w)
        d_shares[i], e_shares[i] = calc_d_e_shares(x_a[i], y_share[i], u, v)


def get_e_d_shares():
    return d_shares, e_shares


def set_z_share(z):
    global z_share
    z_share = z


def layer_2_1():
    z = [0, 0, 0]
    d_b_shares, e_b_shares = bob.get_e_d_shares()

    for i in range(3):
        e = e_shares[i] ^ e_b_shares[i]
        d = d_shares[i] ^ d_b_shares[i]
        z[i] = w_2[i] ^ e & x_a[i] ^ d & y_share[i] ^ e & d

    set_z_share(z)


def layer_3():
    new_z = []
    for i in range(3):
        new_z.append(xor_with_1(z_share[i]))

    set_z_share(new_z)


def layer_4_0():
    set_u_v_w(3)

    d, e = calc_d_e_shares(z_share[1], z_share[2], u, v)

    set_e_d_shares(d, e)


def layer_4_1():
    d_b_shares, e_b_shares = bob.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares

    z = w ^ e & z_share[1] ^ d & z_share[2] ^ e & d

    set_z_share_layer_4(z)


def set_z_share_layer_4(z):
    global z_share_4
    z_share_4 = z


def layer_5_0():
    set_u_v_w(4)

    d, e = calc_d_e_shares(z_share[0], z_share_4, u, v)

    set_e_d_shares(d, e)


def layer_5_1():
    d_b_shares, e_b_shares = bob.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares

    z = w ^ e & z_share[0] ^ d & z_share_4 ^ e & d

    set_final_z(z)


def set_final_z(z_in):
    global z_final
    z_final = z_in


def output_z():
    return z_final ^ bob.get_final_z()
