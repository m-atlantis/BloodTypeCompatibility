## Instruction to ```blood_type_compatibility.py``
The first function looks up the chosen two blood types in a dictionary using the recipients type as the key, and the donors blood type is the value. By seeing if such a value exists for a given key is equal to making a lookup in a truth table.

The second function uses 3-bit representations of the blood types to do bitwise-OR comparisons. By bitwise-OR'ing the two blood types and comparing the result to the recipients blood type we can see if they are compatible. If the recipients bit-representation doesn't change the blood types fit.

The run the script:
	Python main.py ARG

Where ARG is either 1 or 2; running the first o`r second function respectively.
The user will then be prompt to type in the two blood types which are on the form:
	BloodType.TYPE
	
E.g.:
	BloodType.AB_minus
	BloodType.B_plus
	BloodType.O_minus
	
	.. etc.
The program will then return either 1 or 0 for compatibility. 
