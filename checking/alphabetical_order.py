

# def generate_random_usernames(num_users):
#     usernames = []
#     for _ in range(num_users):
#         username = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
#         usernames.append(username)
#     return usernames

def main():
    num_users = ['banana','apple','guava','orange','papaya','watermelon','jack fruit','mango']  # Change this value to generate a different number of random usernames

    print("Random Usernames:")
    print(num_users)

    sorted_usernames = sorted(num_users)
    print("\nUsernames in Alphabetical Order:")

    a = 'hello'
    b = a.capitalize() 

    for i in sorted_usernames:
        for a in i:
            print()

if __name__ == "__main__":
    main()