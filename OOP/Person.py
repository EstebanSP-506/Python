class Person(object):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    def self_introduction(self):
        print "Hello, my name is {}, I am {} years old and I am from {}".format(self.name,self.age,self.location)

p1 = Person("Esteban",29,"Atenas")
p2 = Person("Ana",17,"La Garita")
p3 = Person("Stheve",33,"Tibas")
p4 = Person("Todd",33,"Seattle")

p1.self_introduction()
p2.self_introduction()
p3.self_introduction()
p4.self_introduction()


