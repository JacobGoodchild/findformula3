"""True n_4(s) for 0<s<256 from the exponent-1/2 Frobenius solution at s=0 (n_4 is even in k = s^{1/4}):
   s n_4'(s) = c (s/256)^{1/2} 3F2(1/2,1/2,1/2; 5/4, 3/4; s/256),   c fixed by C^1-continuity at s=256 with 2F1(1/8,3/8;1;1)^2.
 n_4(s) = n_4(256) - int_s^256 s' n_4'(s') ds'/s'.   Compare with the direct 2-D Jensen integral."""
import sys
from mpmath import mp, mpf, hyp3f2, hyp2f1, quad, log, nsum, factorial, inf, gamma, sqrt, pi
mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 40
F1 = hyp2f1(mpf(1)/8, mpf(3)/8, 1, 1)**2
G1 = hyp3f2(mpf(1)/2, mpf(1)/2, mpf(1)/2, mpf(5)/4, mpf(3)/4, 1)
c = F1/G1
a = lambda n: factorial(4*n)/(factorial(n)**4*n*mpf(256)**n)
n256 = log(256) - nsum(a, [1, inf], method='r+s+e')
def n4_true(s):
    s = mpf(s)
    f = lambda t: c*sqrt(t/256)*hyp3f2(mpf(1)/2, mpf(1)/2, mpf(1)/2, mpf(5)/4, mpf(3)/4, t/256)/t
    return n256 - quad(f, [s, 256])
if __name__ == "__main__":
    print("c =", mp.nstr(c, 20), " F(1) =", mp.nstr(F1, 20), " n_4(256) =", mp.nstr(n256, 25))
    for k, direct in ((3.9, 5.2844726), (3.5, 4.7783773), (3.0, 4.1655352), (2.5, 3.5825156), (2.0, 3.0403441)):
        v = n4_true(mpf(k)**4)
        print("k=%.1f  n_4 true-branch = %s   direct 2-D integral = %.7f   diff = %.2e" % (k, mp.nstr(v, 15), direct, float(v) - direct))
