import unittest

from exampletest.calculator  import Calculator  # CUT or SUT


class Test_TestCalculator(unittest.TestCase):
  def test_add_should_return_addition_of_two_numbers(self):
    # Arrange
    calc = Calculator()
    
    # Act
    actual_result = calc.add(1, 2)

    # Assert
    expected_result = 3
    assert actual_result == expected_result

if __name__ == '__main__':
    unittest.main()
