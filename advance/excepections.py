# file and error exception handling

# a=3;b=4 #when you try to excecute with the zeroth values you will get an error
# def cal(a,b):
#   return a/b
# res=cal(a,b)
# print(res)




try:
    a=int(input("enter numerator : "))
    b=int(input("enter denominator : "))
    res=a/b
    print("the result is : ",res)
except Exception as e :
    print(e)
except ValueError as ve :
    print(ve)
finally:
  print("excecutions closed here ")
