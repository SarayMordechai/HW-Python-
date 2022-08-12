"""
Student:Saray Mordehai
ID: 316153592
Assignment no.4
Program:grades.py

#A program that reads data from 2 files the data The program will read into two dictionaries,
the program prints on the screen the students name, his grade point average, 
the gradereceived the most times and the list of grades received more than once
"""

def converting_to_dict(file_name,dictionery):
    '''A function that defines two dictionaries'''
    try: 
        file = open(file_name,"r")
        #A loop that puts the contents of the file into dictionaries
        for line in file.readlines():
            newline = line.split()
            if file_name == 'grades.txt':
                dictionery[ newline[0]] = [float(i) for i in newline[1:]]
            elif file_name == 'students.txt': 
                dictionery[ newline[0]] = " ".join(newline[1:])
    except IOError:
          print("File not accessible")

def bestgrade(dict_grad,dict_stud):
    '''A function that returns the average grade per student'''
    lst=[[sum(dict_grad[i])/len(dict_grad[i]), dict_stud[i]] for i in dict_stud]
    lst.sort(reverse=True)
    return lst


def commongrade(dict_grad):
    '''A function that returns the score obtained the most times'''
    commongrade={}
    grades=(sum(list(dict_grad.values()),[]))
    for i in grades: 
        if i in sum(list(commongrade.values()),[]):
            continue
        if grades.count(i) not in list(commongrade.keys()): #Is the score in the dictionary
            commongrade[grades.count(i)]=[i]
        elif grades.count(i) in list(commongrade.keys()): #Score count
            commongrade[grades.count(i)]+=[i]
    return commongrade[max(commongrade)]


def get_common_elements(lstinlst):
    '''Function that receivesList of lists and returns a list of the organs
    that have appeared on more than one list'''
    #A loop that puts students' grades in a list of lists
    lst = [[int(i[j]) for j in range(len(i))] for i in lstinlst] 
    set1=set()
    for i in range (len(lst)):
        for j in range(i+1, len(lst)):
            grop=(set(lst[i]) & set(lst[j]))
            set1|=grop
    return set1


def wrong_id(dict_grad, dict_stud):
    '''A function that checks whether the input is correct'''
    for Id in dict_grad: #Checks if there is an incorrect ID number
        if (len(Id)) != 9:
            return False
    for Id in dict_stud:
        if (len(Id)) != 9:
            return False
        #Checks if any ID number appears in one file and in the other does not
    for Id in dict_grad:
        if Id not in dict_stud or len(dict_stud) != len(dict_grad):
            return False
    for i in dict_grad:
        if len(i) == 0:
            return False
    for i in dict_grad.values():
        if len(i)==0: #ID number that does not show scores in the txt.g file
            return False
        #ID number that does not have a name in the file students.txt
    for i in dict_stud.values(): 
        if len(i)==0:
            return False
    return True


def main():
    '''The main function that checks whether the input
    is correct and prints the data to the screen'''
    dict_grad = {}
    dict_stud = {}
    converting_to_dict('grades.txt', dict_grad)
    converting_to_dict('students.txt', dict_stud)
    
    if wrong_id(dict_grad, dict_stud) == False: #Checks if the file is invalid
        print("Not fulfilling all criteria")
    else: #Print the program to output
        lst2=(bestgrade(dict_grad,dict_stud))
        for i in range(len(lst2)):
            print(lst2[i][1],lst2[i][0])
        print("Most common grades:",commongrade(dict_grad))
        print("Grades that more than one student got:"),print(*get_common_elements(dict_grad.values()), sep =",")

main()
