import json

def custom_datetime(year, month, day, hour, minute, second):
    # Validate input values
    if not (1 <= month <= 12) or not (1 <= day <= 31) or \
       not (0 <= hour < 24) or not (0 <= minute < 60) or not (0 <= second < 60):
        return None
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Leap year check
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29
    
    total_days = sum(days_in_month[:month]) + day - 1
    
    total_seconds = ((total_days * 24 + hour) * 60 + minute) * 60 + second
    
    return total_seconds

# Example usage
year = 2023
month = 7
day = 25
hour = 14
minute = 30
second = 0

timestamp = custom_datetime(year, month, day, hour, minute, second)
print("Custom Timestamp:", timestamp)


def register_user():
    user_Name = input('Enter Your User Name: ')
    user_Pass = input('Enter Your Password: ')
    user_list = {user_Name:user_Pass}
    f = open('user_db.txt','a')
    f.write(json.dumps(user_list))
    f.close()
    print(custom_datetime('year', 'month', 'day', 'hour', 'minute', 'second'))

while True:

    choice = input('login: ')

    if choice == 'l':
        register_user()
    else:
        print('invalid choice')


