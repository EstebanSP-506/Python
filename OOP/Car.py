class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price>10000:
            self.tax=0.15
        else:
            self.tax=0.12
        self.displayAll()
    def displayAll(self):
        print "Price: "+str(self.price)
        print "Speed: "+self.speed
        print "Fuel: "+self.fuel
        print "Mileage: "+self.mileage
        print "Tax: "+str(self.tax)


car1 = Car(150000,"420mph","Full","120mpg")
car2 = Car(500,"320mph","Full","100mpg")
car3 = Car(300,"120mph","Full","80mpg")
car4 = Car(2000,"60mph","Full","180mpg")
car5 = Car(6000,"40mph","Full","80mpg")
car6 = Car(15700,"220mph","Full","70mpg")
car7 = Car(10000,"40mph","Full","19mpg")
car8 = Car(10001,"450mph","Full","25mpg")
