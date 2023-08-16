user_list = {}
def login_User():
    password = user_list.get(user_Name)
    user_pass = input('Enter Your password: ')
    if user_pass == password:
        main_Atm()
    else:
        register_debitcard_deposit()

def check_balance(): # check balance function
    card_number = input("Enter your debit card number: ")
    if card_number in debit_cards:
        print(f"Your balance is: rs {debit_cards[card_number]}")
        print(f"Your debit card number :{card_number} ")
    else:
        print(f"{card_number} Debit card not registered. Please register your card.")

def add_amount(): #add amount function
    card_number = input("Enter your debit card number: ")
    if card_number in debit_cards:
        additional_amount = int(input("Enter the amount to add: rs "))
        debit_cards[card_number] += additional_amount
        print(f"{additional_amount} added successfully.")
    else:
        print("Debit card not registered. Please register your card.")

def withdraw_amount(): # withdraw amount function
    card_number = input("Enter your debit card number: ")
    if card_number in debit_cards:
        withdrawal_amount = float(input("Enter the amount to withdraw: rs "))
        if withdrawal_amount <= debit_cards[card_number]:
            debit_cards[card_number] -= withdrawal_amount
            print(f"{withdrawal_amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Debit card not registered. Please register your card.")


def register_debitcard_deposit(): # register debit card and deposite amount function
    card_number = input("Enter your new debit card number: ")
    if card_number not in debit_cards:
        amount = int(input("Enter the amount to deposit: rs "))
        debit_cards[card_number] = amount
        print(f"{card_number} Debit card successfully registered and rs{amount} amount deposited.")
    else:
        print(f"{card_number} Debit card already registered. Please use the check balance option.")

def register_User():
    user_Name = input('Enter Your User Name: ')
    user_Password = input('Enter Your Password: ')
    user_list[user_Name] = user_Password

def titles():
    mind = '<----------Welcome MindRiser ATM---------->'
    # riser = mind.upper()
    print(mind.upper())
    print("1. Check Balance")
    print("2. register debit card and deposit")
    print("3. withdraw amount")
    print("4. add amount")
    print("5. exit")

debit_cards = {}
re = True



def main_Atm():
    while True:
        titles()
        choices = input("enter your choice (1/2/3/4/5): ")

        if choices == '1':
            
            check_balance() #calling function check_balance
        elif choices == '2':
            
            register_debitcard_deposit() # calling function register_debitcard_deposit
        elif choices == '3':
            withdraw_amount() # calling function withdraw_amount
        elif choices == '4':
            add_amount() # calling function add_amount
        elif choices == '5':
            login_User()
        else:
            print("invalid choice. please enter a valid option (1/2/3/4/5).")

def title():
    print("1. login")
    print("2. register")
    print('Press Any Key To Exit')

while re:
    title()
    choice = input("enter your choice (1/2): ")
    if choice == '1':
        user_Name = input('Enter Your User Name: ')
        if user_Name in user_list:
            login_User()
        else:
            print('User not in data base. Please Register first')
            register_User()
    elif choice == '2':
     register_User() # calling function register_User
    else:
        exit()


