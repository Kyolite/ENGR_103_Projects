# Author: Kyle Davis
# GitHub username: Kyolite
# Date: 10/11/2023
# Description: Prompts the user to input a Celsius temperature and displays the corresponding Fahrenheit temperature

print("Please enter a Celsius temperature.")  # Prompts user to enter a Celsius temperature
cel_temp = float(input())  # assigns user input to the variable cel_temp and casts as float
c_to_f = cel_temp * (9/5) + 32  # converts Celsius temperature to Fahrenheit temperature
print("The equivalent Fahrenheit temperature is:")  # prints corresponding Fahrenheit temperature
print(c_to_f)
