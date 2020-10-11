# Instructions
To run the code, type
```python test_garbed_circuit.py```

I apparently have an error somewhere in my construction of the p and q values for ElGamal.
Since this assignment hasn't been corrected, and despite trying to debug and find the error myself, 
I have had to send the e_x value to Alice without using OT, so she simply just chooses the value, causing no secure on this part, meaning she learns both values of e_x.

The error is very peculiar. I have tried encrypting e_x = [[1, 2], [1, 2], [1, 3]], which are values that I can encrypt and decrypt correctly in the OT assignment.
This also works for Alice' x value = 111, but if the value is e.g. 100, two of the 3 values are decrypted wrong. If e.g. x = 010 the value for 1 is decrypted wrong, so I can't even find the invariant for decrypting wrong.
I have tried changing the length of the chosen primes without success. 

The code for OT and ElGamal that doesn't work is included but commented out.
