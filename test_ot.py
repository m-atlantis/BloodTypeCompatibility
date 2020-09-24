import unittest


class TestProtocolCorrectness(unittest.TestCase):
    def test(self):
        return True


suite = unittest.TestLoader().loadTestsFromTestCase(TestProtocolCorrectness)
unittest.TextTestRunner(verbosity=2).run(suite)
