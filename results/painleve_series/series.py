"""u''u - u'^2 = e^{-x} P(u) - 1,  u = sum_k p_k(x) q^k,  q = e^{-x},  p_0 = x.   (arXiv:2606.21145, Habib & Hildebrand)
Exact rational recursion for the polynomials p_k.  Polynomials are lists of Fractions (index = power of x)."""
import sys
from fractions import Fraction as Fr
def padd(a, b, c=1):
    n = max(len(a), len(b)); r = [Fr(0)]*n
    for i, x in enumerate(a): r[i] += x
    for i, x in enumerate(b): r[i] += c*x
    return trim(r)
def trim(a):
    while a and a[-1] == 0: a.pop()
    return a
def pmul(a, b):
    if not a or not b: return []
    r = [Fr(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b): r[i+j] += x*y
    return trim(r)
def pder(a): return trim([i*a[i] for i in range(1, len(a))])
def pscale(a, c): return trim([c*x for x in a])
def solveL(s, r):
    """solve  x p'' - 2 s x p' + s^2 x p - 2(p' - s p) = r  for polynomial p; return (p, residual) where residual is the failed m=0 equation."""
    D = len(r) - 1
    a = [Fr(0)]*(D+2)           # a_0..a_{D+1}; true degree D-1
    for m in range(D, 0, -1):
        rm = r[m] if m < len(r) else Fr(0)
        am = a[m]; am1 = a[m+1] if m+1 < len(a) else Fr(0)
        a[m-1] = (rm - 2*s*(1-m)*am - (m+1)*(m-2)*am1) / (s*s)
    res = (r[0] if r else Fr(0)) - (2*s*a[0] - 2*a[1])
    return trim(a), res
def compute(P, S):
    """P: list of coefficients pi_j; returns list of p_k (k=0..S) and the list of consistency residuals"""
    p = [[Fr(0), Fr(1)]]       # p_0 = x
    resid = []
    # powers of u as series in q: we need [q^{s-1}] P(u); maintain u-series and its powers lazily (recompute with truncation)
    def Pu_coeff(s):
        # [q^s] P(u) = sum_j pi_j [q^s] u^j ; compute u^j truncated to q^s
        tot = []
        pw = [[[Fr(1)]] + [[] for _ in range(s)]]       # u^0
        cur = pw[0]
        for j in range(1, len(P)):
            new = [[] for _ in range(s+1)]
            for a in range(s+1):
                if not cur[a]: continue
                for b in range(s+1-a):
                    if not p[b]: continue
                    new[a+b] = padd(new[a+b], pmul(cur[a], p[b]))
            cur = new
            if P[j] != 0: tot = padd(tot, pscale(cur[s], Fr(P[j])))
        return tot
    for s in range(1, S+1):
        # R_s = sum_{i+j=s, i,j>=1} [ (p_i'' - 2i p_i' + i^2 p_i) p_j - (p_i' - i p_i)(p_j' - j p_j) ]
        R = []
        for i in range(1, s):
            j = s - i
            A = padd(padd(pder(pder(p[i])), pder(p[i]), -2*i), p[i], i*i)
            B = padd(pder(p[i]), p[i], -i)
            C = padd(pder(p[j]), p[j], -j)
            R = padd(R, pmul(A, p[j])); R = padd(R, pmul(B, C), -1)
        rhs = padd(Pu_coeff(s-1), R, -1)       # [q^{s-1}] P(u) - R_s  (the "-1" source only at s=0)
        pk, res = solveL(s, rhs)
        resid.append(res)
        p.append(pk)
        if res != 0: break
    return p, resid
if __name__ == "__main__":
    d = int(sys.argv[1]); S = int(sys.argv[2])
    P = [0]*(d+1); P[d] = 1
    p, resid = compute(P, S)
    print("P = t^%d: computed p_1..p_%d; first nonzero residual:" % (d, len(p)-1), next((i+1 for i, r in enumerate(resid) if r != 0), None))
    mn = min((min(c) if c else 0) for pk in p for c in [pk])
    print("min coefficient overall:", mn, " degrees:", [len(pk)-1 for pk in p[:12]])
