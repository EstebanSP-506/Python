# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if len(list_one)!=len(list_two):
    print "The lists have a different length, therefore:"
    print "The lists are not the same."
else:    
    same = True
    for index in range(0,len(list_one)):
        if list_one[index] != list_two[index]:
            same = False
            break
    if same == True:
        print "The lists are the same."
    else:
        print "The lists are not the same."
