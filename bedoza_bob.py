import random
from bedoza_func import get_bits, xor_with_1, calc_d_e_shares
import bedoza_alice as alice
import bedoza_dealer as dealer


def __init(y_in):
    global y, u, v, w, y_a, y_b
    y = get_bits((y_in))
    # y_a = [random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)]
    y_a = [0, 0, 1]
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
    new_x = []
    for i in range(3):
        new_x.append(xor_with_1(get_x_share()[i]))
    set_x_share(new_x)


def set_e_d_shares(d, e):
    global d_shares, e_shares
    e_shares = e
    d_shares = d


def set_u_v_w(u_in, v_in, w_in):
    global u, v, w
    u = u_in
    v = v_in
    w = w_in


def layer_2_0():
    u_in, v_in, w_in = dealer.get_u_v_w_layer1_b()

    set_u_v_w(u_in, v_in, w_in)
    set_e_d_shares([0, 0, 0], [0, 0, 0])

    for i in range(3):
        d_shares[i], e_shares[i] = calc_d_e_shares(x_share[i], y_b[i], u[i], v[i])


def get_e_d_shares():
    return d_shares, e_shares


def set_z_share(z):
    global z_share
    z_share = z


def layer_2_1():
    z = [0, 0, 0]
    d_b_shares, e_b_shares = alice.get_e_d_shares()

    for i in range(3):
        e = e_shares[i] ^ e_b_shares[i]
        d = d_shares[i] ^ d_b_shares[i]
        z[i] = (w[i] ^ e) & (y_b[i] ^ d) & (x_share[i] ^ e) & d

    set_z_share(z)


def layer_3():
    new_z = []
    for i in range(3):
        new_z.append(xor_with_1(z_share[i]))
    set_z_share(new_z)


def layer_4_0():
    u_in, v_in, w_in = dealer.get_u_v_w_layer4_b()
    set_u_v_w(u_in, v_in, w_in)
    d, e = calc_d_e_shares(z_share[2], z_share[1], u, v)
    set_e_d_shares(d, e)


def layer_4_1():
    d_b_shares, e_b_shares = alice.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares
    z = (w ^ e) & (z_share[2] ^ d) & (z_share[1] ^ e) & d

    set_z_share_layer_4(z)


def set_z_share_layer_4(z):
    global z_share_4
    z_share_4 = z


def layer_5_0():
    u_in, v_in, w_in = dealer.get_u_v_w_layer5_b()
    set_u_v_w(u_in, v_in, w_in)

    d, e = calc_d_e_shares(z_share_4, z_share[0], u, v)
    set_e_d_shares(d, e)


def layer_5_1():
    d_b_shares, e_b_shares = alice.get_e_d_shares()
    e = e_shares ^ e_b_shares
    d = d_shares ^ d_b_shares
    z = (w ^ e) & (z_share_4 ^ d) & (z_share[0] ^ e) & d

    set_final_z(z)


def set_final_z(z):
    global z_final
    z_final = z


def get_final_z():
    return z_final
