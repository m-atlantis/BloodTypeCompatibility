import garbled_circuit_func as func
import elgamal_new as elgamal


def init(x_in):
    """ Initializes the El-Gamal public keys and secret keys. """
    global public_keys, secret_keys, x
    x = func.get_bits(x_in)

    public_keys, secret_keys = [], []

    elgamal.init_g_p_q()
    for i in range(3):
        create_keys(i)


def create_keys(i):
    """ Generates the secret keys and public keys dynamically.
        The public keys for x[i] are correctly generated, and
        the ones for 1 - x[i] are the fake ones. """
    sk = elgamal.create_sk()
    secret_keys.append(sk)

    keys = [0, 0]

    keys[x[i]] = elgamal.gen(sk)
    keys[1 - x[i]] = elgamal.o_gen()

    public_keys.append(keys)


def get_public_keys():
    """ Getter for the public keys. """
    return public_keys


def set_values_from_bob(F_in, Y_in, d_in, ciphertexts):
    """ Sets the variables for the values coming from Bob. """
    global F, d, e_x, e_y, e_xor
    F, d = F_in, d_in
    e_y, e_xor = Y_in
    e_x = decrypt(ciphertexts)


def test():
    """ Evaluates the circuit to check if decoding can be done correctly for the chosen values. """
    Z = func.evaluate_circuit(F, e_x, e_y, e_xor)
    if Z == d[0]:
        return 0
    elif Z == d[1]:
        return 1


def decrypt(ciphertexts):
    """ Decrypts the ciphertexts that matches the indexes of the binary value for x.
        Since the values are converted from binary to integers before decryption,
        then the decrypted values are converted back to binary and filled to fit a 16-bit size. """
    e_x = []

    for i in range(3):
        c1, c2 = ciphertexts[i][x[i]]
        dec = elgamal.decrypt(c1, c2, secret_keys[i])
        e_x.append(str(bin(dec))[2:].zfill(16))

    return e_x
