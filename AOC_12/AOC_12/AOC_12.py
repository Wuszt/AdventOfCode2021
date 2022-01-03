nodes = {}
file = open( "input.txt", "r" )

def AddNode( name1, name2 ):
    if not name1 in nodes:
        nodes [ name1 ] = []
    nodes[ name1 ].append( name2 )

for line in file:
    splitted = line.rstrip().split('-')
    AddNode( splitted[0], splitted[1])
    AddNode( splitted[1], splitted[0])
    
resultsAmount = 0
visitedNodes = set()
visitedTwice = False
def ProcessNode2(name):
    global resultsAmount, visitedTwice
    wasVisitedTwice = visitedTwice
    if name in visitedNodes:
        if visitedTwice or name == "start":
            return
        visitedTwice = True

    if name == "end":
        resultsAmount +=1
        return

    if not name.isupper():
        visitedNodes.add(name)

    for connection in nodes[ name ]:
        ProcessNode2( connection )

    if (wasVisitedTwice or not visitedTwice) and not name.isupper():
        visitedNodes.remove(name)

    visitedTwice = wasVisitedTwice

def ProcessNode1(name):
    global resultsAmount
    if name in visitedNodes:
        return

    if name == "end":
        resultsAmount +=1
        return

    if not name.isupper():
        visitedNodes.add(name)

    for connection in nodes[ name ]:
        ProcessNode1( connection )

    if not name.isupper():
        visitedNodes.remove(name)

#ProcessNode1("start")
ProcessNode2("start")
print(resultsAmount)
