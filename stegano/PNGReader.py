

# http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html

def readDWORD( data, offset ):
    ret = 0
    for i in range( 4 ):
        ret *= 256
        ret += data[i+offset]
    return ret

def readWORD( data, offset ):
    ret = 0
    for i in range( 2 ):
        ret *= 256
        ret += data[i+offset]
    return ret

def readBYTE( data, offset ):
    return data[ofset]

def writeDWORD( data, offset, val ):
    for i in range( 4 ):
        data[offset+i] = ( (val >> (8*(3-i))) & 0xFF )
    return data

def writeWORD( data, offset, val ):
    for i in range( 2 ):
        data[offset+i] = ( (val >> (8*(1-i))) & 0xFF )
        
    return data

def writeBYTE( data, offset, val ):
    data[offset] = ( val & 0xFF )
    return data

class PNGReader:
    def __init__( self, filename ):
        self.filename = filename
        
    def computeCRC( self, data ):
        import zlib 
        
        checksum = zlib.crc32(data)
        checksum &= 2**32-1
        return checksum
        
    def checkSignature( self, data ):
        if data[:8] == list(b'\x89PNG\r\n\x1a\n'):
            val = "Signature OK\n"
        else:
            val = "Error in signature\n"
        return val
    
    def computeChunkCRC( self, chunk ):
        allData = [ord(c) for c in chunk[1]]
        allData.extend( chunk[2] )
        return self.computeCRC( bytes( allData ) )
    
    def checkChunkCRC( self, chunk ):
        return self.computeChunkCRC( chunk ) == chunk[3]

    def checkHeader( self, chunk ):
        val = ""
        if chunk[1] != 'IHDR':
            val += "Wrong type for header chunk: " + chunk[1] + " found\n"
        elif not self.checkChunkCRC( chunk ):
            val += "Bad CRC - computed " + str() + ", found " + str(chunk[3]) + "\n"
        return val
    
    def readChunk( self, data ):
        length = 0
        for d in data[0:4]:
            length *= 256
            length += d
        chunkType = "".join( [chr(c) for c in data[4:8]] )
        chunkData = data[8:8+length]
        crc = 0
        for d in data[8+length:12+length]:
            crc *= 256
            crc += d
        crc2 = readDWORD(data[8+length:12+length],0)
        print("crc",crc,crc2)
        return (length, chunkType, chunkData, crc )
    
    def buildChunk( self, tag, data ):
        length = len(data)
        chunkData = [0] * (length+12)
        chunkData = writeDWORD( chunkData, 0, length )
        for i in range(4):
            chunkData[4+i] = ord(tag[i])
        for i in range(length):
            chunkData[8+i] = data[i]
        crc = self.computeCRC( bytes(chunkData[4:-4]) )
        chunkData = writeDWORD( chunkData, 8+length, crc ) 
        return chunkData
    
    def displayHeader( self ):
        with open( self.filename, "rb" ) as fic:
            data = list(fic.read())
        val = ""
        val += self.checkSignature( data )
        header = self.readChunk( data[8:] )
        val += self.checkHeader( header )
        headerData = header[2]
        w = readDWORD( headerData, 0 )
        h = readDWORD( headerData, 4 )
        val += "Width: " + str(w) + "\n"
        val += "Height: " + str(h) + "\n"
        
        print( val )
    
    def readChunks( self ):
        with open( self.filename, "rb" ) as fic:
            data = list(fic.read())
        idx = 8
        cpt = 1
        ret = []
        while idx < len( data ):
            chunk = self.readChunk( data[idx:] )
            ret.append(chunk)
            print( cpt, chunk[1], "length:", chunk[0], "- crc test :", self.checkChunkCRC( chunk ) )
            idx += 12 + chunk[0]
            cpt += 1
        return ret
    
    def repairOneByte( self, chunk ):
        initData = [ord(c) for c in chunk[1]]
        size = len( chunk[2] )
        for i in range( size ):
            print(i)
            for j in range( 256 ):
                allData = initData
                val = list(chunk[2])
                val[i] = j
                allData.extend( val )
                if self.computeCRC( bytes( allData ) ) == chunk[3]:
                    print( i, j )
                    return
                
    def modifySize( self, width, height, filename ):
        with open( self.filename, "rb" ) as fic:
            data = list(fic.read())
        header = self.readChunk( data[8:] )
        headerData = header[2]
        print(headerData)
        headerData = writeDWORD( headerData, 0, width )
        headerData = writeDWORD( headerData, 4, height )
        print(headerData)
        chunkData = self.buildChunk( "IHDR", headerData )
        #dataList = list(data)
        for i in range( len(chunkData) ):
            data[8+i] = chunkData[i]
        with open( filename, "wb" ) as fic:
            fic.write(bytes(data))
        
       
png = PNGReader( "test.png" )
png.displayHeader()
for i in range(10):
    png.modifySize( 200+i, 200, "test"+("000"+str(i))[-3:]+".png" )




        