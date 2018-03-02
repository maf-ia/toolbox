from PIL import Image 


img = Image.open( "spiral-1.gif")
#img = img.convert('RGB')
pix = img.load()
w,h = img.size

#backColor = pix[posx, posy]
for posy in range( h ):
    for posx in range( w ):
        backColor = pix[posx, posy]

# si palette
palette = image.getpalette()
print(palette)

from PIL import ImageDraw
img = Image.new("RGB", (5000,1000), "#444")
draw  =  ImageDraw.Draw(img) 
draw.line( ( (offX,offY), (newOffX,newOffY) ) )
img.save( "sawed.png" )
