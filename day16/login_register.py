user_pass = {}
def user_login():
    password = user_pass.get(user_name)
    users_pass = input('Enter your password: ')
    if users_pass == password:
        print('login successfull')
    else:
         print('invalid user!')

def user_register():
    user_username = input('Enter username : ')
    user_password = input('Enter password : ')
    user_age = int(input("enter your age: "))
    if user_age >= 18:
        user_pass[user_username] = user_password
    else:
        print("Your under age to register!")
    


while True:
    print(user_pass)
    user_choice = input('Do you want to register or login or exit? ')
    if user_choice == 'login':
        user_name = input('Enter your user name: ')
        if user_name in user_pass:
            user_login()  
        else:
         print('User not in data base. Please Register first')

    elif user_choice == 'register':
        user_register()

    elif user_choice == 'exit':
        exit()
        
    else:
        print('Invalid choice!')

    
