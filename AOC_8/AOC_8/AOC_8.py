import math

digitsSegments = [ [0,1,2,4,5,6], [2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5], [0,1,3,5,6], [0,1,3,4,5,6], [0,2,5], [0,1,2,3,4,5,6], [0,1,2,3,5,6] ]
commons = [ [] ] * 8

for l in range(1,8):
   tmp = [ x for x in range( len(digitsSegments) ) if len(digitsSegments[ x ]) == l ]
   
   common = []
   if len(tmp) > 0:
       common = digitsSegments[ tmp[ 0 ] ]

   for t in tmp:
    common = list( set(common).intersection(digitsSegments[ t ]) )

   for t in tmp:
        commons[l] = common

def CountBits( nr ):
    return bin(nr).count("1")

def Ord( ch ):
    return ord(ch) - ord('a')

def Decode( word, dictionary ):
    decoded = []

    for w in word:
        for d in range(len(dictionary)):
            if math.log(dictionary[d],2) == Ord(w):
                decoded.append( d )

    for x in range(len(digitsSegments)):
        if len(digitsSegments[x]) == len(word) and set(decoded).issubset( digitsSegments[x] ):
            return x

    return -1

def Resolve( word, dictionary ):
    length = len(word)
    common = commons[ length ]

    mask = 0
    for ch in word:
        mask |= 1 << Ord(ch)

    for c in common:
        dictionary[c] &= mask

file = open( "input.txt", "r" )

sum = 0
for line in file:
    dictionary = [ 0b1111111 ] * 7
    [input,output] = line.strip().split( " | " )
    inputs = input.split( " " )
    outputs = output.split( " " )
    for word in inputs:
        Resolve( word, dictionary )

    while True:
        anyNotResolved = False
        for i, dict in enumerate(dictionary):
            if CountBits(dict) > 1:
                for d in dictionary:
                    if CountBits(d) == 1 and d != dictionary[i]:
                        dictionary[i] &= ~d
                anyNotResolved |= CountBits(dict) > 1
        
        if not anyNotResolved:
            break
    
    for w in range(len(outputs)):
         sum += math.pow( 10, len(outputs) - w - 1) * Decode( outputs[w], dictionary )

print(sum)

