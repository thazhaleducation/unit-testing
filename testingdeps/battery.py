class Battery:
  FULL_CHARGE = 100

  def __init__(self, charge = FULL_CHARGE) -> None:
    self.charge_remaining = charge
  
  def set_charge(self, charge):
    self.charge_remaining = charge

  def charge_remaining(self):  # pragma: no cover
    return self.charge_remaining
