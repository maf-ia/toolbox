from PIL import Image 
import sys

def asort(d):
     return sorted(d.items(), key=lambda x: x[1])

def detectRandomness( filename ):
    img = Image.open( filename )
    pix = img.load()
    w,h = img.size
    block = 8
    
    xsize = int(w/block)
    ysize = int(h/block)
    
    count = dict()
    avg_count = dict();
    
    for i in range(block):
        for j in range(block):
            for y in range(j*ysize,(j+1)*ysize):
                for x in range(i*xsize,(i+1)*xsize):
                    c = pix[x,y]
                    if (i,j,c) in count:
                        count[(i,j,c)] = count[(i,j,c)]+1
                    else:
                        count[(i,j,c)] = 1
            for elt in count:
                if elt[0] == i and elt[1] == j:
                    v = float(count[elt])/float(block*block)
                    if elt[2] in avg_count:
                        avg_count[elt[2]] = avg_count[elt[2]] + v
                    else:
                        avg_count[elt[2]] = v

    # -----------------------------------------------------------
    # Calculate a dispersion (deviation) from average count
    # for each color as sum of each block's squared difference
    # -----------------------------------------------------------
    d = dict()
    dmax = 0
    
    for i in range(block):
        for j in range(block):
            for elt in count:
                if elt[0] == i and elt[1] == j:
                    color = elt[2]
                    color_count = count[elt]
                    if color in d:
                        d[color] = d[color] + (color_count-avg_count[color])**2
                    else:
                        d[color] = (color_count-avg_count[color])**2
                    if d[color] > dmax:
                        dmax = d[color]
                        
    # -----------------------------------------------------------
    # Calculate average dispersion, just for information
    # -----------------------------------------------------------
    avg_d = float(sum([d[v] for v in d])) / float(len(d))
    print( "MAX disp: ", dmax, "; AVG: ", avg_d )
    
    # -----------------------------------------------------------
    # Find the largest "gap" in array, use it as edge
    # -----------------------------------------------------------
    d2 = asort(d)
    gap = 0
    gap_disp = 0
    prev_disp = -1
    
    for color in d2:
        disp = d[ color[0] ]
        if prev_disp > 0:
            if disp - prev_disp > gap:
                gap = disp - prev_disp
                gap_disp = float(prev_disp) + float(disp - prev_disp)/2.0
        prev_disp = disp
        
    print( "GAP: ",gap_disp," +/- ",gap/2 )
    

    # -----------------------------------------------------------
    # Blacken pixels with disp < $limit
    # -----------------------------------------------------------
    limit = gap_disp    # Note: we can use intval($dmax/3);
    
    for x in range(w):
        for y in range(h):
            c = pix[x,y]
            if d[c] < limit:
                pix[x,y] = (0,0,0)
    
        
    img.save( "solve.png" )
    print( "DONE" )
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        detectRandomness(sys.argv[1])
    else:
        print("Usage: pyhton detectrandomness image.png")
