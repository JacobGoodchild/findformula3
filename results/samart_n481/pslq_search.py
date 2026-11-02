import sys, re, json
from mpmath import mp, mpf, pslq, log, pi
from cypari import pari
mp.dps = 40
pari.allocatemem(4*10**9); pari.set_real_precision(60)
n481 = mpf(sys.argv[1])
cands = {}
for N, D in [(7,-7),(8,-8),(11,-11),(12,-3),(15,-15),(16,-4),(19,-19),(20,-20),(24,-24),(27,-3),(32,-8),(35,-35),(36,-4),(40,-40),(43,-43),(48,-3),(51,-51),(64,-4),(67,-67),(163,-163),(3,-3),(4,-4)]:
    try:
        mf = pari('mfinit([%d,3,%d],0)' % (N, D)); eb = pari('mfeigenbasis')(mf)
        for i in range(len(eb)):
            F = eb[i]
            if pari('mfisCM')(F) == 0: continue
            L = pari('lfunmf')(mf, F)
            cands["g(N=%d,D=%d,#%d)" % (N, D, i+1)] = mpf(str(pari('lfun')(L, 0, 1)))
    except Exception as e:
        pass
print("target n_4(81) =", mp.nstr(n481, 30))
print("40*M_7 =", mp.nstr(40*cands["g(N=7,D=-7,#1)"], 30), " difference =", mp.nstr(n481 - 40*cands["g(N=7,D=-7,#1)"], 15))
found = False
for name, val in cands.items():
    for extra in ([], [log(3)], [log(2)], [log(3), log(2)]):
        basis = [n481, val] + extra
        rel = pslq(basis, maxcoeff=10**5, maxsteps=10**5)
        if rel and rel[0] != 0:
            print("RELATION with", name, [str(e)[:12] for e in extra], rel); found = True
# pairs of L-values
names = list(cands)
for i in range(len(names)):
    for j in range(i+1, len(names)):
        rel = pslq([n481, cands[names[i]], cands[names[j]]], maxcoeff=2000, maxsteps=10**5)
        if rel and rel[0] != 0:
            print("RELATION pair", names[i], names[j], rel); found = True
print("done; found =", found)
