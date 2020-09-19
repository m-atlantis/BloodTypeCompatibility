import unittest
import bedoza_dealer as dealer
import bedoza_alice as alice
import bedoza_bob as bob
from bedoza_func import blood_type_boolean


def init_parties(x, y):
    randomness_a, randomness_b = dealer.init()
    alice.__init(x, randomness_a)
    bob.__init(y, randomness_b)
    alice.set_y_share(bob.send_y_share_to_alice())
    bob.set_x_share(alice.send_x_share_to_bob())


def run_circuit(x, y):
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
                self.assertEqual(run_circuit(i, j), blood_type_boolean(i, j))

    # def test_101_011(self):
    #     x = 5
    #     y = 3
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_111(self):
    #     x = 5
    #     y = 7
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_100_111(self):
    #     x = 5
    #     y = 7
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_111(self):
    #     x = 7
    #     y = 7
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_110(self):
    #     x = 7
    #     y = 6
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_101(self):
    #     x = 7
    #     y = 5
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_100(self):
    #     x = 7
    #     y = 4
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_011(self):
    #     x = 7
    #     y = 3
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_010(self):
    #     x = 7
    #     y = 2
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_001(self):
    #     x = 7
    #     y = 1
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_111_000(self):
    #     x = 7
    #     y = 0
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_111(self):
    #     x = 6
    #     y = 7
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_110(self):
    #     x = 6
    #     y = 6
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_101(self):
    #     x = 6
    #     y = 5
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_100(self):
    #     x = 6
    #     y = 4
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_011(self):
    #     x = 6
    #     y = 3
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_010(self):
    #     x = 6
    #     y = 2
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_001(self):
    #     x = 6
    #     y = 1
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_110_000(self):
    #     x = 6
    #     y = 0
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_110(self):
    #     x = 5
    #     y = 6
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_101(self):
    #     x = 5
    #     y = 5
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_100(self):
    #     x = 5
    #     y = 4
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_011(self):
    #     x = 5
    #     y = 3
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_010(self):
    #     x = 5
    #     y = 2
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_001(self):
    #     x = 5
    #     y = 1
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))
    #
    # def test_101_000(self):
    #     x = 5
    #     y = 0
    #     self.assertEqual(run_circuit(y, x), blood_type_boolean(y, x))


suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
unittest.TextTestRunner(verbosity=2).run(suite)
