#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
print("please enter the amount of terms you want to print")
terms = input()
print("calculating fibbonacci sequence up to " + terms + " digits")

value1 = 0
value2 = 1
for x in range (0,4):
  if x == 0:
    print(value1)
  else:
    value3 = value1 + value2
    value1 = value2
    value2 = value3
    print(value2)
  
