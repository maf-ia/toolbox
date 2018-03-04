alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
dico = dict()
for i,a in enumerate(alpha):
    dico[a] = ("000000" + bin(i)[2:])[-6:]

def unpadBase64( val ):
    ret = ""
    nbEgal = 0
    for v in val:
        if v != '=':
            ret += dico[v]
        else:
            nbEgal+=1
        
    if nbEgal == 0:
            return ""
    elif nbEgal == 1:
            return ret[-2:]
    else:
            return ret[-4:]
 

with open( "example.txt", "r" ) as fic:
    data = fic.read().split("\n")

ret = ""        
for d in data:
    ret += unpadBase64(d)
        
sol = ""
for i in range( len(ret)/8 ):
    sol += chr(int(ret[i*8:(i+1)*8],2))
print(sol) 
