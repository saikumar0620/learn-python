# this is all about higher order function
# meaning : a function which accepts a function as an arguments or returns function as a result


# examples code snipts of the above 

def square(nums):
   return nums*nums
  
def cube(nums):
     return nums*nums*nums

  
def operate(nums,operation):
  for i in nums:
    result=operation(i)
    print(result)
  
nums=[5,6,7]
operate(nums,cube)
