
# swapping of two numbers without using third variable

# a=2; b=4
# a=a+b
# b=a-b
# a=a-b
# print(a,b)



#  sum of three digits number


# num= 123
# hundreds= num // 100
# tens= (num // 10) % 10
# ones= num % 10
# total= hundreds+tens+ones
# print("the sum of toatl digits:", total)


# swap pratcices agin

# a=3;b=5
# a=a+b
# b=a-b
# a=a-b
# print(a,b)


# table print

# number = 3
# for i in range(1,11):
#   result=number*i
#   print(number,"X",i,"=",result)

# sum of natural numbers

# total=0
# for num in range(1,101):
#   total=num+total
# print(total)


# simple multiplication table 

# tablenum=2
# for i in range(1,11):
#   res=tablenum*i
#   print(tablenum,"X",i,"=",res)


# sum of three digits

# num = 123

# hundreds=num // 100
# tens=(num // 10)%10
# ones= num %10
# digits=hundreds+tens+ones
# print("the sum of three digits are : ",digits)

# sum of natural numbers

# number=0
# for i in range(1,101):
#   number= number+i
# print(number)


# reverse of a number
# number=123

# approch one 
# while number > 0:
#   digit=number % 10
#   print(digit)
#   number= number//10

# approch two
# number =12345
# reversed=0
# while number > 0:
#   digit=number % 10
#   reversed=reversed*10+digit
#   number=number // 10
# print(reversed)


# reverse

# num=123
# while num > 0:
#   digit= num % 10
#   print(digit)
#   num=num // 10

# 2nd approch
# num =123
# reversed=0
# while num > 0:
#   digit=num%10
#   reversed=reversed*10+digit
#   num=num // 10
# print(reversed)
  
  
  # fact of num usingb recursion
  
# def rec(number):
#   if number == 1:
#     return number
#   return number*rec(number-1)

# res=rec(5)
# print(res)

# lambda fn

def swape_1st(fn):
  def wrapper(*args):
    args=list(args)
    
    if len(args)>=2 and args[0]< args[1]:
      args[0],args[1]=args[1], args[0]
      # a,b=b,a
    return fn(*args)
  return wrapper
    
      
@swape_1st
def add(a,b,c,d):
  return a+b+c+d
res=add(6,7,8,9)
print(res)