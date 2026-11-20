# we should know about †he inheritences
# SINGLE heritence definition: in general example is parent properties is to the child Like (parent to child class)

# single inheritence
# class A:
#   def f1(self):
#     print("f1 calls")
#   def f2(self):
#     print("f2 calls")

# class B:
#     def f3(self):
#       print("f3 calls")
#     def f4(self):
#       print("f4 calls")
      
# obj1=A()
# obj1.f1()#in this way  we can access only theb parent one class methods access
# obj1.f4()# now your trying to access the another class methods your getting an error



#Multi level inheritence

# class A:
#   def f1(self):
#     print("f1 calls")
#   def f2(self):
#     print("f2 calls")

# class B(A):
#     def f3(self):
#       print("f3 calls")
#     def f4(self):
#       print("f4 calls")
      
# obj1=B()
# obj1.f1()
# obj1.f4()


# multiple inheritence
# class A:
#   def f1(self):
#     print("f1 calls")
#   def f2(self):
#     print("f2 calls")
#   def access(self):
#     print("inside a called")

# class B:
#     def f3(self):
#       print("f3 calls")
#     def f4(self):
#       print("f4 calls")
#     def access(self):
#       print("inside b called")
# class C(A,B):
#     def f3(self):
#       print("f3 calls")
#     def f4(self):
#       print("f4 calls")
#     # def access(self):
#     #   print("inside c called")
      
# obj1=C()
# obj1.access()


class A():
  def __init__(self):
    print("A init called")
  def f1(self):
    print("called A f1")
    
class B(A):
  def __init__(self):
    super().__init__()
    print("B init called")
  def f2(self):
    print("called B f2")
    
    
obj=B()
obj.f2()
