usernames_list = ["alis", "amir", "bhupesh", "diksan", "anjan"]
username = input("Enter Your User name: ")
if username in usernames_list:
    print(f"{username} is in database, Login Successfull.")
else:
    print(f"{username} isnot in database, Login failed.")