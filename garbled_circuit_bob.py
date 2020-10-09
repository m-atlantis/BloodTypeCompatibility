import garbled_circuit_extra_func as func
import garbled_circuit_func as gb_func
import random


def init(y_in):
    global F, Y, d
    one_power_128_string = func.create_128_bit_string(1)
    circuit = None

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)


def enc_x(e_x, x):
    # TODO: 2-1-OT protocol
    e_x_0 = [0]
    e_x_1 = [1]
    X = [e_x_0, e_x_1]
    return X


def send_to_alice():
    return F, Y, d
