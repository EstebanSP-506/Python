def odd_even():
    for count in range (1,2001):
        if count % 2 == 0:
            print "Number is "+str(count)+". This is an even number."
        else:
            print "Number is "+str(count)+". This is an odd number."

odd_even()

a = [2,4,10,16]
def multiply(givenList,number):
    temp = []
    for element in givenList:
        temp.append(element*number)
    return temp

b = multiply(a, 5)
print b

def layered_multiples(arr):
    new_array = list()
    for index in range(0,len(arr)):
        new_array.append([1]*arr[index])
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]