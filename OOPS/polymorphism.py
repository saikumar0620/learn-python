#  polymorphism
class human:
  def speak(self):
    return"showting"
    
class animal:
  def speak(self):
    return"meow meow"
    
    
things=[human(),animal()]
# print(things)
for i in things:
  print(i.speak())