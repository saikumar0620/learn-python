# factorial of a number approch 1

# def fact(num):
#   result=1
#   for i in range(1,num+1):
#     result=result*i
#   return result
# res=fact(5)
# print(res)

#  factorial of given number by using recursion

# def rec(num):
#   if num == 1:
#     return 1
#   return num*rec(num -1)
# res=rec(5)
# print(res)


def rec(num):
  if num == 1:
    return 1
  return num*rec(num -1)
res=rec(5)
print(res)
