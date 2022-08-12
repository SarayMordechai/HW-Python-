"""
Student:Saray Mordehai
ID: 316153592
Assignment no.4
Program:vigenere.py

#A program that asks the user to choose between e and d to enter an encryption key and file
name if he selects e will print the decryption results to the file, 
if he selects d will print the decryption results to the screen
"""

def add_letters(s1 ,s2):
    '''A function that receives 2 strings and returns the sum of the letter'''
    #Definition of the dictionary outside the function
    dict1={chr(ord('a')+i):0+i for i in range(26)}
    #Check if the strings are 1 length and if it is Latin
    if len(s1)==1 and s1.isalpha():
        if len(s2)==1 and s2.isalpha():
            #Add the sum of the letters and return the numeric value
            char=dict1[s1.lower()]+dict1[s2.lower()]
            return(chr(char%26+(ord("a"))))
    return None


def add_string(str1,str2):
    '''A function that receives 2 strings and returns the sum 
    of the letters in their order and length'''
    #Check whether the string is from Latin letters
    if str1.isalpha()==False or str2.isalpha()==False: 
        return None
    #Add the sum of the letters of the two strings to one string
    lst1 = ""
    lene = min(len(str1),len(str2))
    for i in range(lene):
        lst1+= add_letters(str1[i],str2[i])
    return lst1


def vigenere_encrypt(s,k):
    '''A function that receives a string s and a key k and 
    returns the result The encryption of s using the key k.'''
    if k.isalpha()==False: #If K from Latin letters
        return None
    size= (len(s)/len(k))+1
    kye=k*(int(size))#Multiply k by the size of s
    lst=""
    for i in s: #Returns the encrypted text
        if i.isalpha()==True:
            lst+=i
    return add_string(kye,lst)


def vigenere_decrypt(w,k):
    '''A function that receives a string w and a key k and 
    returns the resultDeciphering w using the k key.'''
    dict1={chr(ord('a')+i):0+i for i in range(26)}
    dict2={0+i:chr(ord('a')+i) for i in range(26)}
    w=w.lower()
    word= ""
    for i in w: #Returns the encrypted text
        if i.isalpha()==True:
            word+=i
    if k.isalpha()==False:
        return None
    size= (len(word)/len(k))+1
    key=k*(int(size))
    lst2=""
    for i in range(len(word)): #Returns the decoded text
        lst2+= dict2[(dict1[word[i]]-dict1[key[i]]+26)%26]
    return lst2


def main():
    '''A function that asks the user to select between e and d if he selects e will
    print the decoding results to a fileif he selects d will print the decoding
    results to the screen'''
    try:
        letter = input("enter 'd' or 'e': ")
        
        #If the user clicked e read from a file and write to a separate file
        if letter == 'e' :
            key=input("enter a encryption key:")
            ntxt=input("enter a file name:")
            file1=open(ntxt,"r")
            txt=file1.read()
            file1.close()
            enctxt= vigenere_encrypt(txt,key)
            newName=ntxt.replace(".txt",".vig")
            newfile= open(newName,"w")
            newfile.write(enctxt)
            newfile.close()
            print("Encryption completed")
            
            #If the user pressed d read from a file and write to the screen
        if letter == 'd':
            key=input("enter a decryption key:")
            ntxt=input("enter a file name:")
            file1=open(ntxt,"r")
            txt=file1.read()
            file1.close()
            print(vigenere_decrypt(txt,key))
        else:
            return
    except IOError:
            print("File not accessible")
main()