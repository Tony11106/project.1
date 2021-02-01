#Project 1
#amaldo36@uic.edu
#Tony Maldonado-Perez
#I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s
#Academic Integrity standards. Signed: Anthony Maldonado-Perez

import math

#First

#use x as a variable to store as a float
x = float(input("Please provide a value for x: "))
# solve for y in order to print to the thousandths decimal
y = (math.sqrt(x**2 +9)- 7)/(2**x + 5)
print("The value of y is:  %.3f"%y)
print('-'*40)

#Second
#use string as my input to be read
#string = input("Please enter a string: ")
#the count of e's and 4's
#count = 0
#tried to loop character in string
# for c in string:
#   if c == 'e' or c == '4' + 1
#percentage = count/len(string)*100

#print decimal to the tenth decimal place
#print("The percentage is  %.1f %%"%percentage)
#print('-'*40)

#Third

# use bits as my input to be read
bits = int(input("Please enter a number of bits: "))

#convert bits to gb and remove gn bits
gb = bits//(1000*1000*1000*8)
bits = bits%(1000*1000*1000*8)

#convert bits to mb and remove mb bits
mb = bits//(1000*1000*8)
bits = bits%(1000*1000*8)

#calculate bits to kb
kb = bits//(1000*8)

#print gb ,mb, and kb
print("The number of bits given is equal to ",gb," gigabytes ",mb," megabytes ",kb," kilobytes")
