class MathDojo(object):
    def __init__(self):
        self.result = 0

    # Methods
    def add(self, *args):
        value = 0
        for arg in args:
            if type(arg) == list:
                tempVal = 0
                for element in arg:
                    tempVal+=element
                value+=tempVal    
            elif type(arg) == tuple:
                tempVal = 0
                for element in arg:
                    tempVal+=element
                value+=tempVal    
            else:
                value+=arg
        self.result+=value
        return self
    def subtract(self, *args):
        value = 0

        for arg in args:
            if type(arg) == list:
                tempVal = 0
                for element in arg:
                    tempVal+=element
                value+=tempVal    
            elif type(arg) == tuple:
                tempVal = 0
                for element in arg:
                    tempVal+=element
                value+=tempVal    
            else:
                value+=arg
        self.result-=value
        return self



md1 = MathDojo()
md2 = MathDojo()

print md1.add([1], 3,4).add([3,5,7,8],(2,3), [2,4.3,1.25]).subtract(2,(15,3), [2,3], [1.1,2.3]).result

print md2.add(2).add(2,5).subtract(3,2).result
