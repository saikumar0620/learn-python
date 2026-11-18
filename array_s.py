# explore all the array methods

from array import *
arr= array('i',[23,35,5,7,23])
arr.append(12)
arr.insert(0,1)
arr.extend([50,40])
arr.pop(2)
arr.remove(7)
arr.index(23)
print(arr.count(23))
arr.reverse()
for i in arr :
  print(i)