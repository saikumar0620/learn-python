def outer():
  print("outer fnctn prints")
  def inner():
    print("inner fnctn prints")
  return inner
res=outer()
res()
