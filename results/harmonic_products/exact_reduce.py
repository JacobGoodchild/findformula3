"""
Exact reduction of S_q = sum_{k>=1} prod_{j=0}^q H_{k+j} / prod_{j=0}^q (k+j)  to multiple zeta values (MZVs).

Pure rational algebra (python Fractions + sympy partial fractions). No numerics.
Values are dicts {(tpow, word): Fraction}; word=() means the number 1, otherwise an admissible
index tuple (s1>=2, s1 = exponent of the LARGEST summation index), meaning zeta(s1,...,sr)=sum_{n1>...>nr>=1}.
T stands for the regularised divergent harmonic number H_K (K -> infinity); all T-dependence must cancel.
"""
import sys
from fractions import Fraction as Fr
from functools import lru_cache
from math import comb

# ---------- small linear-combination helpers ----------
def vadd(a, b, c=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + c*v
        if r[k] == 0: del r[k]
    return r
def vscale(a, c):
    return {k: v*c for k, v in a.items()} if c != 0 else {}
def vTmul(a, j=1):
    return {(k[0]+j, k[1]): v for k, v in a.items()}

# ---------- quasi-shuffle with the single letter (1) ----------
def stuffle_with_1(word):
    """return dict word->mult for  (1) * word  (stuffle / quasi-shuffle)"""
    out = {}
    n = len(word)
    for i in range(n+1):                     # insert 1 at position i
        w = word[:i] + (1,) + word[i:]
        out[w] = out.get(w, 0) + 1
    for i in range(n):                       # merge 1 into letter i
        w = word[:i] + (word[i]+1,) + word[i+1:]
        out[w] = out.get(w, 0) + 1
    return out

@lru_cache(None)
def reg(word):
    """stuffle-regularised value of Z_K(word) as K->inf: dict {(tpow, admissible word): coeff}"""
    if len(word) == 0:
        return {(0, ()): Fr(1)}
    if word[0] >= 2:
        return {(0, word): Fr(1)}
    # leading 1:  (1)*w' = sum_v mult_v v ,  w=(1,w') appears with multiplicity j = (#leading ones of w)
    j = 0
    while j < len(word) and word[j] == 1: j += 1
    wp = word[1:]
    prod = stuffle_with_1(wp)
    res = vTmul(reg(wp))
    for v, mult in prod.items():
        if v == word:
            assert mult == j, (word, mult, j)
            continue
        res = vadd(res, reg(v), -mult)
    return vscale(res, Fr(1, j))

@lru_cache(None)
def Hpow_words(r):
    """H_{p-1}^r as sum of nested sums Z_{p-1}(w):  dict word -> coeff"""
    cur = {(): 1}
    for _ in range(r):
        nxt = {}
        for w, c in cur.items():
            for v, m in stuffle_with_1(w).items():
                nxt[v] = nxt.get(v, 0) + c*m
        cur = nxt
    return cur

@lru_cache(None)
def E_reg(m, s):
    """regularised  sum_{p=1}^K H_p^m / p^s  (K->inf), value dict"""
    res = {}
    for l in range(m+1):
        for w, c in Hpow_words(m-l).items():
            res = vadd(res, reg((s+l,)+w), comb(m, l)*c)
    return res

def Hrat(n, m=1, s=1):
    """exact finite sum  sum_{p=1}^{n} H_p^m / p^s"""
    tot = Fr(0); H = Fr(0)
    for p in range(1, n+1):
        H += Fr(1, p)
        tot += H**m / Fr(p)**s
    return tot
def Hn(n):
    return sum((Fr(1, i) for i in range(1, n+1)), Fr(0))

from fastpf import pf
from itertools import product as _iprod
def _compositions(l, parts):
    if parts == 1:
        yield (l,); return
    for i in range(l+1):
        for rest in _compositions(l-i, parts-1):
            yield (i,) + rest
@lru_cache(None)
def pf_dshift(a, l, s):
    """partial fractions in p of  d_a(p)^l / p^s  as tuple of (b,u,coeff) meaning coeff/(p+b)^u
       d_a = -sum_{i=0}^{a-1} 1/(p-i) for a>0 ;  +sum_{i=1}^{|a|} 1/(p+i) for a<0"""
    if a > 0: poles = [-i for i in range(a)]; sign = -1
    else:     poles = [i for i in range(1, -a+1)]; sign = 1
    from math import factorial
    acc = {}
    for comp in _compositions(l, len(poles)):
        mult = factorial(l)
        for k in comp: mult //= factorial(k)
        ex = {}
        for b, k in zip(poles, comp):
            if k: ex[b] = ex.get(b, 0) + k
        ex[0] = ex.get(0, 0) + s
        for (b, u), c in pf(tuple(sorted(ex.items()))).items():
            acc[(b, u)] = acc.get((b, u), 0) + (sign**l)*mult*c
    return tuple((b, u, c) for (b, u), c in acc.items() if c != 0)

@lru_cache(None)
def reduce_sum(m, a, s, n0):
    """value of  sum_{n>=n0} H_n^m / (n+a)^s   (n0>=1, n+a>=1 on the range)"""
    if a == 0:
        res = E_reg(m, s)
        head = Hrat(n0-1, m, s)
        return vadd(res, {(0, ()): head}, -1) if head != 0 else res
    p0 = n0 + a
    assert p0 >= 1
    if m == 0:
        if s >= 2:
            fin = sum((Fr(1, p**s) for p in range(1, p0)), Fr(0))
            return vadd({(0, (s,)): Fr(1)}, {(0, ()): fin}, -1) if fin != 0 else {(0, (s,)): Fr(1)}
        else:
            return vadd({(1, ()): Fr(1)}, {(0, ()): Hn(p0-1)}, -1)
    res = reduce_sum(m, 0, s, p0)
    for l in range(1, m+1):
        for (b, u, c) in pf_dshift(a, l, s):
            res = vadd(res, reduce_sum(m-l, b, u, p0), comb(m, l)*c)
    return res

def S_exact(q):
    # expand prod_{j=0}^q (x + y_1+...+y_j) * prod_{j=0}^q y_j,  y_i = 1/(k+i)
    poly = {(0, (0,)*(q+1)): Fr(1)}
    for j in range(q+1):
        new = {}
        for (xp, ex), c in poly.items():
            # term x
            key = (xp+1, ex); new[key] = new.get(key, 0) + c
            for i in range(1, j+1):
                e2 = list(ex); e2[i] += 1
                key = (xp, tuple(e2)); new[key] = new.get(key, 0) + c
        poly = new
    total = {}
    for (m, ex), c in poly.items():
        ex2 = tuple((i, e+1) for i, e in enumerate(ex))
        for (a, u), cf in pf(ex2).items():
            total = vadd(total, reduce_sum(m, a, u, 1), c*cf)
    return total

if __name__ == "__main__":
    q = int(sys.argv[1])
    tot = S_exact(q)
    bad = {k: v for k, v in tot.items() if k[0] != 0}
    print("q =", q, " T-terms (must be empty):", bad)
    for (t, w), c in sorted(tot.items(), key=lambda kv: (sum(kv[0][1]), kv[0][1])):
        print(f"  {c} * zeta{w}  (weight {sum(w)})")
