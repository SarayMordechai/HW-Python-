
#Receive a sentence from the user
sentence = input (("enter a sentenc:"))

#Print the sentence for each line separately:
i = 0
for i in range(len(sentence)):
         if sentence[i]==" ":
            print()
         else:
            print(sentence[i], end="")
