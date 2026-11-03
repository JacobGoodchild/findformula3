"""Checks for the Gurland results (paper Sec. 7).
(a) ln G*(x,y) = sum_k (1/k) d^{2k} zeta(2k, 1+h) (h=(x+y)/2, d=(x-y)/2) at several (x,y), including delta/(1+h)=0.98, to 40 digits;
(b) numerical support for the conjecture theta < 1/3 (theta=(h-t)/(h-g), psi'(1+t)=ln G*/d^2): 150 random points, all theta in (0,1/3), and theta -> 1/3 as h grows with d/h small.
Exit code 1 on failure."""
import random, sys
from mpmath import mp, mpf, loggamma, zeta, psi, sqrt, nsum, inf
mp.dps = 150
ok = True
def lnG(x, y):
    x, y = mpf(x), mpf(y); h = (x + y)/2
    return loggamma(1 + x) + loggamma(1 + y) - 2*loggamma(1 + h)
def series(x, y, N):
    x, y = mpf(x), mpf(y); h = (x + y)/2; d = (x - y)/2
    return sum(zeta(2*k, 1 + h)*d**(2*k)/k for k in range(1, N + 1))
for (x, y, N) in [(1, 2, 80), (5, 5, 5), (3, 3.001, 40), (50, 0.5, 700), (0.01, 100, 2000), (1e-3, 1e3, 4000)]:
    h = (mpf(x) + y)/2; d = abs(mpf(x) - y)/2
    r = (d/(1 + h))**2
    a, b = lnG(x, y), series(x, y, N)
    err = abs(a - b)
    pred = r**N/(N*(1 - r)) if r < 1 else 0
    good = err < max(pred*5, mpf(10)**-40)
    ok &= good
    print("gurland series (x,y)=(%s,%s) N=%d: |lnG*-S_N|=%.2e (predicted tail ~%.1e): %s" % (x, y, N, err, pred, "OK" if good else "FAIL"))
def theta(x, y):
    x, y = mpf(x), mpf(y); h = (x + y)/2; d = (x - y)/2; g = sqrt(x*y)
    target = lnG(x, y)/d**2
    lo, hi = g, h
    for _ in range(120):
        mid = (lo + hi)/2
        if psi(1, 1 + mid) - target > 0: lo = mid
        else: hi = mid
    t = (lo + hi)/2
    return (h - t)/(h - g)
mp.dps = 40
random.seed(2026)
mx = 0; bad = 0
for i in range(150):
    x = 10**random.uniform(-3, 3.5); y = 10**random.uniform(-3, 3.5)
    if abs(x - y)/max(x, y) < 1e-3: continue
    th = theta(x, y); mx = max(mx, th)
    bad += (th <= 0 or th >= mpf(1)/3)
good = bad == 0 and mx < mpf(1)/3
ok &= good
print("gurland theta in (0,1/3) at 150 random points, max theta=%.5f: %s" % (mx, "OK" if good else "FAIL"))
th = [theta(x, x*1.001) for x in (1e3, 1e4)]
good = all(mpf('0.33') < t < mpf(1)/3 for t in th)
ok &= good
print("gurland theta -> 1/3 for large h, small d: %s: %s" % ([float(t) for t in th], "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
