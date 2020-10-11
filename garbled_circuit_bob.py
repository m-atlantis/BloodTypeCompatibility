import garbled_circuit_extra_func as func
import garbled_circuit_func as gb_func
import elgamal


def init(y_in):
    global F, Y, d, blood_type_index, encrypted_e_x

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)
    Y = [e_y, e_xor]

    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (
            elgamal.encrypt_for_garbled_circuits(e_x[i][0], public_keys[i][0], primes[i], generators[i]))
        encrypted_e_x[i][1] = (
            elgamal.encrypt_for_garbled_circuits(e_x[i][1], public_keys[i][1], primes[i], generators[i]))

    # TODO: This is used to override encrypted_e_x[] because OT doesn't decrypt correctly.
    encrypted_e_x = e_x


def set_public_keys(pk_in, g_in, p_in):
    global public_keys, generators, primes
    public_keys = pk_in
    generators = g_in
    primes = p_in


def get_encrypted_messages():
    return encrypted_e_x


def send_to_alice():
    return F, Y, d
