import time
from fractions import Fraction as Fr
from series import compute
def run(P, S):
    t = time.time(); p, res = compute([Fr(x) for x in P], S)
    neg = [(k, j, str(c)) for k, pk in enumerate(p) for j, c in enumerate(pk) if c < 0]
    print("P=%s  S=%d consistent=%s nonneg=%s %s [%.0fs]" % (P, len(p)-1, all(r == 0 for r in res) and len(p) == S+1, not neg, neg[:2], time.time()-t), flush=True)
run([0,0,0,1], 40)
run([0,0,0,0,1], 30)
run([0,0,0,0,0,0,1], 20)
run([0,1,1,1], 30)
run([0,1,1,0,1], 25)
