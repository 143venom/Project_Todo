# All in one programme
# add function
def add(a, b): 
    return a + b

# multiply function
def multiply(a, b):
    return a * b

# substract function
def substract(a, b):
    return a - b
# divide function
def divide(a, b):
    return a / b

# function calculator
def calculator():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    operation = input("choose your operation ('-', '*', '+', '/'):" )
    if operation == '+':
        print(add(first_number, second_number)) # calling add function
    elif operation == '-':
        print(substract(first_number, second_number)) # calling substract function
    elif operation == '*':
        print(multiply(first_number, second_number)) # calling multiply function
    elif operation == '/': 
        print(divide(first_number, second_number)) # calling divide function
    else:
        print(f"{operation} This operation is not available please coose from this ('-', '*', '+', '/')")

# Function voting
def voting():
    user_age = int(input('How Old Are You: '))
    if user_age >=18:
        print('Go and vote')
    else:
        print(' You are under 18 age. Go Home!')


# function five time print
# take permisstion to print five times
def five_times_print():
    user_name = input('What is your name: ')
    ask_user = input('may i print yoyr name five times (y/n):')
    if ask_user.lower() == "y":
        count = 0
        while count < 5:
            print(user_name)
            count += 1
    elif ask_user.lower() == 'n':
        print(user_name)
    else:
        print('programe clossing')


# Main Function 
print ('WELCOME TO ALL IN ONE PROGRAME')
print('MENU')
print('1.CALCOLATOR')
print('2.VOTING')
print('3.PRINT 5 TIMES')

while True:
    
    menu_select = input('Select taks from Menu"1,2,3": ')
    if menu_select == '1':
        calculator()        # calling function calculator
    elif menu_select == '2':
        voting()            #calling function votting
    elif menu_select == '3':
        five_times_print()  # calling function five time print
    else:
        # print('programe clossing')
        # restart main function
        # restart = input('Do you want to restart programme again (y/n): ')
        # if restart != 'y':
            break



