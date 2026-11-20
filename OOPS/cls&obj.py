class computer:
  brand=" Brand is APPLE"
  manufactured="manufactured 2020"
  expired= "expired 2026"

  def __init__(self,cpu,ram,ssd):
    # print("init called")
    self.cpu=cpu
    self.ram=ram
    self.ssd=ssd
    
  def properties(self):
    print("configuration", self.cpu,self.ram,self.ssd)
    
  @classmethod 
  def brandInfo(cls):
    return cls.brand,cls.manufactured,cls.expired


print(computer.brandInfo())
c1=computer("M4","12GB","512Gb")
c2=computer("M5","16GB","1Tb")
c1.properties()
c2.properties()


