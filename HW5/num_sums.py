"""
A program that reads from a row of numbers and prints on the screen the
 number of times the first number can be written as the sum 
 of the other numbers in the list
"""

def num_sums(n,lst):
    '''A function that receives a positive number and a list of numbers 
    and returns the number of ways to write the number as a sum of numbers'''
    if n == 0:
        return 1
    if n < 0:
        return 0
    count=0
    for i in lst:
        count += num_sums(n-i,lst)
    return count

def check_num(lst):
    '''A function that checks whether the input is correct 
    if it does not return an error'''
    if len(set(lst)) != len(lst): #Check the length of the input
        return False
    for i in lst:
        if i.isdigit() == 0: #Check if number
            return False
        if float(i) != int(i): #If an integer
            return False
        if int(i) <= 0: 
            return False
    if len(lst) < 2: #Is the length greater than 2
        return False
    return True

def main():
    '''The main function that reads a file and prints the output of the number
    of times the connection of the numbers can be written'''
    file=open("input_ex2.txt","r")
    lst1=[i.split() for i in file]
    file.close()
    newfile= open("output_ex2.txt","w")
    for lst in lst1:
        if check_num(lst) == False:
            newfile.write("Error \n")
        else:
            newfile.write (str(num_sums(int(lst[0]),[int(i) for i in lst[1:]]))+"\n")
    newfile.close()

main()
