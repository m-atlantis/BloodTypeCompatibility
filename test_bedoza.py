import unittest
import bedoza_dealer as dealer
import bedoza_alice as alice
import bedoza_bob as bob
import boolean_blood_type_eval as booleval


def init_parties(x, y):
    dealer.__init_x_and_y_partitions()
    alice.__init(x, dealer.get_x_b())
    bob.__init(y, dealer.get_y_a())
    alice.set_y_a(bob.get_y_a())
    bob.set_x_b(alice.get_x_b())


def test():
    x = 2
    y = 7
    init_parties(x, y)
    u, v, w = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    for i in range(5):
        u[i] = alice.__get_u(i) ^ bob.__get_u(i)
        v[i] = alice.__get_v(i) ^ bob.__get_v(i)
        w[i] = alice.__get_w()[i] ^ bob.__get_w()[i]

    # Layer 1
    alice.set_y_a(booleval.layer_1(alice.get_y_a()))
    bob.set_y_b(booleval.layer_1(bob.get_y_b()))

    # Layer 2
    d_shares_a, e_shares_a = booleval.get_e_d_shares(alice.get_x_a(), alice.get_y_a(), alice.__get_u(0), alice.__get_v(0))
    d_shares_b, e_shares_b = booleval.get_e_d_shares(bob.get_y_b(), bob.get_y_b(), bob.__get_u(0), bob.__get_v(0))
    d, e = [0, 0, 0], [0, 0, 0]
    for i in range(3):
        d[i] = d_shares_a[i] ^ d_shares_b[i]
        e[i] = e_shares_a[i] ^ e_shares_b[i]

    alice.set_z(booleval.layer_2_1(alice.get_x_a(), alice.get_y_a(), alice.__get_w(), d, e))
    bob.set_z(booleval.layer_2_1(bob.get_x_b(), bob.get_y_b(), bob.__get_w(), d, e))

    # Layer 3
    alice.set_z(booleval.layer_3(alice.get_z()))
    bob.set_z(booleval.layer_3(bob.get_z()))

    # Layer 4
    alice.set_z(booleval.)

    print(alice.get_z())
    print(bob.get_z())


class TestProtocolCorrectness(unittest.TestCase):
    # The following tests for compatibility with self
    def test_test(self):
        x = 3
        y = 3
        init_parties(x, y)

        # self.assertEqual(eval.secure_bool_eval_blood_type_compatibility(x, y, u, v, w),
        #                 eval.blood_type_boolean(x, y))


# suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
# unittest.TextTestRunner(verbosity=2).run(suite)
test()
