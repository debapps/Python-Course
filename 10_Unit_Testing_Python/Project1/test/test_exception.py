import unittest
from proj.sample_module import add2num

class TestExceprion(unittest.TestCase):

    def test_add_exception(self):
    #     self.assertRaises(TypeError, add2num, 2, 'Bittu')

        with self.assertRaises(TypeError) as e:
            r = add2num(3, 'hello')
            self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")


if __name__ == '__main__':
    unittest.main()