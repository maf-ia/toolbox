
def rol_one( val, size ):
    return ( (val << 1) & (2**size - 1)) + ( (val >> (size-1) ) & 0x1 )    

def ror_one( val, size ):
    return ( (val >> 1) & (2**size - 1)) + ( (val << (size-1)) & (2**size - 1) )

def rol32( val, nb ):
    for i in range(nb):
        val = rol_one( val, 32 )
    return val

def ror32( val, nb ):
    for i in range(nb):
        val = ror_one( val,32 )
    return val

def rol64( val, nb ):
    for i in range(nb):
        val = rol32one( val, 64 )
    return val    

def ror64( val, nb ):
    for i in range(nb):
        val = ror_one( val, 64 )
    return val


