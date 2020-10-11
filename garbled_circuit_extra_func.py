import hashlib
import random


def get_bits(byte_in):
    """ Returns bit-string representation of given int. """
    tmp = []
    for i in range(3):
        tmp.insert(0, int((byte_in & (1 << i)) != 0))
    return tmp


def get_bit(byte_val, idx):
    """ Returns bit on index 'idx' of integer bit-representation. """
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

    return final_bit_str


def hash(left_key, right_key, input=None):
    """ Hashing using SHA-256 of digest length 32 bit, using first 'left_key' and then 'right_key'. """
    h = hashlib.shake_256()
    h.update(str(left_key).encode('utf-8'))
    h.update(str(right_key).encode('utf-8'))

    if input is not None:
        h.update(input.encode('utf-8'))

    return h.hexdigest(32)


def string_xor(s1, s2):
    """This is a work-around for XOR of strings."""
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
