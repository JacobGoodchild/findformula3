"""Q. Fan, arXiv:2609.11186 (Riesz capacity ratios with negative exponents): Conjecture 5.9.
B, C on the unit circle at polar angles +-phi (phi in (pi/2, 2pi/3]); A at angle psi in [0, 2pi - 3phi] so that BC is the longest side.
Energy of a 3-point set with side lengths a,b <= c (Lemma 5.7 = Clark-Laugesen Thm 8):  U = c^r/2 if a^r+b^r <= c^r ; U = 2 a^r b^r c^r / (4 (ab)^r - (a^r+b^r-c^r)^2) otherwise.
Conjecture 5.9: for r >= 2, U is maximal at psi = 2pi - 3phi (i.e. AC = BC)."""
import numpy as np, sys
def energy(phi, psi, r):
    c = 2*np.sin(phi)
    a = 2*np.abs(np.sin((phi - psi)/2)); b = 2*np.abs(np.sin((phi + psi)/2))
    x, y, z = a**r, b**r, c**r
    out = np.where(x + y <= z, z/2, 2*x*y*z/(4*x*y - (x + y - z)**2))
    return out
def check(r, nphi=400, npsi=2000):
    worst = 0; arg = None
    for phi in np.linspace(np.pi/2 + 1e-6, 2*np.pi/3, nphi):
        psis = np.linspace(0, 2*np.pi - 3*phi, npsi)
        U = energy(phi, psis, r)
        # normalise by endpoint energy
        d = (U.max() - U[-1])/U[-1]
        if d > worst: worst = d; arg = (phi, psis[np.argmax(U)])
    return worst, arg
if __name__ == "__main__":
    for r in [2.0, 2.0001, 2.01, 2.1, 2.5, 3, 4, 6, 10, 30, 100, 400]:
        w, arg = check(r)
        print("r=%g : max relative excess of U over the endpoint value (conjecture says <= 0): %.3e at %s" % (r, w, arg))
