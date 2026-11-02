import numpy as np
from mpmath import mp, mpf, mpc, hyp2f1, quad, re, im, log, nsum, factorial, inf, pi
from direct_check import n4_direct
mp.dps = 25
F = lambda z: hyp2f1(mpf(1)/8, mpf(3)/8, 1, mpc(z, mpf(10)**-30))**2
a = lambda n: factorial(4*n)/(factorial(n)**4*n*mpf(256)**n)
base = log(256) - nsum(a, [1, inf], method='r+s+e')
for k in (3.9, 3.5, 3.0, 2.5, 2.0):
    s = mpf(k)**4
    cont = base - quad(lambda t: re(F(256/t))/t, [s, 256])
    I = quad(lambda t: im(F(256/t))/t, [s, 256])
    direct = n4_direct(k, 1600)
    D = direct - float(cont)
    print("k=%.1f s=%.2f: direct=%.7f continuation(Re)=%.7f  D=%.7f   int Im F dt/t=%.7f   D/I=%.6f  (D/I)/pi=%.6f" % (k, s, direct, cont, D, I, D/float(I) if abs(I)>1e-12 else float('nan'), D/float(I)/np.pi if abs(I)>1e-12 else float('nan')))
