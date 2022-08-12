"""
A program that reads numbers from a file and checks whether the number 
is a prime number and prints the result next to it
"""
import random

def get_even_odd_parts(n):
    '''get a number and return the even and 
       the odd part.'''
    if n%2 == 1: #Checks if the number is odd
        return 0,n
    else: #Checks if the number is even
        count = 0
        while n%2 != 1:
            count+=1
            n//=2
        return count,n

def is_probably_prime(n,num_iterations):
    '''get a number and the number iterations 
       and return true if the number is probably a 
       prime and false if is not a prime.'''
    s,t = get_even_odd_parts(n-1)
    for i in range (num_iterations):
         if is_suspected_prime(n,t,s) != True:
             return False
    return True

def modular_power(a,b,n):
    """ computes a**b (mod n) using iterated squaring
        assumes b is a nonnegative integer. """
    l=[]
    while b>0:
        if b%2==1:
            l=[1]+l
        else:
            l=[0]+l
        b//=2
    result=1
    for k in l:
        result=(result**2)%n
        if k==1:
            result=(result*a)%n
    return result


def is_suspected_prime(n,t,s):
    '''return true or false if the 
       number is suspected a prime.'''
    a = random.randint(2,n)
    d = modular_power(a,t,n)
    
    if d == 1 or d == n-1:
        return True
    i=1
    for i in range(s-1):
        d = modular_power(d,2,n)
        if d == n-1:
            return True
    return False


def main():
    '''The primary function that reads a file and prints 
    next to each parent number is primary'''
    fo=open('input_ex1.txt', 'r')
    file=fo.readlines()
    fo.close()
    for i in range(len(file)):
        file[i]=int(file[i].replace("\n", ""))
    newfile=open('output_ex1.txt', 'w')
    for line in file:
        if is_probably_prime(line,10)==0:
            newfile.write('{} is not prime\n'.format(line))
        else:
            newfile.write('{} is prime\n'.format(line))
    newfile.close()
    
main()

