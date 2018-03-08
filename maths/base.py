
def int2str(num, base, sbl=None):
    if not sbl:
        sbl = '0123456789abcdefghijklmnopqrstuvwxyz'
    if len(sbl) < 2:
        raise( ValueError, 'size of symbols should be >= 2' )
    if base < 2 or base > len(sbl):
        raise( ValueError, 'base must be in range 2-%d' % (len(sbl)) )

    neg = False
    if num < 0:
        neg = True
        num = -num

    num, rem = divmod(num, base)
    ret = ''
    while num:
        ret = sbl[rem] + ret
        num, rem = divmod(num, base)
    ret = ('-' if neg else '') + sbl[rem] + ret

    return ret

def str2int(num, base):
    return int(num,base)