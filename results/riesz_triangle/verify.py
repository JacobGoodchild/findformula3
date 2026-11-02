"""Checks supporting the proof of Conjectures 5.9 and 5.6 of arXiv:2609.11186 (Q. Fan, Riesz capacity ratios with negative exponents). See README.md."""
import sys, itertools
import numpy as np
ok = True
rng = np.random.default_rng(7)
def U3(a, b, c, r):          # Lemma 5.7 (c longest)
    x, y, z = a**r, b**r, c**r
    return z/2 if x + y <= z else 2*x*y*z/(4*x*y - (x + y - z)**2)
# (1) derivative identity:  d log U/dpsi = (s/D) (r/2) [ (z+y-x) cot(beta) - (z+x-y) cot(alpha) ]  vs finite differences
good = True
for _ in range(2000):
    phi = rng.uniform(np.pi/2 + 0.01, 2*np.pi/3 - 1e-3); psi = rng.uniform(0.01, 2*np.pi - 3*phi - 1e-3) if 2*np.pi - 3*phi > 0.02 else None
    if psi is None: continue
    r = rng.uniform(2.05, 8)
    al, be = (phi - psi)/2, (phi + psi)/2
    a, b, c = 2*np.sin(al), 2*np.sin(be), 2*np.sin(phi)
    x, y, z = a**r, b**r, c**r
    if x + y <= z: continue
    s = x + y - z; D = 4*x*y - s*s
    pred = (s/D)*(r/2)*((z + y - x)/np.tan(be) - (z + x - y)/np.tan(al))
    h = 1e-6
    f = lambda p: np.log(U3(2*np.sin((phi - p)/2), 2*np.sin((phi + p)/2), c, r))
    num = (f(psi + h) - f(psi - h))/(2*h)
    if abs(num - pred) > 1e-5*max(1, abs(pred)): good = False
ok &= good; print("riesz derivative identity for d log U / d psi : %s" % ("OK" if good else "FAIL"))
# (2) key real-variable lemma:  0<a<b<1, a^2+b^2>=1, r>=2, a^r+b^r>1  =>  b^r - a^r >= b^2 - a^2
worst = 1
for _ in range(500000):
    a = rng.uniform(0, 1); b = rng.uniform(a, 1)
    if a*a + b*b < 1: continue
    r = 2 + 10**rng.uniform(-6, 3)
    if a**r + b**r <= 1: continue
    worst = min(worst, (b**r - a**r) - (b*b - a*a))
good = worst > -1e-12; ok &= good; print("riesz key lemma t_r >= t_2 on 5e5 random points (min slack %.2e): %s" % (worst, "OK" if good else "FAIL"))
# (3) Lemma K: k(1-w) >= k(w), w in [1/2,1), k(u) = -u ln u
w = np.linspace(0.5, 1 - 1e-9, 100001)
k = lambda u: -u*np.log(u)
good = np.all(k(1 - w) - k(w) >= -1e-15); ok &= good; print("riesz Lemma K (entropy comparison): %s" % ("OK" if good else "FAIL"))
# (4) Conjecture 5.6 by brute force over all triples (and pairs) of vertices of the regular N-gon, N odd, r>2
def energy_set(pts, r):
    best = 0
    for T in itertools.combinations(range(len(pts)), 2):
        best = max(best, (np.linalg.norm(pts[T[0]] - pts[T[1]])**r)/2)
    for T in itertools.combinations(range(len(pts)), 3):
        d = sorted([np.linalg.norm(pts[T[0]] - pts[T[1]]), np.linalg.norm(pts[T[0]] - pts[T[2]]), np.linalg.norm(pts[T[1]] - pts[T[2]])])
        best = max(best, U3(d[0], d[1], d[2], r))
    return best
good = True
for N in (5, 7, 9, 11, 15, 21, 31):
    pts = np.array([[np.cos(2*np.pi*k_/N), np.sin(2*np.pi*k_/N)] for k_ in range(N)])
    th = (N - 1)*np.pi/(2*N)
    for r in (2.01, 2.5, 3, 5, 12, 40):
        conj = 2**(r - 1)*np.sin(th)**r/(1 - 2**(r - 2)*np.cos(th)**r)
        if abs(energy_set(pts, r) - conj) > 1e-9*conj: good = False
ok &= good; print("riesz Conjecture 5.6 (brute force over all pairs/triples, N odd <= 31): %s" % ("OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
