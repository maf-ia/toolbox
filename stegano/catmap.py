import PIL.Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave

# load image
im = array(PIL.Image.open("o.jpg"))
N = im.shape[0]

# create x and y components of Arnold's cat mapping
x,y = meshgrid(range(N),range(N))
xmap = (2*x+y) % N
ymap = (x+y) % N

for i in xrange(N+1):
    result = PIL.Image.fromarray(im)
    result.save("cat_%03d.png" % i)
    im = im[xmap,ymap] 
