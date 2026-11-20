
# This is a simple Python program that demonstrates the use of a while loop to iterate through a list called `data`. The list contains both integers and strings. The program checks the type of each element in the list, and if the element is either an integer or a string, it prints that element to the console.


# data= [80,"hlo", 90, "hello", 100, "hi"]
# i=0
# while i < len(data):
#     if type(data[i]) == int or type(data[i]) == str:
#         print(data[i])
#     i += 1


# same example using for loop
# data= [80,"hlo", 90, "sai", 100, "kumar"]
# for item in data:
#     if isinstance(item, (str)):
#       print(item)

# for loop using range function

# data= [80,"hlo", 90, "sai", 100, "kumar"]

# for i in range(len(data)):
#     print(data[i])

for i in range(10):
    if i % 2 == 0:
      continue
    print(i)  

  