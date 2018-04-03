# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output should be:
# new_list = ['hello','world']

new_list = []
for item in word_list:
    if char in item:
        new_list.append(item)
    else:
        continue

print new_list