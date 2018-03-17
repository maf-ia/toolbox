 
from PIL import Image 

def gridImage( filename ):
    img = Image.open( filename )
    pix = img.load()
    w,h = img.size
    
    img1 = Image.new("RGB", (w/2,h), "#444")
    img2 = Image.new("RGB", (w/2,h), "#444")
    img3 = Image.new("RGB", (w,h), "#444")
    img4 = Image.new("RGB", (w,h), "#444")
    
    pix1 = img1.load()
    pix2 = img2.load()
    pix3 = img3.load()
    pix4 = img4.load()
    
    oldColor = pix[0,0]
    for posy in range( h ):
        for posx in range( w ):
            backColor = pix[posx, posy]
            if posx%2 == 0:
                pix1[posx/2,posy] = backColor
            if posx%2 == 1:
                pix2[posx/2,posy] = backColor
            if (posx+posy)%2 == 0:
                pix3[posx,posy] = backColor
                pix4[posx,posy] = oldColor
            if (posx+posy)%2 == 1:
                pix3[posx,posy] = oldColor
                pix4[posx,posy] = backColor
            oldColor = backColor
                

    img1.save( "grid1.png" )
    img2.save( "grid2.png" )
    img3.save( "grid3.png" )
    img4.save( "grid4.png" )