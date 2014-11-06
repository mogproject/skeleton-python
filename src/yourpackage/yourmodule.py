def your_function(x):
    ret = 0
    if x % 2:
        ret |= 1
    if x < 10000:
        ret |= 2
    if x == 10000:
        ret |= 4
    if x % 9 == 7:
        ret |= 8
    if x / 2000 == 6:
        ret |= 16
    return ret
