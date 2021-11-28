Andrew Kehl  
11/27/21  
UW Foundations in programming  
Assignment 07  
https://github.com/kehlstorm/IntroToProg-Python-Mod07/blob/main/Assignment07_AK.py

### Introduction
The objective of this assignment is to create a new script that demonstrates how Pickling and Structured error handling work. 
 
# Assignment07_AK.py
Assignment07_AK.py is a simple program that requests a number and a word. It then converts them by pickling into a .dat file and then shows you your information in .dat format. 

## Inputs & Error Handling
I wanted to work on error handling this week since it was a previous question of mine so I thought about what errors humans might make on data entry. Maybe entering numbers for letters and vice versa. 

## Numerical Error Handling
Error Handling was coded into the number input via a if/else statement inside a while(True) loop using the isnumeric function. It asks if the entry is a number. If so, break the loop. Otherwise (else) print a statement and continue the loop. (Figure 1.1)
```
    while (True):
        a_number = input("Enter a Number: ")
        if a_number.isnumeric():
            break
        else:
            print('Enter Only Numbers Please.')
        continue
```
Figure 1.1 - Error Handling with an If/Else statement.
