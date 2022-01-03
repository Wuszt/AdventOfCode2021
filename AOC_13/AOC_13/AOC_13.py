dots = set()
file = open( "input.txt", "r" )

def PrintIt( dots, width, height ):
    for y in range(height):
        for x in range(width):
            if (x,y) in dots:
                print( "#", end="")
            else:
                print( ".", end="")
        print()

for line in file:
    if line == "\n":
        break
    coords = line.strip().split(',')
    dots.add( (int(coords[0]), int(coords[1])) )

folds = []
for line in file:
    splitted = line.strip().split('=')
    folds.append((splitted[0][len(splitted[0])-1],int(splitted[1])))

size = [ 0,0 ]
for fold in folds:
    index = fold[0] == 'y'
    size[ index ] = fold[1]

    offset = ( (index == 0) * fold[1] * 2, (index == 1) * fold[1] * 2)
    dotsCopy = set(dots)
    for dot in dotsCopy:
        if dot[index] > fold[1]:
            dots.add( (abs(offset[0] - dot[0]), abs(offset[1] - dot[1]) ) )
            dots.remove( dot )

    print(len(dots))
PrintIt( dots, size[0], size[1])