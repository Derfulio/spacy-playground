import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4+4, 8)  # add assertion here


if __name__ == '__main__':
    unittest.main()
