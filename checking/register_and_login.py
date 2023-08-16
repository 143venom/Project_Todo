import sqlite3

def create_table():
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def main():
    while True:
        choice = input("Do you want to register (R) or login (L)? ").lower()

        if choice == 'r':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
        elif choice == 'l':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login_user(username, password):
                print("Login successful! Welcome back, " + username + "!")
            else:
                print("Invalid credentials" + username + ". Please try again.")
        else:
            print("Invalid choice. Please enter 'R' for registration or 'L' for login.")

        rerun = input("Do you want to run the program again? (yes/no): ").lower()
        if rerun != 'yes':
            print("Thank you for using the Login System. Goodbye!")
            break
            
    

if __name__ == "__main__":
    main()
