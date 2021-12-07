def Part1( nrs ):
    nrs.sort()
    mediana = nrs[ int(len(nrs) / 2) ]
    s = 0
    for nr in nrs:
        s += abs( mediana - nr )

    print( "Part1: " + str( s ) )

def Part2( nrs ):
    avg0 = int( sum( nrs ) / len( nrs ) + 0.5 )
    avg1 = int( sum( nrs ) / len( nrs ) )

    s0 = 0
    s1 = 0

    for nr in nrs:
        s0 += (abs( nr - avg0 ) / 2) * (abs( nr - avg0 ) + 1 )  
        s1 += (abs( nr - avg1 ) / 2) * (abs( nr - avg1 ) + 1 )

    print( "Part2: " + str( min( int(s0), int(s1) ) ) )

file = open( "input.txt", "r" )

nrs = []

for line in file:
    for nr in line.split( "," ):
        nrs.append( int(nr) )

Part1( nrs )
Part2( nrs )