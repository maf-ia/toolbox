

class PNGReader:
    def __init__( self, filename ):
        self.filename = filename
        
    def computeCRC( self, data ):
        import zlib 
        
        checksum = zlib.crc32(data)
        checksum &= 2**32-1
        return checksum
        
    def checkSignature( self, data ):
        if data[:8] == b'\x89PNG\r\n\x1a\n':
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
            val += "Bad CRC - computed " + str(self.computeChunkCRC( chunk )) + ", found " + str(chunk[3])
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
        return (length, chunkType, chunkData, crc )
    
    
    def displayHeader( self ):
        with open( self.filename, "rb" ) as fic:
            data = fic.read()
        val = ""
        val += self.checkSignature( data )
        header = self.readChunk( data[8:] )
        val += self.checkHeader( header )
        
        print( val )
    
    def readChunks( self ):
        with open( self.filename, "rb" ) as fic:
            data = fic.read()
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
        
        