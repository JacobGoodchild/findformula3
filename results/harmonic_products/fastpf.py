"""Fast exact partial fractions for  prod_b (p+b)^(-e_b)  (distinct integers b, exponents e_b>=1).
returns {(b,u): Fraction}  meaning sum c/(p+b)^u."""
from fractions import Fraction as Fr
from functools import lru_cache
def _binom_series(c, e, n):
    """series of (1+eps/c)^(-e) up to eps^(n-1), c nonzero Fraction/int, e>=1"""
    out = [Fr(1)]
    for j in range(1, n):
        # coefficient of eps^j in (1+u)^(-e) with u=eps/c : (-1)^j C(e+j-1,j) / c^j
        num = Fr(1)
        for t in range(j): num = num * (e + t) / (t + 1)
        out.append(num * (-1)**j / Fr(c)**j)
    return out
def _mul(a, b, n):
    r = [Fr(0)]*n
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b):
            if i+j >= n: break
            r[i+j] += x*y
    return r
@lru_cache(None)
def pf(exps):
    """exps: tuple of (b,e) sorted"""
    res = {}
    for (b, e) in exps:
        ser = [Fr(1)] + [Fr(0)]*(e-1)
        for (b2, e2) in exps:
            if b2 == b: continue
            c = b2 - b
            s = _binom_series(c, e2, e)
            pref = Fr(1) / Fr(c)**e2
            s = [pref*x for x in s]
            ser = _mul(ser, s, e)
        for j in range(e):
            if ser[j] != 0:
                res[(b, e-j)] = res.get((b, e-j), 0) + ser[j]
    return res
