""" Importing module for unit testing"""
import unittest
from dumbsquare.core import square

class TestCore(unittest.TestCase):
    """ Unittest class """

    def test_float(self):
        """ Test for square function """
        self.assertAlmostEqual(square(2.),4)

if __name__=='__main__':
    unittest.main()
