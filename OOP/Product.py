class Product(object):
    # Attributes & Constructors
    def __init__(self, price, item_name, weight, brand):
        # Initialize Attributes as self.attribute = attribute
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    # Methods
    def displayInfo(self):
        print 'Item Name: '+self.item_name
        print 'Brand : '+self.brand
        print 'Price: '+str(self.price)
        print 'Status: '+self.status
        print 'Weight: '+self.weight
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        self.price+=self.price*tax
        return self
    def returnProduct(self, reason):
        if reason == "defective":
            self.status = 'defective'
            self.price = 0
        elif reason == 'like new':
            self.status = "for sale"
        elif reason == 'used':
            self.status = "used"
            self.price-=self.price*0.2
        else:
            print "Return not accepted as the reason is not clear, try it again with the correct reason codes: 'defective' 'like new' or 'used'"
        return self

product1 = Product(150,"Bookity Book",'3lb',"D'Originals")

product1.displayInfo()
product1.addTax(0.30).sell().displayInfo()
product1.returnProduct('used').displayInfo()

product2 = Product(250,"A Little Something",'15lb',"ShutUp&Pay")

product2.displayInfo()
product2.addTax(0.15).sell().displayInfo()
product2.returnProduct('didnt like it').displayInfo()