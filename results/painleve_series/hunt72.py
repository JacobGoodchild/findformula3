import random, sys, time
from fractions import Fraction as Fr
from series import compute
random.seed(int(sys.argv[1])); S = int(sys.argv[2]); trials = int(sys.argv[3])
found = 0
for t in range(trials):
    d = random.choice([3,4,5,6])
    pi1 = random.choice([0,0,1,Fr(1,10),Fr(1,100),2,7])
    P = [Fr(0), Fr(pi1), Fr(pi1)] + [Fr(random.choice([0,0,0,Fr(1,100),Fr(1,10),1,3,20,100])) for _ in range(d-2)]
    if P[-1] == 0: P[-1] = Fr(random.choice([1,1000]))
    p, res = compute(P, S)
    ok1 = all(r == 0 for r in res) and len(p) == S+1
    neg = [(k, j, float(c)) for k, pk in enumerate(p) for j, c in enumerate(pk) if c < 0]
    if (not ok1) or neg:
        found += 1
        print("FOUND:", [str(x) for x in P], "consistent", ok1, neg[:3], flush=True)
print("seed", sys.argv[1], "trials", trials, "S", S, "violations", found, flush=True)
