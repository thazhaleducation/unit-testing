import unittest

from setupandteardown.calculator  import Calculator


class CalculatorTestCase(unittest.TestCase):

  #Test Fixture
  def setUp(self) -> None:
    self.calc = Calculator()
    return super().setUp()

  def test_add_should_return_addition_of_two_positive_numbers(self):
    actual_result = self.calc.add(1, 2)
    expected_result = 3
    self.assertEqual(actual_result, expected_result)
  
  def test_add_should_return_addition_of_two_negative_numbers(self):
    actual_result = self.calc.add(-1, -3)
    expected_result = -4
    self.assertEqual(actual_result, expected_result)
  
  def test_return_addition_of_two_numbers_when_one_of_the_operand_is_negative(self):
    actual_result = self.calc.add(-1, 2)
    expected_result = 1
    self.assertEqual(actual_result, expected_result)
  
  def test_divide_should_return_result_of_division_of_two_numbers(self):
    actual_result = self.calc.divide(4, 2)
    expected_result = 2
    self.assertEqual(actual_result, expected_result)
  
  def test_divide_should_raise_exception_when_divided_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
      self.calc.divide(4, 0)

if __name__ == '__main__':
    unittest.main()
