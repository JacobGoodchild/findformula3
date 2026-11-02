import random, sys, time
from fractions import Fraction as Fr
from series import compute
random.seed(int(sys.argv[1])); S = int(sys.argv[2]); trials = int(sys.argv[3])
for t in range(trials):
    d = random.choice([3,4,5,6,7])
    pi1 = random.choice([0,0,1,2,3])
    P = [Fr(0), Fr(pi1), Fr(pi1)] + [Fr(random.choice([0,0,1,2,5])) for _ in range(d-2)]
    if P[-1] == 0: P[-1] = Fr(1)
    t0 = time.time()
    p, res = compute(P, S)
    ok1 = all(r == 0 for r in res) and len(p) == S+1
    neg = [(k, j, str(c)) for k, pk in enumerate(p) for j, c in enumerate(pk) if c < 0]
    print("P=%s S=%d  conj7.1(consistent)=%s  conj7.2(nonneg)=%s %s [%.1fs]" % ([str(x) for x in P], len(p)-1, ok1, not neg, neg[:2], time.time()-t0), flush=True)
