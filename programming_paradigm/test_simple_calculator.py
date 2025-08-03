import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -6), -7)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.2, 2.8), 4.0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the sub method."""
        self.assertEqual(self.calc.subtract(7, 3), 4)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -6), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(3.5, 2.5), 1.0)

    def test_multipication(self):
        """Test the * method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -6), 6)
        self.assertEqual(self.calc.multiply(6, 0), 0)
        self.assertEqual(self.calc.multiply(1.2, 2.8), 3.36)

    def test_division(self):
        """Test the / method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(7, 1), 7)
        self.assertEqual(self.calc.divide(-8, 4), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 0),None, 'Division by zero is not allowed' )


# Remember to write additional test methods for subtract, multiply, and divide.
 
