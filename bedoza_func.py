import bedoza_dealer as dealer


def get_bits(byte_in):
    tmp = []
    for i in range(3):
        tmp.insert(0, int((byte_in & (1 << i)) != 0))
    return tmp


def xor_with_1(val_in):
    return ~val_in


#        while not dealer.triple_check():
#            dealer.__init_triple()
#        u[i], v[i], w[i] = dealer.get_triple_a()


def calc_d_e_shares(x, y, u, v):
    d_share = x ^ u
    e_share = y ^ v
    return d_share, e_share
