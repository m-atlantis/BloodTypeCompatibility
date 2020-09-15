import unittest
import bedoza_dealer as dealer
import bedoza_alice
import bedoza_bob
import boolean_blood_type_eval


def init_parties(x, y):
    dealer.__init_x_and_y_partitions()
    bedoza_alice.__init(x, dealer.get_x_b())
    bedoza_bob.__init(y, dealer.get_y_a())


class TestProtocolCorrectness(unittest.TestCase):
    # The following tests for compatibility with self
    def test_test(self):
        x = 3
        y = 3
        init_parties(x, y)
        self.assertEqual(1, boolean_blood_type_eval.blood_type_boolean(x, y))


suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
unittest.TextTestRunner(verbosity=2).run(suite)
