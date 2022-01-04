file = open( "input.txt", "r")
template = file.readline().strip()
file.readline()

rules = {}
for line in file:
    splitted = line.strip().split(" -> ")
    rules[ splitted[0] ] = splitted[0][0] + splitted[1] + splitted[0][1]

pairs = {}
for key in rules.keys():
    pairs[ key ] = 0

for c in range( len(template) - 1):
    pairs[ template[c:c+2] ] += 1

stepsAmount = 40
for step in range(stepsAmount):
    pairsCopy = dict(pairs)
    for key in pairsCopy.keys():
        output = rules[ key ]
        pairs[ output[0:2] ] += pairsCopy[ key ]
        pairs[ output[1:3] ] += pairsCopy[ key ]
        pairs[ key ] -= pairsCopy[ key ]

counter = [0] * (ord('Z') - ord('A') + 1)
for p in pairs.keys():
    counter[ord('Z') - ord(p[0])] += pairs[p]
    counter[ord('Z') - ord(p[1])] += pairs[p]

counter[:] = [int(x / 2 + 0.5) for x in counter if x > 0]
print( max(counter) - min(counter) )

