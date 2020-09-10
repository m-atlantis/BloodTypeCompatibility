## Instructions
Type `python test.py` to run the test-suite for the program.
It will test each blood type against each other from 000 - 000 to 111 - 111, and output the result and the expected result.

#### Testing specific blood types
If the user runs `python blood_type_compatibility.py spec`, the program will run and ask the user to input the specific blood types.
The allowed values for these are either their respective name or the bit encoding of the blood type, e.g.:
    
    AB+
    AB-
    B+ 
    O+
    O-
    111
    101
    001
    010
    ... etc.

Once both have been input, the program will return the result as a single bit, 1 for compatible, 0 for non-compatible. 