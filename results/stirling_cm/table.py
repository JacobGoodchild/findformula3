import sys, time
from cmfast import crit
rows = []
for n in range(int(sys.argv[1]), int(sys.argv[2])+1):
    for m in (0, 1):
        t0 = time.time()
        try:
            q, a, t = crit(n, m)
            print("n=%d m=%d  d_CM = %d + %.10f   delta=%.10f  (2n-1)*delta=%.6f  t*=%.4f [%.0fs]" % (n, m, q, a, a, (2*n-1)*a, t, time.time()-t0), flush=True)
        except AssertionError as e:
            print("n=%d m=%d assertion failed %s" % (n, m, e), flush=True)
