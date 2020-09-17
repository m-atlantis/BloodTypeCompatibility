import unittest
import bedoza_dealer as dealer
import bedoza_alice as alice
import bedoza_bob as bob
from boolean_blood_type_eval import blood_type_boolean


def init_parties(x, y):
    dealer.init()
    alice.__init(x)
    bob.__init(y)
    alice.set_y_share(bob.send_y_share_to_alice())
    bob.set_x_share(alice.send_x_share_to_bob())


def test(x, y):
    # Init
    init_parties(x, y)

    # Layer 1
    alice.layer_1()
    bob.layer_1()

    # Layer 2
    alice.layer_2_0()
    bob.layer_2_0()
    alice.layer_2_1()
    bob.layer_2_1()

    # Layer 3
    alice.layer_3()
    bob.layer_3()

    # Layer 4
    alice.layer_4_0()
    bob.layer_4_0()
    alice.layer_4_1()
    bob.layer_4_1()

    # Layer 5
    alice.layer_5_0()
    bob.layer_5_0()
    alice.layer_5_1()
    bob.layer_5_1()

    # Output z
    return alice.output_z()


class TestProtocolCorrectness(unittest.TestCase):
    def test_all(self):
        for i in range(8):
            for j in range(8):
                self.assertEqual(test(j, i), blood_type_boolean(j, i))

    def test_101_011(self):
        x = 5
        y = 3
        self.assertEqual(test(x, y), blood_type_boolean(x, y))

    def test_000_011(self):
        x = 0
        y = 3
        # print(blood_type_boolean(x, y))
        self.assertEqual(test(x, y), blood_type_boolean(x, y))

    def test_010_100(self):
        y = 2
        x = 4
        self.assertEqual(test(x, y), blood_type_boolean(x, y))


suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
unittest.TextTestRunner(verbosity=2).run(suite)
