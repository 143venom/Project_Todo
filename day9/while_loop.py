# programme need:
# Ask user name
# Get user input in string
# Ask user to print user name for five times. 

print("WELCOME COME TO WHILE LOOP PROGRAME")
user_name = str(input("Enter Your Name: "))
print(f"\n Hi, {user_name}")

def print_five_times():
    count = 0
    while count < 5:
        print(user_name)
        count += 1
        
ask_user = input(f"{user_name} can i print your name for five times, (y/n): ")
if ask_user == 'y':
    print('printing Your name five times')
    print_five_times()
else:
    print('programme closed')

    

