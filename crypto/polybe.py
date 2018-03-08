

class polybe:
    def __init__( self, alphabet ):
        self.alphabet = [] 
        for row in range( 5 ):
            line = []
            for col in range( 5 ):
                line.append( alphabet[row*5 + col] )
            self.alphabet.append( line )

    def decrypt( self, listnumber ):
        msg = ""
        
        for nb in listnumber:
            msg += self.alphabet[nb/10][nb%10]
        return msg
            