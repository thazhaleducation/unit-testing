import unittest

from testingdeps.phone import Phone
from testingdeps.battery import Battery

class PhoneTestCase(unittest.TestCase):
  def setUp(self):
    self.phone = Phone( )
    return super().setUp()

  def test_should_return_true_for_enable_power_save_mode_when_battery_low(self):
    phone_with_low_battery = Phone(Battery(10))
    self.assertTrue(phone_with_low_battery.enable_power_save_mode())
  
  def test_should_return_false_for_enable_power_save_mode_when_battery_is_not_low(self):
    self.assertFalse(self.phone.enable_power_save_mode())
  
if __name__ == '__main__':
    unittest.main()
