
class asm:
    def __init__( self, archsize ):
        self.archsize = archsize
        self.mask = ( 2**archsize - 1 )
        self.mask8 = ( 2**(archsize-8) - 1 ) << 8
        self.mask16 = ( 2**(archsize-16) - 1 ) << 16
        self.mask32 = ( 2**(archsize-32) - 1 ) << 32

    # ADD
    def add8( self, dest, val ):
        return (dest & self.mask8) + ( (dest + val) & 0xFF )
    
    def add16( self, dest, val ):
        return (dest & self.mask16) + ( (dest + val) & 0xFFFF )
    
    def add32( self, dest, val ):
        return (dest & self.mask32) + ( (dest + val) & 0xFFFFFFFF )
    
    def add64( self, dest, val ):
        return (dest + val) & 0xFFFFFFFFFFFFFFFF
    
    # ROL
    def rol_one( self, val ):
        return ( (val << 1) & self.mask) + ( (val >> (self.archsize-1) ) & 0x1 )    

    def rol( self, val, nb ):
        for i in range(nb):
            val = self.rol_one( val )
        return val

    # ROR
    def ror_one( self, val, size ):
        return ( (val >> 1) & self.mask) + ( (val << (self.archsize-1)) & self.mask )

    def ror( self, val, nb ):
        for i in range(nb):
            val = self.ror_one( val )
        return val    



