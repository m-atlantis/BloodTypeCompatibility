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


def __run():
    val1 = input("Enter blood type for recipient: ")
    val2 = input("Enter blood type for donor: ")

    x = __get_blood_type_bits(val1)
    y = __get_blood_type_bits(val2)

    dealer.__init()
    dealer.init_alice(x)
    dealer.init_bob(y)
    bob.receive(alice.send())
    v, z_b = bob.send()
    alice.receive(v, z_b)

    print(alice.output_z())


__run()
