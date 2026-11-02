"""For each order ell: find Gr(ell) = 1 + (last n whose sign (-1)^(n-1) G_n^(ell) is wrong), with rigorous (interval) sign certification
for ALL n <= N. Precision is doubled until every coefficient with n>=50 is certified (zero coefficients occur only at small n)."""
import sys, time, json
from gr import coeffs
def certified_scan(ell, N, prec):
    while True:
        c = coeffs(ell, N, prec)
        bad = []; unk = []
        for n in range(1, N+1):
            x = c[n] * (1 if (n-1) % 2 == 0 else -1)
            if x.lower() > 0: continue
            if x.upper() < 0: bad.append(n)
            else: unk.append(n)
        if all(n < 50 for n in unk): return bad, unk, prec
        prec *= 2
if __name__ == "__main__":
    out = {}
    for ell in range(int(sys.argv[1]), int(sys.argv[2])+1):
        N = int(sys.argv[3].replace('x', str(3**ell))) if 'x' in sys.argv[3] else int(sys.argv[3])
        t = time.time()
        bad, unk, prec = certified_scan(ell, N, int(sys.argv[4]))
        gr = (bad[-1] + 1) if bad else 1
        print("ell %d  N %d  prec %d  Gr=%d  Gr/3^ell=%.5f  zeros/undetermined(n<50)=%s  [%.0fs]" % (ell, N, prec, gr, gr/3**ell, unk, time.time()-t), flush=True)
