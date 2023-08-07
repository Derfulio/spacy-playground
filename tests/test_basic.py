import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1+1, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
