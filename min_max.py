# Author: Kyle Davis
# GitHub username: Kyolite
# Date: 10/14/2023
# Description:

print("How many integers would you like to enter?")
num_of_ints = int(input())
print("Please enter", num_of_ints, "integers.")
min_num = max_num = int(input())
for i in range(num_of_ints - 1):
    num = int(input())
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num
print("min:", min_num)
print("max:", max_num)
