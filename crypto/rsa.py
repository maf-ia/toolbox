
def txt2int( text ):
    return reduce( lambda x,y: (x<<8)+y, map(ord, text) )

def int2txt( number, size ):
    text = "".join([chr((number>>j)&0xff) for j in reversed(range(0, size<<3,8) )] )
    return  text.lstrip("\x00")
