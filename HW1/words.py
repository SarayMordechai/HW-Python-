"""
Created on Mon Oct 26 21:17:26 2020

@author: saray mordehai
ID:316153592
Assignment no. 1
Program: words.py
"""

#Receive a sentence from the user
sentence = input (("enter a sentenc:"))

#Print the sentence for each line separately:
i = 0
for i in range(len(sentence)):
         if sentence[i]==" ":
            print()
         else:
            print(sentence[i], end="")
