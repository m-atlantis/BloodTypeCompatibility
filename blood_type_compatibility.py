import sys
import dealer
import alice
import bob


def __get_blood_type_bits(i):
    switcher = {
        "AB+": 7,
        "AB-": 6,
        "A+": 5,
        "A-": 4,
        "B+": 3,
        "B-": 2,
        "O+": 1,
        "O-": 0,
        "111": 7,
        "110": 6,
        "101": 5,
        "100": 4,
        "011": 3,
        "010": 2,
        "001": 1,
        "000": 0
    }
    return switcher.get(i, "Invalid blood type.")


def __blood_type_compatibility(x, y):
    dealer.__init()
    dealer.init_alice(x)
    dealer.init_bob(y)
    bob.receive(alice.send())
    v, z_b = bob.send()
    alice.receive(v, z_b)
    return alice.output_z()


def should_return(x, y):
    should_be = 0

    if (x | y) == x:
        should_be = 1

    return should_be


def run(*args):
    if len(sys.argv) > 1 and sys.argv[1] == "spec":
        val1 = input("Enter blood type for recipient: ")
        val2 = input("Enter blood type for donor: ")

        x = __get_blood_type_bits(val1)
        y = __get_blood_type_bits(val2)

        print(__blood_type_compatibility(x, y))
    else:
        x = args[0]
        y = args[1]
        return __blood_type_compatibility(x, y)
