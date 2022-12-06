# import the necessary modules
import random

# define a function to generate a 16-digit number
def generate_number(first_six):
  # create a list to store the digits
  digits = [0] * 16

  # set the first 6 digits based on the input
  for i in range(6):
    digits[i] = int(first_six[i])

  # generate the remaining 10 digits randomly
  for i in range(6, 16):
    digits[i] = random.randint(0, 9)

  # calculate the 16th digit using the Luhn algorithm
  digits[15] = (sum(digits[::2]) * 2 + sum(digits[1::2])) % 10

  # return the 16-digit number as a string
  return "".join(str(d) for d in digits)

# prompt the user for the first 6 digits
first_six = input("Enter the first 6 digits: ")

# prompt the user for the number of outputs
num_outputs = int(input("Enter the number of outputs: "))

# generate and print the desired number of outputs
for i in range(num_outputs):
  number = generate_number(first_six)
  print(number)
