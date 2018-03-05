import tempfile as tf
from subprocess import call

def readLine( filename ):
    tempfile = tf.NamedTemporaryFile(suffix=".txt").name
    print( tempfile )
    call( ["tesseract", filename, tempfile[:-4], "-psm 8" ] )

    with open( tempfile, "r" ) as fic:
        msg = fic.read()
        msg = msg.replace( "\n", "" )
    
    call( ["rm", tempfile ] )
    return msg
