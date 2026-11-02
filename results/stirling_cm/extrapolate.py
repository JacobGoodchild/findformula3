"""Extrapolate (2n-1)*delta_{n,0} (= (2n-1)(d_CM(R_n) - (2n-2))) from table_m0_n2_22.txt and compare with Krasniqi's upper bound 2 pi^2 / J, J = int_0^{2pi} (1-cos u)/u du = Cin(2 pi)."""
import re, sys
import numpy as np
from mpmath import mp, quad, cos, pi
mp.dps = 20
J = quad(lambda u: (1 - cos(u))/u, [0, 2*pi]); bound = float(2*pi**2/J)
data = {}
for line in open('table_m0_n2_22.txt'):
    m = re.match(r"n=(\d+) m=0\s+d_CM = (\d+) \+ ([0-9.]+)", line)
    if m: data[int(m.group(1))] = float(m.group(3))
n = np.array(sorted(data), float); y = np.array([(2*k - 1)*data[int(k)] for k in n])
est = []
for var in (1/n, 1/(n + 0.5)):
    for lo in (8, 10, 12):
        sel = n >= lo
        for deg in (4, 5, 6):
            A = np.vstack([var[sel]**k for k in range(deg + 1)]).T
            est.append(np.linalg.lstsq(A, y[sel], rcond=None)[0][0])
est = np.array(est)
print("n = %d..%d ; extrapolated limits (polynomial in 1/n or 1/(n+1/2), degree 4-6): min %.5f, median %.5f, max %.5f" % (n[0], n[-1], est.min(), np.median(est), est.max()))
print("Krasniqi's upper bound 2*pi^2/J = %.6f ; difference to median = %.2e" % (bound, np.median(est) - bound))
sys.exit(0 if abs(np.median(est) - bound) < 5e-3 else 1)
