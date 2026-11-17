
# This is a simple while loop that starts with the variable `num` set to 5. The loop continues to execute as long as `num` is less than or equal to 10. Inside the loop, it prints the current value of `num` and then increments `num` by 1. Once `num` exceeds 10, the loop ends, and it prints a message indicating that the loop has ended, followed by the final value of `num`.


# num = 5
# while num <= 10:
#     print(num)
#     num += 1
# print("The loop has ended.")
# print(num)


# nested while loop
# This is a nested while loop that starts with the variable `num` set to 1. The outer loop continues to execute as long as `num` is less than or equal to

num = 1
while num <= 3:
    print("Outer loop iteration:", num)
    inner_num = 1
    while inner_num <= 2:
        print("  Inner loop iteration:", inner_num)
        inner_num += 1
    num += 1
print("The nested loop has ended.")