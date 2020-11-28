import garbled_circuit_extra_func as func
import garbled_circuit_func as gb_func
import elgamal_new as elgamal


def init(y_in):
    global F, Y, d, blood_type_index, encrypted_e_x

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)
    Y = [e_y, e_xor]

    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (elgamal.encrypt(int(e_x[i][0], 2), public_keys[i][0]))
        encrypted_e_x[i][1] = (elgamal.encrypt(int(e_x[i][1], 2), public_keys[i][1]))


def set_public_keys(pk_in):
    global public_keys
    public_keys = pk_in


def get_encrypted_messages():
    return encrypted_e_x


def send_to_alice():
    return F, Y, d
