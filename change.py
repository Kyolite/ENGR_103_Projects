# Author: Kyle Davis
# GitHub username: Kyolite
# Date: 10/11/2023
# Description: Asks user for an integer number of cents from 0 to 99 and outputs
# how many of each type of coin would represent that amount with the fewer total
# number of coins

QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1
print("Please enter an amount in cents less than a dollar.")
cents = int(input())
q_amount = cents // QUARTERS
d_amount = ((cents - (q_amount * QUARTERS)) // DIMES)
n_amount = ((cents - (q_amount * QUARTERS) - (d_amount * DIMES)) // NICKELS)
p_amount = (cents - (q_amount * QUARTERS) - (d_amount * DIMES) - (n_amount * NICKELS))
print("Your change will be: ")
print("Q: " + str(q_amount))
print("D: " + str(d_amount))
print("N: " + str(n_amount))
print("P: " + str(p_amount))
