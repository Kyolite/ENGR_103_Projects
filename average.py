# Author: Kyle Davis
# GitHub username: Kyolite
# Date: 10/11/2023
# Description: Asks the user to input five numbers and prints the average of those numbers.

print("Please enter five numbers.")  # Prompts user to enter five numbers
# Assign each of the five user inputs to a unique variable (num_1-5)
num_1 = float((input()))  # float is used to cast from a string to a numerical value
num_2 = float((input()))
num_3 = float((input()))
num_4 = float((input()))
num_5 = float((input()))
# num_avg adds the five user inputs then divides by five to calculate the average
num_avg = ((num_1 + num_2 + num_3 + num_4 + num_5) / 5)
# Average is printed
print("The average of those numbers is:")
print(num_avg)
