"""

#A program that reads from a file a quadratic matrix  and a list of numbers 
that represents a polynomial and prints the results of the placement of the
 matrix in a polynomial
"""
def matrix_scalar_mult(matrix , scalar):
    '''A function that multiplies a matrix in a scalar'''
    return[[matrix[j][i]*scalar for i in range (len(matrix[0]))]
           for j in range(len(matrix))]

def matrix_add(matrix1 , matrix2):
    '''A function that connects two matrixes and returns their sum'''
    return[[matrix1[i][j]+matrix2[i][j] for j in range (len(matrix1[0]))]
           for i in range(len(matrix2))]


def matrix_mult(matrix1, matrix2):
    '''A function that multiplies two matrixes and returns their sum'''
    return [[sum([matrix1[i][j]*matrix2[j][c] for j in range(len(matrix2))])
            for c in range(len(matrix2[1]))]for i in range(len(matrix1))]

def identy_matrix(n):
    '''A function that returns the unit matrix'''
    return[[1 if i == j else 0 for i in range(n)] for j in range(n)]


def matrix_polynom(p, A):
    '''A function that receives a list that represents a polynomial and 
    a square matrix and calculates the result of the matrix in the polynomial'''

    #The coefficient of the first limb is double the identy matrix
    for i in range(0,len(p)):
        if i == 0:
            finalsum = matrix_scalar_mult(identy_matrix(len(A)) ,p[0])

    #Multiply the matrix by the power of the polynomial
        else:
            result = A
            for j in range(i-1):
                result=matrix_mult(result , A)
            result=matrix_scalar_mult(result , p[i])
            finalsum = matrix_add(finalsum, result)
    return finalsum



def print_matrix(matrix, file):
    '''A function that returns the wanted matrix Into a file'''
    f=open(file ,"w")
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            wanted=(f"{matrix[i][j]:.2f}")
            f.write(str(wanted) + " ")
        f.write("\n")
    f.close()


def main():
    '''A function that reads a matrix and a polynomial from a file makes it a list
    and prints the matrix calculation in the polynomial into a separate file'''
    op=open("matrix_input.txt")
    text=op.readlines()
    for i in range (len(text)):
        text[i] = text [i].split() #Make the string a list of strings
        for j in range (len(text[i])): #make the list of strings of a list
            text[i][j] = float(text[i][j])
    matrix=text[0 : -1] #The matrix
    poly=text[-1] #The polynomial
    matrix2=(matrix_polynom(poly, matrix))
    print_matrix(matrix2, "matrix_output.txt")

main()
