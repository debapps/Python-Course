import unittest
from proj.sample_module import add2num, pow2num

def setUpModule():
    print('Executed before an test in the module')

def tearDownModule():
    print('Executed after all tests in module are run')

class TestAdd2Num(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Executed before any test in the class runs.')

    @classmethod
    def tearDownClass(cls):
        print('Executed after all tests in class are run.')

    def setUp(self):
        print('Executed before each test.')

    def tearDown(self):
        print('Executed after each test.')

    def test_sum_2pos_num(self):
        self.assertEqual(add2num(7, 8), 15)

    def test_sum_1pos_1neg_num(self):
        self.assertEqual(add2num(-10, 9), -1)

class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -27)


if __name__ == '__main__':
    unittest.main()