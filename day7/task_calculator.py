# CALCULATOR
# Take first and second from user as input.
# Take arithmetic symbols operation from user to perform with those numbers .
# called function
# Perform the operation described by the user.


# add function
def add(a, b):
    return a + b

# subtract function
def subtract(a, b):
    return a - b

# multiply function
def multiply(a, b):
    return a * b

# divide function
def divide(a, b):
    return a / b

first_number = int(input("Enter your first number: "))
user_operation = input("select your operation '/','*','-','+': ")
second_number = int(input("Enter your second number: " ))

if user_operation == ("/"):
    # calling divided function
    print(divide(first_number, second_number))

elif user_operation == ("*"):
    # calling multiply function
    print(multiply(first_number, second_number))

elif user_operation == ("-"):
    # calling subtract function
    print(su(first_number, second_number))

elif user_operation == ("+"):
    # calling add function
    print(add(first_number, second_number))

else:
    print("The operation you provided is currently not available!")