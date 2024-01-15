### This a demonstration script for the following assignment.
'''
Erwin Ma 
Student ID: 349916
CSC 500 Principles of Programming
Critical Thinking Assigment 1
''';



# Get input.  has to cast as float
print("Please enter two numbers for addition and subtraction.")
num1 = float(input("Choose number one: "))
num2 = float(input("Choose number two: "))
 
# Calculate
sum = num1 + num2
difference = num1 - num2
 
# Print
print(f"Adding {num1:.2f} to {num2:.2f} gives: {sum:.2f}")
print(f"Subtracting {num1:.2f} from {num2:.2f} gives: {difference:.2f}")
 
 
 
 
### biggest difference is we need to add an error check for 0
### because we can't divide by zero.
 
# get inputs
print('\nPlease enter two numbers for multiplication and division.')
print('The second number cannot be zero!')
num1 = float(input("Choose number one: "))
num2 = float(input("Choose number two: "))
 
# calculate again. use an if statement to check if zero.
if num2 == 0:
    print("Can't divide by zero.")
else:
    product = num1 * num2
    quotient = num1 / num2
 
    # Print the results
    print(f"Multiplying {num1} and {num2} gives: {product:.2f}")
    print(f"Dividing {num1} by {num2} gives: {quotient:.2f}")
