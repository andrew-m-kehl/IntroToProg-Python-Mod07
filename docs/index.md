Andrew Kehl  
11/27/21  
UW Foundations in programming  
Assignment 07  
https://kehlstorm.github.io/IntroToProg-Python-Mod07/
https://github.com/kehlstorm/IntroToProg-Python-Mod07/blob/main/Assignment07_AK.py

### Introduction
The objective of this assignment is to create a new script that demonstrates how pickling and structured error handling work. 
 
# Assignment07_AK.py
Assignment07_AK.py is a simple program that requests a number and a word. It then converts them by pickling into a .dat file and then shows you your information in .dat format. 

## Inputs & Error Handling

### Numerical Error Handling
Error Handling was coded into the number input via an if/else statement inside a while(True) loop using the isnumeric function. It asks if the entry is a number. If so, break the loop. Otherwise (else) print a statement and continue the loop. (Figure 1.1 & Figure 1.2)
```python
    while (True):
        a_number = input("Enter a Number: ")
        if a_number.isnumeric():
            break
        else:
            print('Enter Only Numbers Please.')
        continue
```
Figure 1.1 - Error Handling with an If/Else statement.  
  
![NEHUI](https://raw.githubusercontent.com/kehlstorm/IntroToProg-Python-Mod07/main/docs/Numerical%20Error%20Handling%20UI.jpg)  
Figure 1.2 - Numerical Error Handling User Interface.  

### Alphabetical Error Handling
Error Handling was coded into the word input via a try/except statement inside a while(True) loop again using the isnumeric function. It asks if the entry is a number. If so, raise the exception and print a statement and continue the loop. If not (else) break. (Figure 1.3 & Figure 1.4)
```python
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
```  
Figure 1.3 - Error Handling with a try/except statement.  
  
![AEHUI](https://raw.githubusercontent.com/kehlstorm/IntroToProg-Python-Mod07/main/docs/Alphabeticall%20Error%20Handling%20UI.jpg)  
Figure 1.4 - Alphabetical Error Handling User Interface.  

Both Numerical and Alphabetical input loops are included into a class called 'user_input'. (Figure 1.5)
```python
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
```
Figure 1.5 - user_input class.  
### Pickling our data
Now we open a new file on the local database for writing to store our data. We call the user_input data and tell the pickle function where to put it.  (Figure 2.1)
```python
import pickle
with open('PickleData.dat', 'wb') as f:
    pickle.dump(user_input(), f)
``` 
Figure 2.1 - Saving data to a local database using the pickle function.  
Using the pickle.dumps function, we can read and print the data as the computer sees it. (Figure 2.2 & Figure 2.3)
```python
my_pickled_data = pickle.dumps(user_input())
print(f"This is my pickled data: {my_pickled_data}\n")
```
Figure 2.2 - Printing pickled data.  
  
![PDUI](https://raw.githubusercontent.com/kehlstorm/IntroToProg-Python-Mod07/main/docs/Pickled%20Data%20UI.jpg)  
Figure 2.3 - Pickled data user interface.  
  
Finally, we use the pickle.loads function to unpickle the data to a format we all can read. (Figure 2.4 & Figure 2.5)
```python
my_unpickled_data = pickle.loads(my_pickled_data)
print(f"This is my unpickled data: {my_unpickled_data.a_number}, {my_unpickled_data.a_word}")
```
Figure 2.4 - Printing unpickled data.  
  
![UPDUI](https://raw.githubusercontent.com/kehlstorm/IntroToProg-Python-Mod07/main/docs/Unpickled%20Data.jpg)  
Figure 2.5 - Unpickled data user interface.  
  
## Conclusion
Assignment07_AK.py is a new script that demonstrates how structured error handling works with user inputs and how pickling and unpickling data works. 
