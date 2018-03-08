

def cesarAscii( msg ):
    ret = []
    for i in range( 256 ):
        ret.append( "".join([chr( (ord(c) + i)%256 ) for c in msg]) )
    return ret
