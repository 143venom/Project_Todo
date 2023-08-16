def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("user_credentials.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("user_credentials.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        stored_username, stored_password = line.strip().split(":")
        if stored_username == username and stored_password == password:
            print("Login successful!")
            return
    
    print("Invalid credentials.")

def main():
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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
