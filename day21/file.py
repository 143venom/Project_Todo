import json

def login():
    user_username = input('Enter your username : ')
    f = open('F:\Python\day21/user_db.txt','r')
    a = f.read()
    list_user = a.split('-')
    for i in list_user:
        if i != '':
            user_dict = json.loads(i)
            if user_username in user_dict:
                password = user_dict.get(user_username)
                user_pass = input('Enter Your password: ')
                if user_pass == password:
                    print('login successfull')
                else:
                    print('password not match with given user name')

            print('invalid user name')
    f.close()
            
def register():        
    user_username = input('Enter username : ')
    user_password = input('Enter password : ')
    user_info = {f"{user_username}:{user_password}\n"}
    f = open('F:\Python\day21/user_db.txt','a')
    f.write(json.dumps(user_info))
    f.close()

while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")