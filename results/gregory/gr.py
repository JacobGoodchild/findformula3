import sys, time
from flint import arb, arb_series, ctx, fmpq
def coeffs(ell, N, prec):
    ctx.prec = prec; ctx.cap = N+1
    v = arb_series([arb(1)/(k+1) * (1 if k % 2 == 0 else -1) for k in range(N+1)])   # log(1+x)/x
    F = (v.log() * (-ell)).exp()                                                      # (x/log(1+x))^ell
    return F.coeffs()
if __name__ == "__main__":
    ell = int(sys.argv[1]); N = int(sys.argv[2]); prec = int(sys.argv[3])
    t = time.time(); c = coeffs(ell, N, prec); print("time", time.time()-t)
    print([str(x)[:20] for x in c[:6]])
