# this is a normal function return values and perform the 2 arguments(also called default arguments)

# def add(a,b):
#   return a+b
# res=add(5,9)
# print(res)

# function with variable arguments
# def add(num1,*num2):
#   sum=num1
#   for i in num2:
#     sum=sum+i
#   return sum
# res=add(2,2,4,5,6)
# print(res)


# function with keyword arguments
def person(name,age):
  print("name : ",name)
  print("age : ",age)
details=person(age="24",name="sai")