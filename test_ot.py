import unittest
import ot_alice as alice
import ot_bob as bob
import elgamal


def test(x, y):
    elgamal.init()
    alice.init(x)
    bob.set_public_keys(alice.get_public_keys())
    bob.init(y)
    return alice.decrypt(bob.get_encrypted_messages())


class TestProtocolCorrectness(unittest.TestCase):
    # def test_all_in_one_function(self):
    #     for i in range(8):
    #         for j in range(8):
    #             to_test = test(i, j)
    #             self.assertEqual(to_test, (i | j) == i)

    # The following tests all combinations of AB+
    def test_111_110(self):
        i = 7
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_101(self):
        i = 7
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_100(self):
        i = 7
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_011(self):
        i = 7
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_010(self):
        i = 7
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_001(self):
        i = 7
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_111_000(self):
        i = 7
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 110
    def test_110_111(self):
        i = 6
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_101(self):
        i = 6
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_100(self):
        i = 6
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_011(self):
        i = 6
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_010(self):
        i = 6
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_001(self):
        i = 6
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_110_000(self):
        i = 6
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 101
    def test_101_111(self):
        i = 5
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_110(self):
        i = 5
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_100(self):
        i = 5
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_011(self):
        i = 5
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_010(self):
        i = 5
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_001(self):
        i = 5
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_101_000(self):
        i = 5
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 100
    def test_100_111(self):
        i = 4
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_110(self):
        i = 4
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_101(self):
        i = 4
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_011(self):
        i = 4
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_010(self):
        i = 4
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_001(self):
        i = 4
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_100_000(self):
        i = 4
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 011
    def test_011_111(self):
        i = 3
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_110(self):
        i = 3
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_101(self):
        i = 3
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_100(self):
        i = 3
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_010(self):
        i = 3
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_001(self):
        i = 3
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_011_000(self):
        i = 3
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 010
    def test_010_111(self):
        i = 2
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_110(self):
        i = 2
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_101(self):
        i = 2
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_100(self):
        i = 2
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_011(self):
        i = 2
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_001(self):
        i = 2
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)

    def test_010_000(self):
        i = 2
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 001
    def test_001_111(self):
        i = 1
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_110(self):
        i = 1
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_101(self):
        i = 1
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_100(self):
        i = 1
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_011(self):
        i = 1
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_010(self):
        i = 1
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_001_000(self):
        i = 1
        j = 0
        self.assertEqual(test(i, j), (i | j) == i)

    # The following tests all combinations for 000
    def test_000_111(self):
        i = 0
        j = 7
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_110(self):
        i = 0
        j = 6
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_101(self):
        i = 0
        j = 5
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_100(self):
        i = 0
        j = 4
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_011(self):
        i = 0
        j = 3
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_010(self):
        i = 0
        j = 2
        self.assertEqual(test(i, j), (i | j) == i)

    def test_000_001(self):
        i = 0
        j = 1
        self.assertEqual(test(i, j), (i | j) == i)


suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
unittest.TextTestRunner(verbosity=2).run(suite)
