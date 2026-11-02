"""Conjecture 7.2 of arXiv:2606.21145 (nonnegative coefficients of p_k when all pi_j >= 0).
Reduction proved here:  p_s = L_s^{-1} rho_s, where (Lemma B, proved) the top-down solution of L_s p = rho has nonnegative coefficients whenever rho_m >= 0 for m >= 1.
So Conjecture 7.2 follows from:  (A) all coefficients of rho_s are >= 0.   This script checks (A) exactly (rational arithmetic) for many P up to s = S, and Lemma B on random data."""
import random, sys
from fractions import Fraction as Fr
from series import padd, pmul, pder, pscale, solveL
def rhs_sequence(P, S):
    p = [[Fr(0), Fr(1)]]
    out = []
    def Pu_coeff(s):
        tot = []
        cur = [[Fr(1)]] + [[] for _ in range(s)]
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
        R = []
        for i in range(1, s):
            j = s - i
            A = padd(padd(pder(pder(p[i])), pder(p[i]), -2*i), p[i], i*i)
            B = padd(pder(p[i]), p[i], -i)
            C = padd(pder(p[j]), p[j], -j)
            R = padd(R, pmul(A, p[j])); R = padd(R, pmul(B, C), -1)
        rhs = padd(Pu_coeff(s-1), R, -1)
        pk, res = solveL(s, rhs)
        assert res == 0
        out.append(rhs); p.append(pk)
    return out
def lemmaB(trials=2000):
    random.seed(5)
    for _ in range(trials):
        s = random.randint(1, 9); D = random.randint(1, 14)
        r = [Fr(random.randint(0, 9)) if random.random() < 0.8 else Fr(0) for _ in range(D+1)]
        r[D] = Fr(random.randint(1, 9))
        a, res = solveL(s, r)       # res (m=0 equation) is NOT assumed to vanish; Lemma B concerns the coefficients a_0..a_{D-1} determined by r_1..r_D
        if any(c < 0 for c in a): return False
    return True
if __name__ == "__main__":
    ok = lemmaB()
    print("Lemma B (top-down solution nonnegative when rho_m >= 0, m >= 1): %s" % ("OK" if ok else "FAIL"))
    random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    S = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    bad = 0; total = 0
    tests = [[0,0,0,1],[0,0,0,0,1],[0,1,1],[0,1,1,1],[0,1,1,0,1],[0,2,2,1,3],[0,0,0,0,0,1],[0,0,0,0,0,0,1]]
    for _ in range(25):
        d = random.choice([3,4,5,6]); pi1 = random.choice([0, 1, 3])
        tests.append([0, pi1, pi1] + [random.choice([0, 0, 1, 2, 5]) for _ in range(d-2)])
    for P in tests:
        if P[-1] == 0: P = P[:-1] + [1]
        seq = rhs_sequence([Fr(c) for c in P], S)
        for s, rhs in enumerate(seq, 1):
            total += 1
            if any(c < 0 for c in rhs): bad += 1; print("NEGATIVE rho_%d for P=%s" % (s, P))
    print("(A) rho_s >= 0 coefficientwise: %d of %d (P,s) cases violate" % (bad, total))
    sys.exit(0 if ok and bad == 0 else 1)
