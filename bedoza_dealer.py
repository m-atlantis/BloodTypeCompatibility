import random


def init_random_vars():
    return random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)


def __init_x_and_y_partitions():
    global x_b, y_a
    x_b = init_random_vars()
    y_a = init_random_vars()


def __init_triple():
    global u_a, u_b, v_a, v_b, w_a, w_b
    u_a = random.getrandbits(1)
    u_b = random.getrandbits(1)
    v_a = random.getrandbits(1)
    v_b = random.getrandbits(1)
    w_a = random.getrandbits(1)
    w_b = random.getrandbits(1)


def triple_check():
    return (w_a ^ w_b) == (u_a ^ u_b) & (v_a ^ v_b)


def get_y_a():
    return y_a


def get_x_b():
    return x_b


def get_triple_a():
    return u_a, v_a, w_a


def get_triple_b():
    return u_b, v_b, w_b
