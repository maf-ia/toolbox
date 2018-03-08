import math

sign = lambda x: math.copysign(1, x)

def dichotomy( f, a, b, delta ): 
    aa = f(a)
    bb = f(b)
    if abs(bb - aa) < delta:
        return a
    
    c = (a+b)/2.0
    cc = f(c)
    if sign( cc ) == sign( aa ):
        return dichotomy( f, c, b, delta )
    else:
        return dichotomy( f, a, c, delta )
