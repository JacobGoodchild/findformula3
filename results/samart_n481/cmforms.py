"""Derivatives L'(g,0) of weight-3 CM newforms with rational coefficients (level N, character (D/.))."""
from cypari import pari
pari.allocatemem(4*10**9)
pari.set_real_precision(50)
out = {}
for N, D in [(3,-3),(4,-4),(7,-7),(8,-8),(11,-11),(12,-3),(12,-4),(15,-15),(16,-4),(19,-19),(20,-20),(24,-24),(27,-3),(28,-7),(32,-8),(35,-35),(36,-4),(40,-40),(43,-43),(48,-3),(51,-51),(52,-4),(64,-4),(67,-67),(163,-163)]:
    try:
        mf = pari('mfinit([%d,3,%d],0)' % (N, D))
        eb = pari('mfeigenbasis')(mf)
        for i in range(len(eb)):
            F = eb[i]
            cm = pari('mfisCM')(F)
            if cm == 0: continue
            co = pari('mfcoefs')(F, 8)
            L = pari('lfunmf')(mf, F)
            d1 = pari('lfun')(L, 0, 1)
            print("N=%d D=%d form#%d CM=%s coefs=%s  L'(g,0)=%s" % (N, D, i+1, cm, co, str(d1)[:40]), flush=True)
    except Exception as e:
        print("N=%d D=%d : %s" % (N, D, str(e)[:80]))
