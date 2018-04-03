class Animal(object):
    def __init__(self, name):
        # Initialize Attributes as self.attribute = attribute
        self.name = name
        self.health = 100
    # Methods
    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def displayHealth(self):
        print "The remaining health for {} is: {}".format(self.name,self.health)


animal1 = Animal("bambi")
animal1.walk().walk().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    # Methods
    def pet(self):
        self.health+=5
        return self
        
dog1 = Dog("Rufo")
dog1.run().run().run().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name)
        self.health = 170
    # Methods
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        super(Dragon,self).displayHealth()
        print "I am a dragon!"

        
dragon1 = Dragon("Falcor")
dragon1.fly().fly().fly().fly().fly().fly().fly().fly().display_health()


