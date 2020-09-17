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
    # The following tests for compatibility with self
    def test_all(self):
        for i in range(8):
            for j in range(8):
                self.assertEqual(test(i, j), blood_type_boolean(i, j))

    def test_101_011(self):
        self.assertEqual(test(5, 3), blood_type_boolean(5, 3))


# suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
# unittest.TextTestRunner(verbosity=2).run(suite)

print(test(5, 3))
