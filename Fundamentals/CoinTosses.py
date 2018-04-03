# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!

import random

def tossingCoinXTimes(x):
    headsCounter = 0
    tailsCounter = 0
    print "Starting the program..."
    for index in range(1,x+1):
        if round(random.random()) != 0:
            coin = "tail!"
            tailsCounter+=1
        else:
            coin = "head!"
            headsCounter+=1
        print "Attempt #"+str(index)+": Throwing a coin... It's a "+coin+" ... Got "+str(headsCounter)+"head(s) so far and "+str(tailsCounter)+" tail(s) so far"
    print "Ending the program, thank you!"

tossingCoinXTimes(5000)


tossingCoinXTimes(5)
tossingCoinXTimes(10)
tossingCoinXTimes(100)