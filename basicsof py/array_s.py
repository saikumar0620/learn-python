# explore all the array methods

from array import *

# arr= array('i',[23,35,5,7,23])
# arr.append(12)
# arr.insert(0,1)
# arr.extend([50,40])
# arr.pop(2)
# arr.remove(7)
# arr.index(23)
# print(arr.count(23))
# arr.reverse()
# for i in arr :
#   print(i)


arr1= array('i',[3,544,34,5,323,2,])

arr2=array(arr1.typecode,(n for n in arr1))

arr1[0]=50
for i in arr2:
  print(i)
# print(arr2)