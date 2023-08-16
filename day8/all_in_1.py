import time
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

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Exiting the program in {i} seconds...")
        time.sleep(1)


def calculator():
    print("Calculator")
    print("a. Addition")
    print("s. Subtraction")
    print("m. Multiplication")
    print("d. Division")

    operation = (input("Enter your choice: ")).lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == 'a':
        print(add(num1,num2))
    elif operation == 's':
        print(subtract(num1,num2))
    elif operation == 'm':
        print(multiply(num1,num2))
    elif operation == 'd':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(divide(num1,num2))
    else:
        print("Invalid operation selected. Please select  'a','s','m','d':")

def check_voting_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("you are eligible to vote.") #f"{age} are eligible to vote."
    else:
        print("you arenot eligible to vote.") #f"{number} is positive number."

def check_positive_negative_zero():
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"{num} is positive number.")
    elif num < 0:
        print(f"{num} is negative number.")
    else:
        print(f"{num} is zero number.")

def check_odd_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

def main():
    while True:
        print("\nSelect an option:")
        print("c. Calculator")
        print("v. Check Voting Eligibility")
        print("pnz. Check Positive/Negative/Zero")
        print("oe. Check Odd/Even number")
        print("e. Exit")

        option = (input("Enter your choice: ")).lower()

        if option == "c":
            calculator()
        elif option == 'v':
            check_voting_eligibility()
        elif option == 'pnz':
            check_positive_negative_zero()
        elif option == 'oe':
            check_odd_even()
        elif option == 'e':
            print("Exiting the program in 5 second")
            countdown_timer(4)
            print("Good Bye!")
            break
        else:
            print("Invalid choice. Please select a number from 'a','v','pnz','oe','e'.")

if __name__ == "__main__":
    main()