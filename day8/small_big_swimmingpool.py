# programme age wise swimming pool
# programme need:
# take age from customer
# for age 10 year small pool
# for age greater then 10 year less than 50 year 10 feet pool

def customer_age(age):
    if age >=5 and age<=10:
        print("got to small pool")
    elif age >=10 and age <=50:
        print("got to 10' pool" )
    else:
        print("you cannot swim")

while True:
    customer = int(input('Enter your age:'))
    customer_age(customer)
    next_customer = input("Do you want to check another customer? (y/n): ")
    if next_customer != 'y':
        break
