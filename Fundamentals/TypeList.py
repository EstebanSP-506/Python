# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# input
l = [4,[3,"re",56,"f",6],'Hello',5.32,1234567890,'World!',(2,3,4,1),(1,2,4),"This is cool!",[8,9]]

stringContent = []
list_of_lists = []
list_of_tuples = []
sumTotal = 0;a = 0;b = 0;c = 0;d = 0
for index in range(0,len(l)):
    if isinstance(l[index],int) or isinstance(l[index],float) or isinstance(l[index],long):
        sumTotal += l[index]
        a+=1
    elif isinstance(l[index],str):
        stringContent.append(l[index])
        b+=1
    elif isinstance(l[index],list):
        list_of_lists.append(l[index])        
        c+=1
    elif isinstance(l[index],tuple):
        list_of_tuples.append(l[index])
        d+=1


mix = [a,b,c,d]
cons = ("numbers (integers and/or floats)", "strings", "lists", "tuples")
tempo = []
for index in range(0,4):
    if mix[index] != 0:
        tempo.append(cons[index])
print "The list you entered is made of :",', '.join(tempo)
if c!=0:
    print "Lists:",list_of_lists
if d!=0:
    print "Tuples:",list_of_tuples
if b!=0:
    print "Strings:"," ".join(stringContent)
if a!=0:
    print "Sum:",sumTotal

