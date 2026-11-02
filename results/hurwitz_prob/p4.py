"""Gasull's Problem 21 (arXiv:2012.02524): p_n = P(random polynomial with iid N(0,1) coefficients is Hurwitz stable).  p_3 = 1/16.  For n = 4:
   p_4 = (2/2^5) * P( a4 a1/(a3 a2) + a3 a0/(a2 a1) < 1 ),  a_i iid half-normal   (Routh-Hurwitz for quartics: all a_i > 0 and a3a2a1 > a4a1^2 + a3^2 a0).
 For fixed (a1,a2,a3): P over (a4,a0) = (2/pi) int_0^{pi/2} (1 - exp(-1/(2 (c1 cos t + c2 sin t)^2))) dt, c1 = a1/(a3 a2), c2 = a3/(a2 a1)."""
import numpy as np
from scipy.special import ndtri
def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b-a)*x + 0.5*(b+a), 0.5*(b-a)*w
def p4(n3=60, nt=80):
    u, wu = gl(n3, 0.0, 1.0)
    a = ndtri(0.5*(1.0 + u))                  # half-normal quantiles
    A1, A2, A3 = np.meshgrid(a, a, a, indexing='ij')
    W = wu[:, None, None]*wu[None, :, None]*wu[None, None, :]
    c1 = A1/(A3*A2); c2 = A3/(A2*A1)
    t, wt = gl(nt, 0.0, np.pi/2)
    tot = 0.0
    for ti, wi in zip(t, wt):
        s = c1*np.cos(ti) + c2*np.sin(ti)
        tot += wi*(1.0 - np.exp(-1.0/(2.0*s*s)))
    cond = (2/np.pi)*np.sum(W*tot)
    return cond/16.0, cond
if __name__ == "__main__":
    for n3, nt in ((30, 40), (50, 60), (80, 80)):
        p, cond = p4(n3, nt)
        print("grid %d/%d : p4 = %.10f  (P(Hurwitz | all positive) = %.10f)" % (n3, nt, p, cond), flush=True)
