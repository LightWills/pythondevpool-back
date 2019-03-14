import unittest


class BasicTestCase(unittest.TestCase):

    def test_add(self):
        self.assert(1, 2)


if __name__ == "__main__":
    unittest.main()
    