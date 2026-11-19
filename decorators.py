

#  decorator define  one way
def log_info(fucn):
  def wrap(*args,**kwargs):
    print("the value are :",args)
    result=fucn(*args)
    print("the result is :",result)
    return result
  return wrap
    

def greater_first(fucn):
  def wrapper(*args):
    args=list(args)
    if len(args)>=2 and args[0] < args[1]:
    # if a <b:
      args[0],args[1] =args[1],args[0]
      # a,b=b,a
    return fucn(*args)
  return wrapper

@log_info
@greater_first
def div(a,b,c):
  return a+b+c
divd_res=div(4,2,4)

# @log_info
# @deco
# def div(a,b):
#   return a/b

# @log_info
# @deco
# def add(a,b):
#   return a+b

# print(divd_res)
# add_res=add(4,2)
# print(add_res)
# sub_res=sub(2,4)
# print(sub_res)
