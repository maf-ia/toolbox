
class playfair:
    def __init__( self, di = 1, dj = 1 ):
        self.grid = dict()
        self.setDelta( di, dj )
        
    def setAlphabet( self, alphabet ):
        cpt = 0
        for i in range(5):
            for j in range(5):
                self.grid[(i,j)] = alphabet[cpt]
                cpt += 1
                
    def setDelta( self, di, dj ):
        self.di = di
        self.dj = dj
                
    def getCoord( self, letter ):
        for i in range(5):
            for j in range(5):
                if self.grid[(i,j)] == letter:
                    return (i,j)
        return (0,0)
    
    def encrypt( self, msg ):
        ret = ""
        for i in range( int(len(msg)/2) ):
            l1 = msg[2*i]
            l2 = msg[2*i+1]
            c1 = self.getCoord( l1 )
            c2 = self.getCoord( l2 )
            if c1[0] == c2[0]:
                i1 = c1[0]
                i2 = c2[0]
                j1 = (c1[1]+self.dj)%5
                j2 = (c2[1]+self.dj)%5
            elif c1[1] == c2[1]:
                j1 = c1[1]
                j2 = c2[1]
                i1 = (c1[0]+self.di)%5
                i2 = (c2[0]+self.di)%5
            else:
                i1 = c1[0]
                j1 = c2[1]
                i2 = c2[0]
                j2 = c1[1]
            ret += self.grid[(i1,j1)] + self.grid[(i2,j2)]
        return ret
                
    def decrypt( self, msg ):
        ret = ""
        for i in range( int(len(msg)/2) ):
            l1 = msg[2*i]
            l2 = msg[2*i+1]
            c1 = self.getCoord( l1 )
            c2 = self.getCoord( l2 )
            if c1[0] == c2[0]:
                i1 = c1[0]
                i2 = c2[0]
                j1 = (c1[1]-self.dj)%5
                j2 = (c2[1]-self.dj)%5
            elif c1[1] == c2[1]:
                j1 = c1[1]
                j2 = c2[1]
                i1 = (c1[0]-self.di)%5
                i2 = (c2[0]-self.di)%5
            else:
                i1 = c1[0]
                j1 = c2[1]
                i2 = c2[0]
                j2 = c1[1]
            ret += self.grid[(i1,j1)] + self.grid[(i2,j2)]
        return ret


