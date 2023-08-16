# programme mindriser atm
# programmen need
# check balance
# withdraw amount
# add amount
# register debit card and deposite amount 

    

def check_balance(debit_cards): # check balance function
    card_number = input("Enter your debit card number: ")
    if card_number in debit_cards:
        print(f"Your balance is: rs {debit_cards[card_number]}")
        print(f"Your debit card number :{card_number} ")
    else:
        print(f"{card_number} Debit card not registered. Please register your card.")

def add_amount(debit_cards): #add amount function
    card_number = input("Enter your debit card number: ")
    if card_number in debit_cards:
        additional_amount = int(input("Enter the amount to add: rs "))
        debit_cards[card_number] += additional_amount
        print(f"{additional_amount} added successfully.")
    else:
        print("Debit card not registered. Please register your card.")

def withdraw_amount(debit_cards): # withdraw amount function
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


def register_debitcard_deposit(debit_cards): # register debit card and deposite amount function
    card_number = input("Enter your new debit card number: ")
    if card_number not in debit_cards:
        amount = int(input("Enter the amount to deposit: rs "))
        debit_cards[card_number] = amount
        print(f"{card_number} Debit card successfully registered and rs{amount} amount deposited.")
    else:
        print(f"{card_number} Debit card already registered. Please use the check balance option.")

# def valid_card(card_number):
#     return len(card_number) == 16 and card_number.isdigit()


def title():
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

while re:
    title()
    choice = input("enter your choice (1/2/3/4/5): ")

    if choice == '1':
        # card_number = input("Enter your debit card number: ")
        # if card_number in debit_cards:
        #     print(f"Your balance is: rs{debit_cards[card_number]}")
        #     print(f"Your debit card number :{card_number} ")
        # else:
        #     print(f"{card_number} Debit card not registered. Please register your card.")
        check_balance(debit_cards) #calling function check_balance
    elif choice == '2':
        # card_number = input("Enter your new debit card number: ")
        # while not valid_card(card_number) :
        #     print(f"{card_number} Invalid debit card number. Please enter a 16-digit number.")
        # card_number = input("Enter your new debit card number: ")
        # if card_number not in debit_cards:
        #     amount = int(input("Enter the amount to deposit: rs "))
        #     debit_cards[card_number] = amount
        #     print(f"{card_number} Debit card successfully registered and rs{amount} amount deposited.")
        # else:
        #     print(f"{card_number} Debit card already registered. Please use the check balance option.")
        register_debitcard_deposit(debit_cards) # calling function register_debitcard_deposit
    elif choice == '3':
        withdraw_amount(debit_cards) # calling function withdraw_amount
    elif choice == '4':
        add_amount(debit_cards) # calling function add_amount
    elif choice == '5':
        print("program exiting. goodbye!")
        break
    else:
        print("invalid choice. please enter a valid option (1/2/3/4/5).")
