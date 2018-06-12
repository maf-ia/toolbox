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

import math
from PIL import Image 
from sklearn import linear_model

def redresse( filename ):
    img = Image.open( filename )
    img = img.convert('RGB')
    pix = img.load()
    w,h = img.size

    listex = []
    listey = []
    for posy in range( h ):
        for posx in range( w ):
            backColor = pix[posx, posy]
            if backColor != (255,255,255):
                listex.append(posx)
                listey.append(posy)
    print(backColor)
    reg=linear_model.LinearRegression()
    x = listex
    train_data_X = map(lambda x: [x], list(x))
    train_data_Y = list(listey)
    reg.fit(train_data_X, train_data_Y)
    print (reg.coef_[0], math.atan(reg.coef_[0])*360/(2*math.pi) )
    angle = math.atan(reg.coef_[0])*360/(2*math.pi)
    rot = img.rotate( angle, expand=1 )
    rot.save( "red_" + filename )
    
    img = Image.open( "red_" + filename )
    img = img.convert('RGB')
    pix = img.load()
    w,h = img.size

    for posy in range( h ):
        for posx in range( w ):
            backColor = pix[posx, posy]
            if backColor == (0,0,0):
                pix[posx, posy] = (255,255,255)
            
    img.save("red_"+filename)