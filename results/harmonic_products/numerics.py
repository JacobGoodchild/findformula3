# High-precision S_q = sum_{k>=1} prod_{j=0}^q H_{k+j} / prod_{j=0}^q (k+j)
# Method: exact head k<N, Euler-Maclaurin tail with Taylor data from python-flint (arb_series) and the
# integral by mpmath quad (substitution x=N/t).
import sys
from mpmath import mp, mpf, psi, euler, quad, bernoulli, factorial
from flint import arb, arb_series, ctx

def S(q, dps=50, N=None, R=None):
    N = N or int(40+dps*1.0); R = R or int(20+dps*0.5)
    mp.dps = dps + 20
    ctx.prec = int((dps+40)*3.33)
    f = lambda x: mp.fprod([psi(0, x+j+1)+euler for j in range(q+1)]) / mp.fprod([x+j for j in range(q+1)])
    head = mpf(0)
    for k in range(1, N):
        head += f(mpf(k))
    ctx.cap = 2*R+2
    g = arb(mp.nstr(euler, dps+40))
    num = arb_series([1]); den = arb_series([1])
    for j in range(q+1):
        num = num*(arb_series([N+j+1, 1]).lgamma().derivative() + g)
        den = den*arb_series([N+j, 1])
    c = (num*den.inv()).coeffs()
    tomp = lambda a: mpf(a.str(dps+30, radius=False))
    tail = tomp(c[0])/2
    for r in range(1, R+1):
        tail -= bernoulli(2*r)/factorial(2*r)*tomp(c[2*r-1])*factorial(2*r-1)
    integ = quad(lambda t: f(N/t)*N/t**2, [0, mpf(1)/4, mpf(1)])
    mp.dps = dps
    return +(head + integ + tail)

if __name__ == "__main__":
    q = int(sys.argv[1]); dps = int(sys.argv[2]) if len(sys.argv)>2 else 50
    print(q, S(q, dps))
