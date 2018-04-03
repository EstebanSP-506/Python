xyz = 10
me = {
    'key' : 'Value',
    'name' : 'Esteban',
    'age' : 29
}

def evenPrinter(a):
    for index in range(a):
        if index % 2 == 0:
            print index

evenPrinter(50)
print xyz
print me

print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
Triple quotations allow us to comment across multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
'''

name = "Zen"
print "My name is", name

name = "Zen"
print "My name is " + name


first_name = "Zen"
last_name = "Coder"
age = "older than you"
print "My name is {} {} who is {}".format(first_name, last_name, age)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"



x='1'
y = 2
print x + str(y)
print str(x) + str(y)
print int(x) + y
print x + y


x = [5,34,10,1,6]
x.append(2)
x

if not x: 
    print "x doesnt exist"
else:
    print x


if x not exists:
    print "x doesnt exist"
else:
    print x