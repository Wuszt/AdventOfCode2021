daysAmount = 256
newFish = 8
deadFish = 6

buffSize = newFish + 1

buff = [0] * buffSize
file = open("input.txt", "r")
for line in file:
    for nr in line.split( "," ):
        buff[ int(nr) ] += 1

for day in range( 0, daysAmount ):
    buff[ ( day + deadFish + 1 ) % buffSize ] += buff[ day % buffSize ]

print( sum( buff ) )