from enum import Enum
import sys


class BloodType(Enum):
    AB_plus = int('111', 2)
    AB_minus = int('110', 2)
    A_plus = int('101', 2)
    A_minus = int('100', 2)
    B_plus = int('011', 2)
    B_minus = int('010', 2)
    O_plus = int('001', 2)
    O_minus = int('000', 2)


def lookup_compatibility(recipient, donor):
    compatibility = {
        BloodType.O_minus: [e for e in BloodType],
        BloodType.O_plus: [BloodType.O_plus, BloodType.A_plus, BloodType.B_plus, BloodType.AB_plus],
        BloodType.B_minus: [BloodType.B_minus, BloodType.B_plus, BloodType.AB_plus, BloodType.AB_minus],
        BloodType.B_plus: [BloodType.B_plus, BloodType.AB_plus],
        BloodType.A_minus: [BloodType.A_plus, BloodType.A_minus, BloodType.AB_minus, BloodType.AB_plus],
        BloodType.A_plus: [BloodType.A_plus, BloodType.AB_plus],
        BloodType.AB_minus: [BloodType.AB_plus, BloodType.AB_minus],
        BloodType.AB_plus: [BloodType.AB_plus]
    }
    if recipient in compatibility[donor]:
        return 1
    else:
        return 0


def lookup_compatibility_boolean(recipient, donor):
    if bin(recipient.value | donor.value) == bin(recipient.value):
        return 1
    else:
        return 0
    # print("{0:b}".format(donor.value | recipient.value))


def main():
    if len(sys.argv) != 2:
        print("Type 1 or 2 as argument")
        exit()
    for arg in sys.argv[1:]:
        val = input("Enter blood type for recipient: ")
        val2 = input("Enter blood type for donor: ")

        if arg == "1":
            print(lookup_compatibility(val, val2))
        if arg == "2":
            print(lookup_compatibility_boolean(val, val2))
        else:
            exit()


main()
