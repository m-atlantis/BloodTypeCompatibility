import garbled_circuit_extra_func as func
import garbled_circuit_func as gb_func
import elgamal


def init(y_in):
    global F, Y, d, blood_type_index, encrypted_e_x

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)

    e_x = [[0o0100100110101010, 0o1001101011000101], [0o0011100110010000, 0o1010111000001000],
           [0o1001111001011100, 0o0100000011101111]]
    e_x = [[1, 2], [1, 2], [2, 3]]
    print(e_x)
    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (elgamal.encrypt(e_x[i][0], public_keys[i][0]))
        encrypted_e_x[i][1] = (elgamal.encrypt(e_x[i][1], public_keys[i][1]))


def set_public_keys(pk_in):
    global public_keys
    public_keys = pk_in


def get_encrypted_messages():
    return encrypted_e_x


def enc_x(e_x, x):
    # TODO: 2-1-OT protocol
    e_x_0 = [0]
    e_x_1 = [1]
    X = [e_x_0, e_x_1]
    return X


def send_to_alice():
    return F, Y, d
