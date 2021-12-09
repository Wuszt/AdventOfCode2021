arr = []

def Basin( x, y ):
    if y < 0 or y > len(arr) - 1 or x < 0 or x > len(arr[y]) - 1 or arr[y][x] == 9:
        return 0

    arr[y][x] = 9
    return 1 + Basin( x-1, y ) + Basin( x+1, y ) + Basin( x, y-1 ) + Basin( x, y+1 )

file = open( "input.txt", "r")
for line in file:
    arr.append( [ int(x) for x in line.strip() ] )

sum = 0
largests = [ 0 ] * 3
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if ( x == 0 or arr[y][x] < arr[y][x-1] ) and ( x == len(arr[y]) - 1 or arr[y][x] < arr[y][x+1] ):
            if( y == 0 or arr[y][x] < arr[y-1][x] ) and ( y == len(arr) - 1 or arr[y][x] < arr[y+1][x] ):
                sum += arr[y][x] + 1
                basinSize = Basin( x, y )
                smallest = min(largests)
                if basinSize > smallest:
                    largests[largests.index(smallest)] = basinSize

print( "Part1: " + str(sum) )
print( "Part2: " + str( largests[0] * largests[1] * largests[2]) )