def Part1():
    file = open("input.txt", "r")

    firstLine = file.readline()
    counters = [0] * ( len(firstLine) - 1 )
    file.seek(0)

    linesCounter = 0

    for line in file:
        linesCounter += 1
        for x in range(len(counters)):
            counters[x] += ord(line[x]) - ord('0');

    file.close()

    gamma = 0
    for x in range(len(counters)):
        gamma += ( ( counters[x] - linesCounter / 2 ) > 0 ) << ( len(counters) - x - 1 )

    print( gamma * ( ( ( 1 << len(counters) ) - 1 ) - gamma ) )

def Calculate( nrs, binaryLength, biggest ):
    for currentBitOffset in reversed( range( binaryLength ) ):
        onesCounter = 0
        for nr in nrs:
            onesCounter += ( nr & ( 1 << currentBitOffset ) ) != 0

        bit = ( ( onesCounter >= len( nrs ) / 2 ) == biggest ) << currentBitOffset
        nrs[:] = [ x for x in nrs if ( x & ( 1 << currentBitOffset ) ) == bit ]

        if len(nrs) == 1:
            return nrs[ 0 ]

def Part2():
    file = open("input.txt", "r")

    firstLine = file.readline()
    binaryLength = len(firstLine) - 1
    file.seek(0)

    nrs = [ int( x, 2 ) for x in file ]
    file.close()

    oxygen = Calculate( list( nrs ), binaryLength, True )
    co2 = Calculate( list( nrs ), binaryLength, False )

    print( oxygen * co2 )

Part1()
Part2()