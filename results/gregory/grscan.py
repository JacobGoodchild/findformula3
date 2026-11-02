import sys, time
from flint import arb, arb_series, ctx
from gr import coeffs
def scan(ell, N, prec):
    c = coeffs(ell, N, prec)
    bad = []; unk = []
    for n in range(1, N+1):
        x = c[n] * (1 if (n-1) % 2 == 0 else -1)      # (-1)^(n-1) G_n
        if x.lower() > 0: continue
        if x.upper() < 0: bad.append(n)
        else: unk.append(n)
    return bad, unk
if __name__ == "__main__":
    for ell in range(int(sys.argv[1]), int(sys.argv[2])+1):
        N = int(sys.argv[3]); t = time.time()
        bad, unk = scan(ell, N, int(sys.argv[4]))
        print("ell", ell, "N", N, "last_bad", bad[-1] if bad else None, "#bad", len(bad), "undetermined", unk[:10], len(unk), "[%.1fs]" % (time.time()-t), flush=True)
