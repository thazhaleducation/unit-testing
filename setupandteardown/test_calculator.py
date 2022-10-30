import unittest

from setupandteardown.calculator  import Calculator


class CalculatorTestCase(unittest.TestCase):

  def test_add_should_return_addition_of_two_positive_numbers(self):
    calc = Calculator()
    actual_result = calc.add(1, 2)
    expected_result = 3
    assert actual_result == expected_result
  
  def test_add_should_return_addition_of_two_negative_numbers(self):
    calc = Calculator()
    actual_result = calc.add(-1, -3)
    expected_result = -4
    assert actual_result == expected_result
  
  def test_return_addition_of_two_numbers_when_one_of_the_operand_is_negative(self):
    calc = Calculator()
    actual_result = calc.add(-1, 2)
    expected_result = 1
    assert actual_result == expected_result


if __name__ == '__main__':
    unittest.main()
