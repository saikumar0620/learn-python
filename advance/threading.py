class Hello():
  def do(self):
    for i in range(5):
      print("hello",i+1)
      
class Hi():
  def do(self):
    for i in range(5):
      print("Hi",i+1)
      
t1=Hello()
t2=Hi()

t1.do()
t2.do()