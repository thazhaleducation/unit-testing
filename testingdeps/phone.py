from testingdeps.battery import Battery

class Phone:
  BATTERY_LOW_THRESHOLD = 15

  def __init__(self, battery):
    self.battery = battery

  def enable_power_save_mode(self):
    return self.battery.charge_remaining <= Phone.BATTERY_LOW_THRESHOLD

