def get_bits(byte_in):
    tmp = []
    for i in range(3):
        tmp.insert(0, int((byte_in & (1 << i)) != 0))
    return tmp


def xor_with_1(val_in):
    return val_in ^ 1


def calc_d_e_shares(x, y, u, v):
    d_share = x ^ u
    e_share = y ^ v
    return d_share, e_share


# Used for testing:
def get_bit(byte_val, idx):
    return (byte_val & (1 << idx)) != 0


def blood_type_boolean(x, y):
    # ! y is recipient, x is donor !
    # f((xA, xB, xR),(yA, yB, yR)) = (1 ⊕ (xA · (1 ⊕ yA))) · (1 ⊕ (xB · (1 ⊕ yB))) · (1 ⊕ (xR · (1 ⊕ yR)))
    A_bit = (1 ^ (get_bit(x, 2) & (1 ^ get_bit(y, 2))))
    B_bit = (1 ^ (get_bit(x, 1) & (1 ^ get_bit(y, 1))))
    R_bit = (1 ^ (get_bit(x, 0) & (1 ^ get_bit(y, 0))))

    return (A_bit & B_bit) & R_bit
