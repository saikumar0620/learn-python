
# #  decorator define  one way
# def deco(fucn):
#   def wrapper(a,b):
#     if a <b:
#       a,b=b,a
#     return fucn(a,b)
#   return wrapper
  

# # @deco
# # def div(a,b):
# #   return a/b
# # @deco
# # def add(a,b):
# #   return a+b
# @deco
# def sub(a,b):
#   return a-b

# divd_res=div(4,2)
# print(divd_res)
# # add_res=add(4,2)
# # print(add_res)
# # sub_res=sub(2,4)
# # print(sub_res)

# decorator define 2nd approch

def greater_first(fncn):
  def wrapper(a,b):
      if a<b:
        a,b=b,a
      return fncn(a,b)
  return wrapper

def add(a,b):
  return a+b
add=greater_first(add)
res1=add(2,3)
print(res1)