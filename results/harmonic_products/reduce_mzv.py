"""Express every MZV that appears in S_q as a Q-combination of products of single zeta values (and zeta(5,3) at weight 8).
Each reduction is found by PSLQ at 150 digits (these are the standard MZV evaluations, e.g. Borwein-Girgensohn for weight<=7);
then S_q is assembled exactly with rational arithmetic.  Results are cached in mzv_table.json."""
import json, os, sys, itertools
from fractions import Fraction as Fr
from mpmath import mp, mpf, pslq
from cypari import pari
DPS = 150
def val(w):
    pari.set_real_precision(DPS+10)
    mp.dps = DPS
    if len(w) == 1: return mpf(str(pari('zeta(%d)' % w[0])))
    return mpf(str(pari('zetamult(%s)' % list(w))))
GENS = {2: (2,), 3: (3,), 5: (5,), 7: (7,), 9: (9,)}
def monomials(weight):
    """multisets of generators {2,3,5,7,9} summing to weight, plus (5,3)-type extra generator at weight 8"""
    gens = [2, 3, 5, 7, 9]
    res = []
    def rec(i, rem, cur):
        if rem == 0: res.append(tuple(cur)); return
        if i == len(gens): return
        g = gens[i]
        c = 0
        while c*g <= rem:
            rec(i+1, rem-c*g, cur+[g]*c); c += 1
    rec(0, weight, [])
    res = [tuple(r) for r in res]
    names = [tuple(sorted(r)) for r in res]
    out = [(n, ) for n in names]
    mons = [list(n) for n in names]
    if weight == 8: mons.append(['z53'])
    return mons
def mval(m):
    v = mpf(1)
    for g in m: v *= (val((5, 3)) if g == 'z53' else val((g,)))
    return v
TABLE = 'mzv_table.json'
table = json.load(open(TABLE)) if os.path.exists(TABLE) else {}
def reduce_word(w):
    key = ','.join(map(str, w))
    if key in table: return table[key]
    wt = sum(w)
    mons = monomials(wt)
    mp.dps = DPS
    x = val(w)
    rel = pslq([x] + [mval(m) for m in mons], maxcoeff=10**15, maxsteps=10**7)
    assert rel is not None and rel[0] != 0, ("no relation", w)
    res = {}
    for r, m in zip(rel[1:], mons):
        if r: res['*'.join(map(str, m))] = str(Fr(-r, rel[0]))
    table[key] = res
    json.dump(table, open(TABLE, 'w'), indent=1)
    return res
def assemble(tot):
    out = {}
    for (t, w), c in tot.items():
        assert t == 0
        if w == (): red = {'': '1'}
        else: red = reduce_word(w)
        for mon, cf in red.items():
            out[mon] = out.get(mon, 0) + c*Fr(cf)
    return {k: v for k, v in out.items() if v != 0}
if __name__ == "__main__":
    from exact_reduce import S_exact
    q = int(sys.argv[1])
    res = assemble(S_exact(q))
    print("S_%d =" % q)
    for k in sorted(res, key=lambda s: (sum(int(x) if x.isdigit() else 8 for x in s.split('*') if x), s)):
        print("   ", res[k], "*", k or "1")
