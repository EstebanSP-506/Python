students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def printNames():
    for element in students:
        print element['first_name'], element['last_name']

printNames()

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def printUserNames():
    for userType in users:
        print userType
        count = 0
        charCount = 0
        for element in users[userType]:
            count+=1
            charCount = len(element['first_name'])+len(element['last_name'])
            print str(count)+' - '+element['first_name'].upper()+' '+element['last_name'].upper()+' - '+str(charCount)

printUserNames()



