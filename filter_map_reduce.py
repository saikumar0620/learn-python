
from functools import reduce
#  learning about filter method 
# below one code also filter which you provide the logic  
nums=[123,34,5,656,7,8,734,4,4,242,3,12,332]
evens=[]
def filt(nums):
  for i in nums:
    if i%2==0:
       evens.append(i)
res=filt(nums)
print(evens) 
  

# now by using filter with usingb regular function

nums=[123,34,5,656,7,8,734,4,4,242,3,12,332]
def filt(n):
  return n % 2==0
res= list(filter(filt,nums))
print(res) 


# filter method by using lambda function
nums=[123,34,5,656,7,8,734,4,4,242,3,12,332]
# filt= lambda n: n%2==0  # this is the one expression 
filtered= list(filter(lambda n: n%2==0,nums)) #this is the another way of putting expression written into a one line 
 #this is the another way of putting expression written into a one line 
doubled=list(map(lambda n: n*2 ,filtered))
maxnum=reduce(lambda a,b:a+b,nums)
print(filtered) 
print(doubled) 
print(maxnum) 



      