"""Computer-assisted PROOF, for a given odd m, that ALL Taylor coefficients c_n (n>=0) of 1/q_{m,m}(z) are positive (diagonal Pade, Fasi-Higham conjecture).
Steps (all in rigorous ball arithmetic, python-flint):
 1. isolate all m complex roots rho_i of q = q_{m,m} (distinct, so 1/q = sum_i A_i/(1 - z/rho_i), A_i = -1/(rho_i q'(rho_i)) ... c_n = sum_i B_i rho_i^{-n-1}, B_i = -1/q'(rho_i)).
 2. exactly one real positive root R; every other root satisfies |rho_i| > R (ball-certified).
 3. tail bound: for n >= N0, |sum_{i != R} B_i rho_i^{-n-1}| <= sum |B_i| rho_other^{-n-1} < B_R R^{-n-1}, N0 explicit.
 4. interval-check c_n > 0 for 0 <= n < N0 using the power-series inverse with enough precision.
"""
import sys, time
from math import comb, factorial, log, ceil
from flint import arb, acb, acb_poly, arb_series, ctx, fmpq
def qcoeffs(m):
    return [fmpq((-1)**j * comb(m, j) * factorial(2*m-j), factorial(2*m)) for j in range(m+1)]
def prove(m, prec0=256, verbose=False):
    ctx.prec = prec0
    qc = qcoeffs(m)
    P = acb_poly([acb(arb(c)) for c in qc])
    dP = P.derivative()
    while True:
        try:
            roots = P.roots(tol=arb(2)**(-ctx.prec//2), maxprec=ctx.prec*4)
            break
        except Exception:
            ctx.prec *= 2
            P = acb_poly([acb(arb(c)) for c in qc]); dP = P.derivative()
    assert len(roots) == m
    # real positive roots
    real_pos = [r for r in roots if r.imag.contains(0) and r.real > 0]
    if len(real_pos) != 1: return None, "real positive root count %d" % len(real_pos)
    R = real_pos[0]
    others = [r for r in roots if r is not R]
    assert all(not o.imag.contains(0) for o in others)
    # moduli of the others must exceed R (certified)
    absR = abs(R)
    B = lambda r: -1/dP(r)
    if not others: return 0, "single root"
    lower_mod = min((abs(r).lower() for r in others), key=lambda a: a.mid())   # certified lower bound of the smallest modulus among the other roots
    if not (lower_mod > absR.upper()):
        return None, "dominant-root property not certified"
    BR = B(R).real
    if not (BR.lower() > 0):
        return None, "B_R > 0 not certified"
    assert B(R).imag.contains(0)
    S = sum((abs(B(r)) for r in others), arb(0)) if others else arb(0)
    # need  S * rho_other^{-n-1} < BR * R^{-n-1}   <=>   (rho_other/R)^{n+1} > S/BR
    ratio = (S/BR).upper(); g = (lower_mod/absR.upper())
    N0 = int(ceil((arb(ratio).log()/arb(g).log()).upper())) + 1
    N0 = max(N0, 1)
    # finite part
    prec = max(512, 2*ctx.prec); N = N0 + 5
    while True:
        ctx.prec = prec; ctx.cap = N+1
        q = [arb(c) for c in qc]
        inv = arb_series(q).inv().coeffs()
        if all(inv[n].lower() > 0 for n in range(N+1)): break
        prec *= 2
        if prec > 2**20: return None, "finite check could not be certified (N0=%d)" % N0
    return N0, "proved (N0=%d, prec=%d)" % (N0, prec)
if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for m in range(lo, hi+1, 2):
        t = time.time()
        N0, msg = prove(m)
        print("m=%d: %s [%.1fs]" % (m, msg, time.time()-t), flush=True)
