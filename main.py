class Mobile:
  def __init__(self, mobile, batt):
    self.mobile = mobile
    self.battery = batt

  def getMobile(self):
    print("Mobile: ", self.mobile)
    self.battery.getmah()
    

class Battery:
  def __init__(self, mah):
    self.mah = mah

  def getmah(self):
    print("Battery mAH: ", self.mah)
    

batt = Battery(5000)
mob = Mobile("Samsung", batt)
mob.getMobile()
