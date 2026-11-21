
def calculMedian(x):
    x.sort()
    n = len(x)

    if n % 2 != 0:
        return  x[n// 2] 
    else:
        m1 = n // 2
        m2 = n // 2  - 1

        mediane = (x[m1] + x[m2]) / 2

    return  mediane

