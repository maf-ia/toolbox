import functools

@functools.lru_cache(maxsize=None)
def Fibonacci( n ):
    if n < 2:
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci( n-2 )

    
    