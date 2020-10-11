import garbled_circuit_extra_func as func
import garbled_circuit_func as gb_func
import elgamal


def init(y_in):
    global F, Y, d, blood_type_index, encrypted_e_x

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)
    Y = [e_y, e_xor]

    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (elgamal.encrypt(e_x[i][0], public_keys[i][0]))
        encrypted_e_x[i][1] = (elgamal.encrypt(e_x[i][1], public_keys[i][1]))

    # TODO: This is used because OT doesn't decrypt correctly.
    encrypted_e_x = e_x


def set_public_keys(pk_in):
    global public_keys
    public_keys = pk_in


def get_encrypted_messages():
    return encrypted_e_x


def send_to_alice():
    return F, Y, d
