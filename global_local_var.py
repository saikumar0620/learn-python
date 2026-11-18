#  learning about global variable and local variables

# the below code snippet has accepts the oute side of the function  still it can access the variable values
# a=2
# def checks():
#   print(a)
# checks()

# the below one code also works as usual 
# a=2
# def checking2():
#   a=10
#   print("inside of :",a)
# checking2()
# print("outside of the :",a)


# when it comes to the if we use same variable with mapping or overwrite on it
# python will provides a special method (globals)

# a=2
# def check3():
#   a=1
#   globals()['a']=10
#   print("inside :", a)
# check3()
# print("outside :", a)



