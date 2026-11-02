import sys, time
from diag_arb import check
lo, hi, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
bad = []
t0 = time.time()
for m in range(lo, hi+1, 2):
    prec = 1024
    while True:
        neg = check(m, m, N, prec)
        if not neg or prec >= 2**17: break
        prec *= 2
    if neg:
        bad.append((m, neg[:3], prec)); print("UNCERTIFIED/NEGATIVE m=%d n=%s prec=%d" % (m, neg[:3], prec), flush=True)
    if m % 50 == 1: print("m=%d done prec=%d [%.0fs]" % (m, prec, time.time()-t0), flush=True)
print("scan m in [%d,%d] odd, N=%d: problems=%d" % (lo, hi, N, len(bad)))
