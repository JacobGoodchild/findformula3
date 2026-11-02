"""Independent check of the closed forms in S_table.txt against direct high-precision numerics
(Euler-Maclaurin summation, numerics.py).  Prints OK/FAIL per q."""
import re, sys
from fractions import Fraction
from mpmath import mp, mpf, zeta
from cypari import pari
from numerics import S
DPS = 45
def mz(a, b):
    pari.set_real_precision(DPS+20)
    return mpf(str(pari('zetamult([%d,%d])' % (a, b))).replace(' ', '').replace('E', 'e'))
def evaluate(line):
    rhs = line.split('=', 1)[1]
    total = mpf(0)
    for coef, mon in re.findall(r'\(([-0-9/]+)\)\*((?:zeta\([0-9,]+\)\*?)+)', rhs):
        v = mpf(Fraction(coef).numerator) / Fraction(coef).denominator
        for a in re.findall(r'zeta\(([0-9,]+)\)', mon):
            if ',' in a:
                x, y = map(int, a.split(',')); v *= mz(x, y)
            else:
                v *= zeta(int(a))
        total += v
    return total
def main():
    ok = True
    mp.dps = DPS + 10
    for line in open('S_table.txt'):
        q = int(re.match(r'S_(\d+)', line).group(1))
        mp.dps = DPS + 10
        lhs = S(q, DPS); rhs = evaluate(line)
        mp.dps = DPS
        d = abs(lhs - rhs)
        good = d < mpf(10)**(-(DPS-8))
        ok &= good
        print("harmonic_products S_%d: %s (|diff|=%s)" % (q, "OK" if good else "FAIL", mp.nstr(d, 3)))
    return ok
if __name__ == "__main__":
    sys.exit(0 if main() else 1)
