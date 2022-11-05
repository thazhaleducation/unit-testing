import unittest

from unittest.mock import Mock

from testwithmock.phone import Phone

class PhoneTestCase(unittest.TestCase):
  def setUp(self):
    self.battery = Mock()
    self.phone = Phone(self.battery)
    return super().setUp()

  def test_should_return_true_for_enable_power_save_mode_when_battery_low(self):
    self.battery.charge_remaining = Mock(return_value=10)
    self.assertTrue(self.phone.enable_power_save_mode())
    self.battery.charge_remaining.assert_called_once()

  def test_should_return_false_for_enable_power_save_mode_when_battery_is_not_low(self):
    self.battery.charge_remaining = Mock(return_value=30)
    self.assertFalse(self.phone.enable_power_save_mode())
    self.assertEqual(len(self.battery.charge_remaining.mock_calls), 1)


if __name__ == '__main__':
    unittest.main()
