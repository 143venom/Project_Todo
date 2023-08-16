
    # Strings
def string():
    string_var = "Hello, Mindrisers!"
    print("String:", string_var)
    print("Length of String:", len(string_var))
    print("Indexing Example:", string_var[0])  
    print("Slicing Example:", string_var[7:13])  

    # Lists
def lists():
    list_var = ['a', 'b', 'c', 'd', 'e', 1, 2, 3]
    print("List:", list_var)
    print("Length of List:", len(list_var))
    print("Indexing Example:", list_var[2])  
    print("Slicing Example:", list_var[2:6])  

    # Tuples
def tuples():
    tuple_var = (10, 20, 30, 40, 50, 'a', 'b', 'c' )
    print("Tuple:", tuple_var)
    print("Length of Tuple:", len(tuple_var))
    print("Indexing Example:", tuple_var[5])  
    print("Slicing Example:", tuple_var[1:6])  

    # Sets
def sets():
    set_var = {1, 2, 3, 3, 4, 5, 'hello', 'mindriser'}
    print("Set:", set_var)
    print("Length of Set:", len(set_var))
    print("Sets do not support indexing./ Sets do not support slicing.")

    # Dictionaries
def dictionaries():
    dict_var = {"name": "Subhash", "age": 26, "city": "Kathmandu", "profession":"programmer"}
    print("Dictionary:", dict_var)
    print("Length of Dictionary:", len(dict_var))
    print("Indexing Example:", dict_var["city"])  
    print("Dictionaries do not support slicing.")

def title():
    id_sl = '<---------------indexing and slicing--------------->' 
    i_s = id_sl.upper()
    print(i_s)

# def select_function():
#     sfgb = '<------Select Function Given Below:------>'
#     print(sfgb)


while True :
    title()
    print('<------Select Function Given Below:------>')
    list = ['S:Strings', 'L:Lists', 'T:Tuples', 'SE:Set', 'D:Dictionaries']
    for a in list:
        print(a)
    select_function = input('Select any function: ')
    if select_function == 's':
        string()
    elif select_function == 'l':
        lists()
    elif select_function == 't':
        tuples()
    elif select_function == 'se':
        sets()
    elif select_function == 'd':
        dictionaries() 
    else :
      print("Invalid list select")

    restart = input("Do you want to check another function? (yes): ")
    if restart != "yes":
        break
    

        


