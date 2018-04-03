for index in range(0,8):
    temp = []
    if index % 2 == 0:
        for subindex in range(0,4):
            temp.append("*")
            temp.append(" ")
        print ''.join(temp)
    else:
        for subindex in range(0,4):
            temp.append(" ")
            temp.append("*")
        print ''.join(temp)

def printCheckerboard(x):
    print "Checkerboard of size "+str(x)+'x'+str(x)
    if x%2 == 0:
        for index in range(0,x):
            temp = []
            if index % 2 == 0:
                for subindex in range(0,x/2):
                    temp.append("*")
                    temp.append(" ")
                print ''.join(temp)
            else:
                for subindex in range(0,x/2):
                    temp.append(" ")
                    temp.append("*")
                print ''.join(temp)
    else:
        for index in range(0,x):
            temp = []
            if index % 2 == 0:
                for subindex in range(0,((x+1)/2)):
                    temp.append("*")
                    temp.append(" ")
                temp.pop()
                print ''.join(temp)
            else:
                for subindex in range(0,((x+1)/2)):
                    temp.append(" ")
                    temp.append("*")
                temp.pop()
                print ''.join(temp)


printCheckerboard(3)
