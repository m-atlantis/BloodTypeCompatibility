import random
import numpy as np

def init(n):
    # Choose shifts r \in {0,1}^n and s \in {0,1}^n uniformly random
    # Choose random matrix M_b \in {0,1}^(2^n x 2^n) uniformly random
    # Compute matrix M_a s.t. M_a[i,j] = M_b[i,j] XOR T[i - r mod 2^n, j - s mod 2^n]
    # T[i,j] = f(i,j) and a truth table
    #
    # Output (r, M_a) to Alice, and (s, M_b) to Bob
    r = create_random_bit_string(n)
    s = create_random_bit_string(n)

    M_b = "np.matrix"

    return True


def create_random_bit_string(n):
    final_bit_str = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        final_bit_str += temp

    return final_bit_str
