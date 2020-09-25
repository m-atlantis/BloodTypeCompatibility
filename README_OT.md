# Instructions
The implementation of ElGamal is done with smaller integers, instead of BigInts to save computation time, and to avoid having to implement a primality test, like Miller-Rabin.
I found this fitting, since the importance is understanding the protocol and not security.

To run the tests do:

```python test_ot.py```

### About the (8-1) OT implementation
The 8 messages Alice sends to Bob are public keys, where only 1 of these are generated correctly, the one matching Alice blood type index row, and the rest are generated using the o-gen method.
Bob then returns 8 messages, which are all values for the column in the truth table that corresponds to his blood type.
Now when Alice decrypts the message from Bob that fits her secret key, she opens the index in the truth table that corresponds to both of their blood types.

When both Alice and Bob have i.e. AB+ as their blood types, there is no security using ElGamal, as the c2 part of the encryptions always is equal to 0 for every value that is encrypted by the o-gen public key, thus they learn each others blood types.
This is fixed by setting every false value in the truth table = 2, and using 2 as the value for False, such that encryptions always are different from 0.