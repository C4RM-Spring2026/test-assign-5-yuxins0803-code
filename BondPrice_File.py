import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy
    t = np.arange(1, n + 1)
    cf = np.full(n, c, dtype=float)
    cf[-1] += face
    pv = 1.0 / (1.0 + r) ** t
    return np.sum(cf * pv)
