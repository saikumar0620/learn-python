# we should know about †he inheritences
# SINGLE heritence definition: in general example is parent properties is to the child Like (parent to child class)


class A:
  def f1(self):
    print("f1 calls")
  def f2(self):
    print("f2 calls")

class B:
    def f3(self):
      print("f3 calls")
    def f4(self):
      print("f3 calls")
      
obj1=A()
obj1.f1()