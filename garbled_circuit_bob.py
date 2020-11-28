import garbled_circuit_func as gb_func
import elgamal_new as elgamal


def init(y_in):
    """ Initializes the Garbled Circuit, and encrypts the computed e_x values,
        using the public keys from Alice.
        The values of e_x are converted from binary to integer before being encrypted,
        the resolve size errors for El-Gamal encryption of large strings with chosen primes p, q. """
    global F, Y, d, blood_type_index, encrypted_e_x

    F, e_x, e_y, e_xor, d = gb_func.init_garbled_circuit(y_in)
    Y = [e_y, e_xor]

    encrypted_e_x = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        encrypted_e_x[i][0] = (elgamal.encrypt(int(e_x[i][0], 2), public_keys[i][0]))
        encrypted_e_x[i][1] = (elgamal.encrypt(int(e_x[i][1], 2), public_keys[i][1]))


def set_public_keys(pk_in):
    """ Sets the public keys to the given input. """
    global public_keys
    public_keys = pk_in


def get_encrypted_messages():
    """ A getter for the encrypted e_x values. """
    return encrypted_e_x


def send_to_alice():
    """ Send the garbled circuit values to Alice. """
    return F, Y, d
