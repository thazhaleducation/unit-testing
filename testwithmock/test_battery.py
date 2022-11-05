import unittest

from testwithmock.battery import Battery

class BatteryTestCase(unittest.TestCase):
  def setUp(self) -> None:
    self.battery = Battery()
    return super().setUp()

  def test_battery_initialized_with_100(self):
    self.assertEqual(self.battery.charge_remaining(), Battery.FULL_CHARGE)
  
  def test_battery_charge_is_updated(self):
    self.battery.set_charge(60)
    self.assertEqual(self.battery.charge_remaining(), 60)

if __name__ == '__main__':
    unittest.main()
