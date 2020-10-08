import garbled_circuit_func as func
import random


def init(y_in):
    global F, Y, d
    one_power_128_string = func.create_128_bit_string(1)
    circuit = None

    F, e_x, e_y, d = func.garble_circuit(one_power_128_string, circuit)

    Y = func.enc_y(None, None)


def send_to_alice():
    return F, Y, d
