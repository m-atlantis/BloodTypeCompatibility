import random
from bedoza_func import get_bits, xor_with_1, calc_d_e_shares
import bedoza_alice as alice
import bedoza_dealer as dealer


def __init(y_in, u_v_w_in):
    global y, u, v, w, y_a, y_b, u_v_w
    u_v_w = u_v_w_in
    y = get_bits((y_in))
    y_a = [random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)]
    y_b = __create_y_b()


def __create_y_b():
    tmp = []
    for i in range(len(y_a)):
        tmp.append(y[i] ^ y_a[i])
    return tmp


def set_x_share(x_in):
    global x_share
    x_share = x_in


def get_x_share():
    return x_share


def send_y_share_to_alice():
    return y_a


def layer_1():
    pass


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
        d_shares[i], e_shares[i] = calc_d_e_shares(x_share[i], y_b[i], u, v)


def get_e_d_shares():
    return d_shares, e_shares


def set_z_share(z):
    global z_share
    z_share = z


def layer_2_1():
    z = [0, 0, 0]
    d_a_shares, e_a_shares = alice.get_e_d_shares()

    for i in range(3):
        e = e_shares[i] ^ e_a_shares[i]
        d = d_shares[i] ^ d_a_shares[i]

        z[i] = w_2[i] ^ e & x_share[i] ^ d & y_b[i]

    set_z_share(z)


def layer_3():
    pass
    # new_z = []
    # for i in range(3):
    #     new_z.append(xor_with_1(z_share[i]))
    # set_z_share(new_z)


def layer_4_0():
    set_u_v_w(3)

    d, e = calc_d_e_shares(z_share[1], z_share[2], u, v)

    set_e_d_shares(d, e)


def layer_4_1():
    d_b_shares, e_b_shares = alice.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares

    z = w ^ e & z_share[1] ^ d & z_share[2]

    set_z_share_layer_4(z)


def set_z_share_layer_4(z):
    global z_share_4
    z_share_4 = z


def layer_5_0():
    set_u_v_w(4)

    d, e = calc_d_e_shares(z_share[0], z_share_4, u, v)

    set_e_d_shares(d, e)


def layer_5_1():
    d_b_shares, e_b_shares = alice.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares

    z = w ^ e & z_share[0] ^ d & z_share_4

    set_final_z(z)


def set_final_z(z_in):
    global z_final
    z_final = z_in


def get_final_z():
    return z_final
