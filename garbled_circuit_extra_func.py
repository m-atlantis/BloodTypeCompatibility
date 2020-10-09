import hashlib
import random


def get_bits(byte_in):
    tmp = []
    for i in range(3):
        tmp.insert(0, int((byte_in & (1 << i)) != 0))
    return tmp


def get_bit(byte_val, idx):
    return (byte_val & (1 << idx)) != 0


def create_128_bit_string(bit=None):
    """ Creates a string of random bits that is of length n. """
    final_bit_str = ""

    for i in range(16):
        if bit is None:
            temp = str(random.randint(0, 1))
        else:
            temp = str(bit)
        final_bit_str += temp

    # return int(final_bit_str, 2)
    return final_bit_str


def hash(left_key, right_key, input=None):
    h = hashlib.shake_256()
    h.update(left_key.encode('utf-8'))
    h.update(right_key.encode('utf-8'))

    if input is not None:
        h.update(input.encode('utf-8'))

    return h.hexdigest(32)


def string_xor(s1, s2):
    """Work around for XOR of strings found on stackoverflow."""
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
