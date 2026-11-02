import sys, itertools
from mpmath import mp, mpf, zeta, pslq, nstr
from numerics import S
# basis: monomials in zeta(2),zeta(3),zeta(5),zeta(7) (and pi^2 powers via zeta(2)) of weight in [2, W]; zeta(4),zeta(6) expressed via zeta(2)^k
def monomials(W):
    gens = {2:'z2',3:'z3',5:'z5',7:'z7'}
    out = [((),0)]
    def rec(start, cur, w):
        for g in sorted(gens):
            if g < start: continue
            if w+g <= W:
                nc = cur+(g,)
                out.append((nc, w+g)); rec(g, nc, w+g)
    rec(2, (), 0)
    return out
def val(m):
    v = mpf(1)
    for g in m: v *= zeta(g)
    return v
if __name__ == "__main__":
    q = int(sys.argv[1]); dps = int(sys.argv[2])
    W = q+2
    s = S(q, dps)
    mp.dps = dps
    mons = [m for m,w in monomials(W) if w>=2]
    # homogeneous-by-weight: allow all weights 2..W
    vals = [val(m) for m in mons]
    rel = pslq([s]+vals, maxcoeff=10**9, maxsteps=10**6)
    print("q",q,"S=",nstr(s,40))
    if rel is None: print("no relation"); sys.exit()
    print("basis size", len(mons))
    from fractions import Fraction
    c0 = rel[0]
    terms = [(Fraction(-r, c0), m) for r,m in zip(rel[1:], mons) if r]
    print(" + ".join(f"({t})*{'*'.join('z%d'%g for g in m)}" for t,m in terms))
