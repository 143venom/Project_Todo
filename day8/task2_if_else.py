# number = int(input("Enter a number: ")) # Get user input
# if number > 0:  # check the number is positive, Negative, Zero.
#     print(f"{number} is positive number.")
# elif number < 0:
#     print(f"{number} is Negative number.")
# else:
#     print(f"{number} is Zero number.")


def check_pos_neg_zer(number):
    if number > 0:  # checking given number is positive, Negative, Zero.
        print(f"{number} is positive number.")
    elif number < 0:
        print(f"{number} is Negative number.")
    else:
        print(f"{number} is Zero number.")

while True:
    num = int(input("Enter the Number: ")) # Get user input
    check_pos_neg_zer(num)
    restart = input("Do you want to check another number? (yes/no): ").lower()
    if restart != "yes":
        break

