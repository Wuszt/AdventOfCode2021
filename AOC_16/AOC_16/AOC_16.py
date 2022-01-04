file = open("input.txt", "r")

class Data:
    data = ""
    pointer = 0

data = Data()
for c in file.readline():
    value = bin(int(c,16))[2:]
    value = value.zfill( 4 )
    data.data += value

def ReadInteger( data, bitsLength ):
    version = data.data[data.pointer:data.pointer+bitsLength]
    data.pointer+=bitsLength
    return int(version, 2)

def ReadLiteral( data ):
    buffer = ""
    while True:
        buffer += data.data[data.pointer+1:data.pointer+5]
        data.pointer += 5
        if data.data[data.pointer-5] == '0':
            break

    return int(buffer, 2)

def Mul( values ):
    result = 1
    for value in values:
        result *= value
    return result

class Packet:
    version = 0
    id = 0
    literal = -1
    totalLength = -1
    subpacketsAmount = -1
    subpackets = []

    def __init__(self, data):
        self.subpackets = []
        self.version = ReadInteger( data, 3 )
        self.id = ReadInteger( data, 3 )

        if self.id == 4:
            self.literal = ReadLiteral( data )
        else:
            lengthId = ReadInteger( data, 1 )
            if lengthId == 0:
                self.totalLength = ReadInteger( data, 15 )
                startPointer = data.pointer
                while data.pointer < startPointer + self.totalLength:
                    self.subpackets.append( Packet( data ) )
            else:
                self.subpacketsAmount = ReadInteger( data, 11 )
                for i in range(self.subpacketsAmount):
                    self.subpackets.append( Packet( data ) )

    def CalcValue( self ):
        subpacketsValues = [ x.CalcValue() for x in self.subpackets ]
        if self.id == 0:
            return sum( subpacketsValues )
        if self.id == 1:
            return Mul( subpacketsValues )
        if self.id == 2:
            return min( subpacketsValues )
        if self.id == 3:
            return max( subpacketsValues )
        if self.id == 4:
            return self.literal
        if self.id == 5:
            return subpacketsValues[0] > subpacketsValues[1]
        if self.id == 6:
            return subpacketsValues[0] < subpacketsValues[1]
        if self.id == 7:
            return subpacketsValues[0] == subpacketsValues[1]

    def GetVersion( self ):
        sum = self.version

        for sub in self.subpackets:
            sum += sub.GetVersion()
        return sum

mainPacket = Packet( data )
print( mainPacket.CalcValue() )
 


