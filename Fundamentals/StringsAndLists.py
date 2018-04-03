words = "It's thanksgiving day. It's my birthday,too!"
print(words.index('day'))
print(words.find('day'))
print(words.replace('day','month', 1))
print(words.replace('day','month'))

print(type(words))

x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))

y = ["hello",2,54,-2,7,12,98,"world"]
print(y[0],y[len(y)-1])

test = [19,2,54,-2,7,12,98,32,10,-3,6]
test.sort()
first_half = []
new_list = []
for index in range(0,len(test)-1):
    if index < len(test)/2 :
        first_half.append(test[index])
    else:
        new_list.append(test[index])
new_list.insert(0,first_half)
print new_list



