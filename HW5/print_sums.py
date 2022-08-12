"""
Student:Saray Mordehai
ID: 316153592
Assignment no.5
Program:print_sums.py


#A program that reads from an integer file and list and for each line of input 
function will print to the file all the ways to write the integer as a sum of numbers
"""
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


def print_sums(n,parts,file,lst1=[]):
    '''A function that receives a complete nail and a list of numbers and returns all
    the ways in which the number can be written as a sum'''
    if n==0:
        nums=[int(i) for i in lst1]
        file.write(str(sum(nums))+" = "+" + ".join(lst1)+"\n")
        return
    elif n<0:
        return
    for i in range(len(parts)):
        lst1.append(str(parts[i]))
        x=print_sums(n-parts[i],parts,file,lst1)
        del lst1[-1]

def main():
    '''The main function that reads from an integer file and list and prints to
    the file all the ways to write the integer as a sum of numbers'''
    file=open("input_ex3.txt","r")
    lst1=[i.split() for i in file]
    file.close()
    newfile= open("output_ex3.txt","w")
    for lst in lst1: #If the input is incorrect, printing to an error file
        if check_num(lst) == False:
            numbers=" ".join(lst)
            newfile.write(numbers+"\nError\n\n")
        else: 
            lst=[int(i) for i in lst]
            newfile.write(str(lst[0]) +" as sum of " + str(lst[1:])+":\n")
            print_sums(lst[0],lst[1:],newfile)
            newfile.write("\n")
    newfile.close()
main()

