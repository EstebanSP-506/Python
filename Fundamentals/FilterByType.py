sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

mainList = [sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]
for index in range(0,len(mainList)-1):
    if isinstance(mainList[index],int):
        if mainList[index] < 100:
            print str(mainList[index])+" --> That's a small number"
        else:
            print str(mainList[index])+" --> That's a big number!"
    elif isinstance(mainList[index],str):
        if len(mainList[index]) < 50:
            print str(mainList[index])+" --> Short sentence."
        else:
            print str(mainList[index])+" --> Long sentence."
    elif isinstance(mainList[index],list):
        if len(mainList[index]) < 10:
            print str(mainList[index])+" --> Short list."
        else:
            print str(mainList[index])+" --> Long list."

