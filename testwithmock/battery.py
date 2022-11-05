class Battery:
  FULL_CHARGE = 100

  def __init__(self, charge = FULL_CHARGE) -> None:
    self._charge_remaining = charge
  
  def set_charge(self, charge):
    self._charge_remaining = charge

  def charge_remaining(self):
    return self._charge_remaining
