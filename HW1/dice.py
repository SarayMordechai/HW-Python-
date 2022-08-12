
import random

enter=input("Press Enter to grill the cubes: ")

#Define variables for cube sides:
up   = ' ------- '
empty  = '|       |'
left   = '| O     |'
middle = '|   O   |'
right  = '|     O |'
both   = '| O   O |'

#Assembling the dice:
dice = [(up, empty, empty, middle, empty, empty, up),
        (up, empty, left, empty, empty, right, up),
        (up, empty, left, middle, right, empty, up),
        (up, empty, both, empty, both, empty, up),
        (up, both,empty, middle,empty,both, up),
        (up, empty, both, both, both, empty, up)]

#The number of times the dice were thrown in total
times=1

#Stores the results that came out of the dice throw
lst=[]

#Connecting the smallest results injects 2 dice
s=2

#While the user presses Enter 
while enter ==(""):

#Random shot of two dice
    cube1 = random.randint(1, 6)
    cube2 = random.randint(1, 6)
    print(cube1, cube2)
    print(dice[cube1-1][0], dice[cube2-1][0])
    print(dice[cube1-1][1], dice[cube2-1][1])
    print(dice[cube1-1][2], dice[cube2-1][2])
    print(dice[cube1-1][3], dice[cube2-1][3])
    print(dice[cube1-1][4], dice[cube2-1][4])
    print(dice[cube1-1][5], dice[cube2-1][5])
    print(dice[cube1-1][6], dice[cube2-1][6])
    print(cube1 + cube2)
    enter=input("Press Enter to grill the cubes: ") 
    lst += [cube1+cube2]
    times +=1

#Calculate the sum of the numbers on the dice and its percentage
#Out of the total results:
while s <=12:
    if lst.count(s) > 0:
        print(s, ":", lst.count(s), "times", (lst.count(s)/times)*100, "%")
        s+=1
    else:
         s+=1
