# ------------------------------------------------- #
# Title: Assignment07_AK
# Description: This program demonstrates error handling and stores/reads data from a binary file.
# ChangeLog: (Who, When, What)
# Andrew Kehl,11.27.2021,Created Script
# ------------------------------------------------- #
''' fd fd fd '''

class user_input():
#################################################################################
#Numerical input with if/else error handeling
    while (True):
        a_number = input("Enter a Number: ")
        if a_number.isnumeric():
            break
        else:
            print('Enter Only Numbers Please.')
        continue
#################################################################################
#Alphabetical input with Exception error handling
    while (True):
        try:
            a_word = str(input("Enter a Word: "))
            if a_word.isnumeric():
                raise Exception('Enter Only Words Please.')
        except Exception as e:
            print(e)
            continue
        else:
            break
#################################################################################
print('Thank you!\n')
input('Now for the fun part!\nWe will now turn this into pickles!!\n  -Press any key to Continue-\n')
print('***!!Pickles!!***')

import pickle
with open('PickleData.dat', 'wb') as f: #Creates pickle file 'PickleData.Dat' in local directory
    pickle.dump(user_input(), f) #Saves data input to pickle file 'PickleData.dat' in local directory

my_pickled_data = pickle.dumps(user_input())
print(f"This is my pickled data: {my_pickled_data}\n")

my_unpickled_data = pickle.loads(my_pickled_data)
print(f"This is my unpickled data: {my_unpickled_data.a_number}, {my_unpickled_data.a_word}")
