"""
Created on Wed Oct 28 15:19:00 2020

@author: saray mordehai
ID:316153592
Assignment no. 3
Program: root.py
"""
#Variables received from the user
num=int(input("Enter a number:"))
guess=int(input("Make a guess:"))
precision=float(input("Enter precision:"))

#While the condition greater than epsilon is met:
while abs(guess**2-num) > precision:
    guess =(guess+(num/guess))/2
    print(guess)

#While the condition is equal to or less than epsilon met:
if abs(guess**2-num) <= precision:
    print("sqrt(" , num,")" ,"=", guess)