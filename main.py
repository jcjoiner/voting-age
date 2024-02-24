# Problem Set 5
# Voting Age

'''
    Create a program that prompts the user to enter their age and then determines if they are eligible to vote.
'''

# Ask user for their age
# Check if user is 18 or older
# print() results back to the user

age = int(input("Enter your age: "))
if age >= 18:
    print("Congratulations, you can vote!")
else:
    print("Sorry, you cannot vote.")
