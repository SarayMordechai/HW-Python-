"""
Student:Saray Mordehai
ID: 316153592
Assignment no. 2
Program:histogram.py

#A program that reads a piece of text from the input and prints a histogram 
describing the number of times each letter in ABC appeared on the input.

"""
#Creating a list to contain the a
counters=[0]*26

#Receive a sentence from the user
s= input("enter a string of letters:\n")

#Goes over the list and counts the amount of letters in the sentence
for c in s:
    if c.isalpha():
        counters[ord(c.lower())-ord('a')]+=1

#Print the histogram
for i in range(max(counters), 0 , -1):
    for j in range(0, 26):
        if counters[j] >= i:
            print("* " , end="")
        else:
            print("  ",end="")
    print("")

#Print the letters
print("a b c d e f g h i j k l m n o p q r s t u v w x y z") 