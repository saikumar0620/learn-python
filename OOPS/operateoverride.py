# many forms for best example

# let know with an example
# a=2
# b=3
# # c=a+b
# c= int.__add__(a,b) # the above method and this one give you the same result under hood python is trace
# print(c)

class Account:
  def __init__(self,name,amount):
    self.name=name
    self.amount=amount
    
  def __str__(self):
    return f"{self.name } : {self.amount}"
  def __add__(self,others):
    return Account(f"combained balance is " , self.amount+others.amount)
    # return Account("combained : ", me.amount + others.amount)
  def __gt__(self,others):
    return self.amount>others.amount
    
user1=Account("sai",1000)
user2=Account("naveen",2000)
combained = user1+user2
print(user1,user2)
# print(combained)

# use case 
if user1>user2:
  print("pay the bill sai")
else:
  print("bill pay naveen")
    