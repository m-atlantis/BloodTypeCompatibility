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
    return ~x


def and_x_with_y(x, y, u, v, w):
    d = x ^ u
    e = y ^ v
    z = w ^ e & x ^ d & y ^ e & d
    return z


def layer_1(y_in):
    tmp = [0, 0, 0]

    for i in range(3):
        tmp[i] = xor_with_const_1(y_in[i])

    return tmp


def layer_2(x_in, y_in, u, v, w):
    tmp = [0, 0, 0]

    for i in range(3):
        tmp[i] = and_x_with_y(x_in[i], y_in[i], u[i], v[i], w[i])

    return tmp


def layer_3(var_in):
    tmp = [0, 0, 0]

    for i in range(3):
        tmp[i] = xor_with_const_1(var_in[i])

    return tmp


def layer_4(var_in, u, v, w):
    return and_x_with_y(and_x_with_y(var_in[0], var_in[1], u[3], v[3], w[3]), var_in[2], u[4], v[4], w[4])


def secure_bool_eval_blood_type_compatibility(x, y, u, v, w):
    return layer_4(layer_3(layer_2(x, layer_1(y), u, v, w)), u, v, w)
