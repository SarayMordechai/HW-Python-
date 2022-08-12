

A program that produces 100,000 random numbers and from them tests some of them prime
"""
import math
import random

def is_prime(num):
    '''Function that checks if the number is prime'''
    if (num % 2 == 0):
        if (num != 2):
            return  False
    for i in range(3,int(math.sqrt(num))+1, 2):
        if (num%i == 0):
            return False
    return True

#Grill 100,000 random numbers in range
list1=[random.randint((10**9)/2 , 10**9) for X in range(0 , 100000)]

#Checks which of the numbers drawn is prime
list2 = [n for n in list1 if is_prime(n)]

#Returns the length of the list
prime=(len(list2))

e=2.71828182846 #Value of the number e

#Percentage of prime numbers from the numbers drawn
print(f"density of primes: {prime/len(list1):.4f}") 

#Comparing the result to the expected density
print(f"expected density: {1/math.log((10**9) , e):.4f}")
