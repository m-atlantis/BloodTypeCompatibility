def get_bit(byte_val, idx):
    return (byte_val & (1 << idx)) != 0


def blood_type_boolean(x, y):
    # f((xA, xB, xR),(yA, yB, yR)) = (1 ⊕ (xA · (1 ⊕ yA))) · (1 ⊕ (xB · (1 ⊕ yB))) · (1 ⊕ (xR · (1 ⊕ yR)))
    return (1 ^ (get_bit(x, 2) & (1 ^ get_bit(y, 2)))
            & (1 ^ (get_bit(x, 1) & (1 ^ get_bit(y, 1))))
            & (1 ^ (get_bit(x, 0) & (1 ^ get_bit(y, 0)))))
