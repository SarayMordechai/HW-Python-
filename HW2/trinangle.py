"""
Student:Saray Mordehai
ID: 316153592
Assignment no.1
Program:trinangle.py

#The program receives a string from the user
and prints the string in an asterisks triangle
"""
import math

#Defining variables
X=1
place=1

#Receive a sentence from the user
s= input("Enter a sentence:")

#Calculate the square root of the number of characters in a sentence
rows = int(math.sqrt(len(s)))
if rows**2 != len(s):
    rows+= 1
    s +=(" "*(rows**2-(len(s))))

#Print the triangle with the input inside
print(" "*(rows), "*")

for i in range(0, rows):
    print(" "*(rows-i) + "*" + (s[i**2 : (i+1)**2]) +"*")

print("*"*((rows + 1)*2 + 1))
