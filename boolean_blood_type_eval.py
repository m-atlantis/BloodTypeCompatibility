import bedoza_alice
import bedoza_bob


def get_bit(byte_val, idx):
    return (byte_val & (1 << idx)) != 0


def blood_type_boolean(x, y):
    # f((xA, xB, xR),(yA, yB, yR)) = (1 ⊕ (xA · (1 ⊕ yA))) · (1 ⊕ (xB · (1 ⊕ yB))) · (1 ⊕ (xR · (1 ⊕ yR)))
    return (1 ^ (get_bit(x, 2) & (1 ^ get_bit(y, 2)))
            & (1 ^ (get_bit(x, 1) & (1 ^ get_bit(y, 1))))
            & (1 ^ (get_bit(x, 0) & (1 ^ get_bit(y, 0)))))


def xor_with_const_1(x):
    # XOR with 1 is a NOT gate
    return ~ x


def and_x_with_y(x, y, u, v):
    d_share = x ^ u
    e_share = y ^ v
    return d_share, e_share


def layer_1(y_in):
    tmp = [0, 0, 0]

    for i in range(3):
        tmp[i] = xor_with_const_1(y_in[i])

    return tmp


def get_e_d_shares(x_in, y_in, u, v):
    d_shares = [0, 0, 0]
    e_shares = [0, 0, 0]

    for i in range(3):
        d_shares[i], e_shares[i] = and_x_with_y(x_in[i], y_in[i], u, v)

    return d_shares, e_shares


def layer_2_1(x_share, y_share, w_share, d, e):
    z = [0, 0, 0]

    for i in range(3):
        z[i] = w_share[i] ^ e[i] & x_share[i] ^ d[i] & y_share[i] ^ e[i] & d[i]

    return z


def layer_3(var_in):
    tmp = [0, 0, 0]

    for i in range(3):
        tmp[i] = xor_with_const_1(var_in[i])

    return tmp


def layer_4(x_share, y_share, w_share, d, e):
    z = [0, 0, 0]

    for i in range(3):
        z[i] = w_share[i] ^ e[i] & x_share[i] ^ d[i] & y_share[i] ^ e[i] & d[i]

    return z
