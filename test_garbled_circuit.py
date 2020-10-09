import unittest
import garbled_circuit_alice as alice
import garbled_circuit_bob as bob
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


# suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
# unittest.TextTestRunner(verbosity=2).run(suite)

print(test(2, 3))
