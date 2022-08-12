"""

#A program that reads a sentence from a file and write the median , mean 
and their standard deviation to a separate file
"""
def isfloat(s):
    '''A function that receives a string 
    and checks if the string is a decimal number'''

#A string of characters that can appear in the prime number
    characters="+-.0123456789"

    for i in s: #Checks if the number consists of the defined characters
        if not i in characters:
            return False

    if s[0]== ".": #Check if the limb in the first has a point
            return False

    for i in s: #Check if + and - are only in the first position
        if i == "+" or  i =="-":
            if s.index(i)!=0 or s.count(i) >1:
               return False


    if s[0] == "+" or s[0] =="-": #Check if the limb after + and - is a digit
        if not s[1].isdigit():
            return False

#If the first digit is 0 and is not the last the next character is point
    if s[0] == "0" and len(s)>1: #
        if not s[1] == ".":
            return False


#Checking that "." Does not appear more than once
    count = 0
    for i in s: 
        if i == '.':
            count = count + 1
            if count > 1:
                return False

#Checks if the last limb is a number
    if  not s[-1].isdigit():
        return False

    return True

def string_to_list(a):
    '''A function that contains real numbers and puts them on the list'''
    a = a.split()
    for num in a :
        if isfloat(num) == False:
            return None

    return [float(i) for i in a]

def mean(a): 
    '''A function return the avrage'''
    return sum(a)/len(a)


def sd(a):
    '''A function return the standard deviatio'''
    mean = sum(a)/len(a)
    res = 0.0
    for i in a:
        res = res + (i - mean)**2
    return (res/len(a))**0.5


def median(lst):
    '''A function returned the median of the list'''
    lst.sort()
    if len(lst) < 1:
        return(None)
    if len(lst) % 2 == 0:
        median = (lst[len(lst)//2-1: len(lst)//2+1])
        return sum(median) / len(median)
    else:
        return(lst[len(lst)//2])


def main():
    '''A function that reads from a file and writes the median, mean
    and standard deviation'''
    #Reads from the text file and puts the contents of the file into the string
    op=open("numbers.txt")
    text=op.read()
    
    #Check if the numbers in the string are real decimal numbers
    lst=(string_to_list(text))
    
     #If one of the numbers is invalid it will print an invalid number to the file
    if lst == None:
        f=open("stats.txt" ,"w")
        f.write("illegal input")
        f.close()
    
    # If the number is valid it will print the avrage, standard deviation 
    # and the median of the file
    else:
        avrage=(f"{mean(lst):.2f}")
        deviation=(f"{sd(lst):.2f}")
        median1=(f"{median(lst):.2f}")
        f=open("stats.txt" ,"w")
        f.write("mean:" " " + " " + str(avrage) +"\n")
        f.write("standard deviation:" " " + " "+ str(deviation) + "\n")
        f.write("median:" " " + " " +str(median1) + "\n")
        f.close()

main()
