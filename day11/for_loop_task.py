fruits_list = ['banana','apple','guava','orange','papaya','watermelon','jack fruit','mango']
ignor_fruits_list = ['banana','papaya','orange']
for a in fruits_list:
    # print(a)
    # if a not in ['banana','orange','papaya']: # or
    if a not in ignor_fruits_list:
        print(a)