from garbled_circuit_extra_func import *


def xor_gate(labels_a, labels_b, labels_c):
    """" Creates garbled circuit of an XOR gate. """
    c = []
    one_power_128_string = create_128_bit_string(0)

    c.append(string_xor(hash(labels_a[0], labels_b[1]), (labels_c[1] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[1]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[0], labels_b[0]), (labels_c[1] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[0]), (labels_c[0] + one_power_128_string)))

    # Shuffle the list
    random.shuffle(c)

    return c


def and_gate(labels_a, labels_b, labels_c):
    """" Creates garbled circuit of an AND gate. """
    c = []
    one_power_128_string = create_128_bit_string(0)

    c.append(string_xor(hash(labels_a[0], labels_b[0]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[0], labels_b[1]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[0]), (labels_c[0] + one_power_128_string)))
    c.append(string_xor(hash(labels_a[1], labels_b[1]), (labels_c[1] + one_power_128_string)))

    # Shuffle the list
    random.shuffle(c)

    return c


def init_garbled_circuit(y):
    """ Creates the garbled circuit used for Blood Type Compatibility. """
    labels = [[""] * 2] * 23
    for i in range(23):
        labels[i] = create_labels_e()

    # Ugly code for better readability.
    F = []

    F.append(xor_gate(labels[0], labels[1], labels[2]))
    F.append(and_gate(labels[2], labels[3], labels[4]))
    F.append(xor_gate(labels[4], labels[5], labels[6]))

    F.append(xor_gate(labels[7], labels[8], labels[9]))
    F.append(and_gate(labels[9], labels[10], labels[11]))
    F.append(xor_gate(labels[11], labels[12], labels[13]))

    F.append(and_gate(labels[6], labels[13], labels[14]))

    F.append(xor_gate(labels[15], labels[16], labels[17]))
    F.append(and_gate(labels[17], labels[18], labels[19]))
    F.append(xor_gate(labels[19], labels[20], labels[21]))

    F.append(and_gate(labels[14], labels[21], labels[22]))

    d = labels[22]

    e_x = [labels[3], labels[10], labels[18]]
    e_y = enc_y([labels[0], labels[7], labels[15]], y)
    e_xor = [labels[1], labels[5], labels[8], labels[12], labels[16], labels[20]]

    return F, e_x, e_y, e_xor, d


def create_labels_e():
    """ Creates labels used to represent bits in the Garbled Circuit. """
    wire_0 = create_128_bit_string()
    wire_1 = create_128_bit_string()

    return [wire_0, wire_1]


def enc_y(e_y_labels, y_in):
    """ Creates [Y] by encoding y bit values to e_y labels. """
    y_in_bits = get_bits(y_in)
    Y = []

    for i in range(3):
        Y.append(e_y_labels[i][y_in_bits[i]])

    return Y


def evaluate_gate(garbled_gate, l_a, r_b, i):
    """ Evaluates a given gate on left key and right key. The value 'i' is given for debugging purposes. """

    one_power_128_string = create_128_bit_string(0)

    for i in range(4):
        k = string_xor(garbled_gate[i], hash(l_a, r_b))

        if k[16:] == one_power_128_string:
            return k[:16]

    # TODO: Fix depth, always returning 3 not matter where the decoding fails.
    raise Exception("No correct decryption found for the given keys at gate: ", i)


def evaluate_circuit(F, e_x, e_y, e_xor):
    """ Evaluate the full Blood Type Compatibility circuit. """
    ya_xor = evaluate_gate(F[0], e_y[0], e_xor[0][1], 0)
    ya_and_xa = evaluate_gate(F[1], ya_xor, e_x[0], 1)
    gate_3_xor = evaluate_gate(F[2], ya_and_xa, e_xor[1][1], 2)

    yb_xor = evaluate_gate(F[3], e_y[1], e_xor[2][1], 3)
    yb_and_xb = evaluate_gate(F[4], yb_xor, e_x[1], 4)
    gate_6_xor = evaluate_gate(F[5], yb_and_xb, e_xor[3][1], 5)

    gate_3_and_gate_6 = evaluate_gate(F[6], gate_3_xor, gate_6_xor, 6)

    yr_xor = evaluate_gate(F[7], e_y[2], e_xor[4][1], 7)
    yr_and_xr = evaluate_gate(F[8], yr_xor, e_x[2], 8)
    gate_10_xor = evaluate_gate(F[9], yr_and_xr, e_xor[5][1], 9)

    return evaluate_gate(F[10], gate_3_and_gate_6, gate_10_xor, 10)
