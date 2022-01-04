import time
file=open("input.txt","r")

def Approximation( start, end ):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

startTime = time.time()

openSet = []
gScore = []
fScore = []
map = []
offsets = [ (1,0), (-1,0), (0,1),(0,-1) ]
cameFrom = {}
for line in file:
    map.append([ int(x) for x in line.strip() ])


originalMap = list(map)
dimension = 4
for i in range(dimension):
    for row in originalMap:
        aa = i + 1
        map.append([ ((x + aa) + int((x+aa)/10)) % 10 for x in row ] )

for row in map:
    originalRow = list(row)
    for i in range(dimension):
        aa = i + 1
        row.extend( [ ((x + aa) + int((x+aa)/10)) % 10 for x in originalRow ] )
    fScore.append( [ 9999999 ] * len(map[0]) )
    gScore.append( [ 9999999 ] * len(map[0]) )


start = (0,0)
end = (len(map[0])-1, len(map) - 1)

openSet.append( start )
gScore[ start[1] ][ start[0] ] = 0
fScore[ start[1] ][ start[0] ] = Approximation( start, end )

while len(openSet) > 0:
    current = openSet[0]
    minValue = fScore[current[1]][ current[0]]
    for element in openSet:
        if fScore[element[1]][element[0]] < minValue:
            current = element
            minValue = fScore[element[1]][element[0]]

    if current == end:
        break

    openSet.remove(current)
    for offset in offsets:
        point = (current[0] + offset[0], current[1] + offset[1])

        if point[0] < 0 or point[1] < 0 or point[0] >= len(map[0]) or point[1] >= len(map):
            continue

        potentialScore = gScore[ current[1] ][ current[0] ] + map[ point[1] ][point[0]]
        if potentialScore < gScore[ point[1] ][ point[0] ]:
            cameFrom[ point ] = current
            gScore[ point[1] ][ point[0] ] = potentialScore
            fScore[ point[1] ][ point[0] ] = potentialScore + Approximation( current, end )
            if not point in openSet:
                openSet.append( point )


current = end
path = [ current ]
pathCost = 0
while current in cameFrom:
    pathCost += map[current[1]][current[0]]
    current = cameFrom[current]
    path.append( current )
print(pathCost)

print(time.time()-startTime)

