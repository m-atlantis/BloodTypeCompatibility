import random


def __init_triple():
    global u_a, u_b, v_a, v_b, w_a, w_b
    u_a = random.getrandbits(1)
    u_b = random.getrandbits(1)
    v_a = random.getrandbits(1)
    v_b = random.getrandbits(1)
    w_a = random.getrandbits(1)
    w_b = random.getrandbits(1)


def triple_check():
    __init_triple()
    while not ((w_a ^ w_b) == (u_a ^ u_b) & (v_a ^ v_b)):
        __init_triple()


def init():
    global u_a_1, u_b_1, v_a_1, v_b_1, w_a_1, w_b_1
    global u_a_2, u_b_2, v_a_2, v_b_2, w_a_2, w_b_2
    global u_a_3, u_b_3, v_a_3, v_b_3, w_a_3, w_b_3

    u_a_1, u_b_1, v_a_1, v_b_1, w_a_1, w_b_1 = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]

    for i in range(3):
        triple_check()
        u_a_1[i], v_a_1[i], w_a_1[i] = get_triple_a()
        u_b_1[i], v_b_1[i], w_b_1[i] = get_triple_b()

    triple_check()
    u_a_2, v_a_2, w_a_2 = get_triple_a()
    u_b_2, v_b_2, w_b_2 = get_triple_b()

    triple_check()
    u_a_3, v_a_3, w_a_3 = get_triple_a()
    u_b_3, v_b_3, w_b_3 = get_triple_b()


def init_fake():
    global u_a_1, u_b_1, v_a_1, v_b_1, w_a_1, w_b_1
    global u_a_2, u_b_2, v_a_2, v_b_2, w_a_2, w_b_2
    global u_a_3, u_b_3, v_a_3, v_b_3, w_a_3, w_b_3
    u_a_1, u_b_1, v_a_1, v_b_1, w_a_1, w_b_1 = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]
    u_a_2, u_b_2, v_a_2, v_b_2, w_a_2, w_b_2 = 0, 0, 0, 0, 0, 0
    u_a_3, u_b_3, v_a_3, v_b_3, w_a_3, w_b_3 = 0, 0, 0, 0, 0, 0


def get_triple_a():
    return u_a, v_a, w_a


def get_triple_b():
    return u_b, v_b, w_b


def get_u_v_w_layer1_a():
    return u_a_1, v_a_1, w_a_1


def get_u_v_w_layer1_b():
    return u_b_1, v_b_1, w_b_1


def get_u_v_w_layer4_a():
    return u_a_2, v_a_2, w_a_2


def get_u_v_w_layer4_b():
    return u_b_2, v_b_2, w_b_2


def get_u_v_w_layer5_a():
    return u_a_3, v_a_3, w_a_3


def get_u_v_w_layer5_b():
    return u_b_3, v_b_3, w_b_3
