"""Fit the TRUE Mahler measure for 0<s<256:  n_4(s) = n0 + sum_{j=1}^3 c_j B_j(x), x = s/256, with
 B_j(x) = x^{a_j} sum_n t_{j,n} x^n/(a_j+n),  t_{j,n} = coefficients of 3F2(a_j,a_j,a_j;b1_j,b2_j;x), (a_j) = (1/4,1/2,3/4), n0 = 14 zeta(3)/pi^2 (= 4 m(1+X+Y+Z), Smyth),
 against direct 2-D Jensen integrals (direct_values.json); extra constraints: n_4(256) = 5.4127398169250764 and C^1 matching  sum c_j S_j(1) = 2F1(1/8,3/8;1;1)^2."""
import json, numpy as np
from scipy.special import hyp2f1, zeta
def coeffs(a, b1, b2, N):
    t = np.ones(N+1)
    for n in range(N):
        t[n+1] = t[n]*(a+n)**3/((b1+n)*(b2+n)*(n+1))
    return t
PARS = ((0.25, 0.75, 0.5), (0.5, 1.25, 0.75), (0.75, 1.5, 1.25))
N = 400000
T = [coeffs(*p, N) for p in PARS]
nn = np.arange(N+1)
def B(j, x):
    a = PARS[j][0]
    return x**a*np.sum(T[j]*x**nn/(a+nn))
def S(j, x):
    a = PARS[j][0]
    return x**a*np.sum(T[j]*x**nn)
data = json.load(open('direct_values.json'))
n0 = 14*zeta(3)/np.pi**2
ks = sorted(float(k) for k in data)
rows = []; rhs = []
for k in ks:
    x = k**4/256
    rows.append([B(j, x) for j in range(3)]); rhs.append(data[str(k)][-1] - n0)
# continuity constraints (weighted heavily)
W = 50.0
Nb = [B(j, 1.0) for j in range(3)]
rows.append([W*v for v in Nb]); rhs.append(W*(5.41273981692507642 - n0))
rows.append([W*S(j, 1.0) for j in range(3)]); rhs.append(W*hyp2f1(1/8, 3/8, 1, 1.0)**2)
A = np.array(rows); b = np.array(rhs)
c, res, rk, sv = np.linalg.lstsq(A, b, rcond=None)
print("c1,c2,c3 =", c)
print("residuals (data rows):", np.round((A@c - b)[:len(ks)], 8))
x81 = 81/256
print("n_4(81) from fit =", n0 + sum(c[j]*B(j, x81) for j in range(3)))
