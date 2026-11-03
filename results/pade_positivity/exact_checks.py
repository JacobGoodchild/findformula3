"""Extra exact certifications for the diagonal Pade positivity proofs (added after a referee pass).
For each odd m in [lo, hi]: Q(z) = (2m)! q_{m,m}(z) has integer coefficients (-1)^j C(m,j) (2m-j)!.
 (1) squarefree: gcd(Q, Q') is a nonzero constant (exact integer arithmetic).
 (2) certified complex roots via arb's fmpz_poly complex_roots (isolating balls; real roots are returned with exactly zero imaginary part);
     exactly one root is real and positive: R;
 (3) every other root has certified modulus > R (ball comparison, lower bound of |rho| minus R > 0), and we record the gap ratio.
Progress is appended to exact_checks.log (one line per m) and resumed on restart.
Usage: python3 exact_checks.py LO HI
"""
import sys, os, time
from math import comb, factorial
from flint import fmpz_poly, arb, acb, ctx

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exact_checks.log")

def done_set():
    s = set()
    if os.path.exists(LOG):
        for line in open(LOG):
            if line.startswith("m=") and ": OK" in line:
                s.add(int(line.split(":")[0][2:]))
    return s

def check(m):
    coeffs = [(-1) ** j * comb(m, j) * factorial(2 * m - j) for j in range(m + 1)]
    Q = fmpz_poly(coeffs)
    g = Q.gcd(Q.derivative())
    assert g.degree() == 0, "not squarefree"
    roots = Q.complex_roots()
    assert sum(mult for _, mult in roots) == m and all(mult == 1 for _, mult in roots)
    realpos = [r for r, _ in roots if r.imag == 0 and r.real > 0]
    assert len(realpos) == 1, "positive real root count %d" % len(realpos)
    R = realpos[0].real
    others = [r for r, _ in roots if not (r.imag == 0 and r.real > 0)]
    ratios = []
    for r in others:
        a = abs(r)
        assert a > R, "root with modulus not certified > R"
        ratios.append(a / R)
    gap = min(ratios, key=lambda x: x.mid())
    return R, gap

if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    ctx.prec = 256
    done = done_set()
    for m in range(lo | 1, hi + 1, 2):
        if m < 3 or m in done:
            continue
        t = time.time()
        try:
            R, gap = check(m)
            line = "m=%d: OK squarefree, exactly one positive real root R=%s, min |other|/R > %s [%.1fs]" % (
                m, R.str(15, radius=False), (gap.mid() - gap.rad()).str(10, radius=False), time.time() - t)
        except AssertionError as e:
            line = "m=%d: FAIL %s" % (m, e)
        with open(LOG, "a") as f:
            f.write(line + "\n")
        print(line, flush=True)
