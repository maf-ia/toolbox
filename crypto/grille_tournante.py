import itertools

grid1 = []
grid1.append("agtorw")
grid1.append("ginrey")
grid1.append("leneln")
grid1.append("koielu")
grid1.append("errars")
grid1.append("mlonxl")

grid2 = []
grid2.append("rlthww")
grid2.append("enivae")
grid2.append("lhdean")
grid2.append("thesre")
grid2.append("miiran")
grid2.append("rxtoxa")

p = []
p.append( [(0,0),(0,5),(5,5),(5,0)] )
p.append( [(0,1),(1,5),(5,4),(4,0)] )
p.append( [(0,2),(2,5),(5,3),(3,0)] )
p.append( [(1,0),(0,4),(4,5),(5,1)] )
p.append( [(1,1),(1,4),(4,4),(4,1)] )
p.append( [(1,2),(2,4),(4,3),(3,1)] )
p.append( [(2,0),(0,3),(3,5),(5,2)] )
p.append( [(2,1),(1,3),(3,4),(4,2)] )
p.append( [(2,2),(2,3),(3,3),(3,2)] )


def computeWord( key, grid ):
    res = ""
    for row in range(4):
        letters = []
        for i in range(9):
            x,y = p[i][(key[i]+row)%4]
            letters.append( (x,y, grid[x][y]) )
        letters.sort(key=lambda (x,y,z): (x*10+y)*26+(ord(z)-ord('a')))
        res += "".join([l[2] for l in letters])
    return res

for ite in itertools.product(range(4),repeat=9):
    key = list(ite)
    v = computeWord( key, grid2)
    print(key,v)

