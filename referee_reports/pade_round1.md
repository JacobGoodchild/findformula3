# Referee report, round 1: positivity of Taylor coefficients of 1/q_{m,m}, odd m (3..361)

## (1) Verdict: COMPLETE MODULO MINOR
The scheme is a valid proof for each fixed m, provided the items in (2) are certified. I saw only the written description, not the code, so I can only say what must be certified, not that it was.

## (2) Issues
1. (Medium) Squarefreeness / distinctness. The formula c_n = sum B_i rho_i^{-n-1} needs simple zeros. Pairwise-disjoint root balls with exactly m balls for a degree-m polynomial does certify this, but it must be checked explicitly. Cheaper and fully exact: gcd(q,q')=1 over Q (I did this). Fix: do both.
2. (Medium) Count of positive real zeros. The Arb balls alone do not give this. A ball whose imaginary part contains 0 is not proved real unless it is an isolating ball of a conjugate-closed root set. Fix: an exact Sturm count on Q (I used sympy count_roots(0,oo)==1, and the total real count 1). Then the unique ball with Im containing 0 and Re>0 is R. Also check that no other ball overlaps R's ball.
3. (Medium) Strict inequality of moduli. Must be a certified comparison abs(ball_i) > ball_R (Arb `>` is certified), for all other i, including conjugates of each other. A float mid-minus-rad is not acceptable. Take rmin as the arb-min, i.e. a certified lower bound of the others' moduli.
4. (Medium) Root-ball width. In python-flint 0.9, acb_poly.roots() with default tol returns isolating but very loose balls (about 1e-3 relative at m=9, even at prec 200). B_i = -1/q'(rho_i) then evaluates to NaN or non-positive-certifiable balls. This fails safe (the proof does not go through) but is a trap. Fix: pass tol=2^-(prec/2) and maxprec, or refine with Newton, and raise the precision until everything certifies. Their description of "precision raised" suggests this is already handled.
5. (Low) No polynomial part. 1/q has numerator degree 0 < m, so the partial-fraction expansion has no polynomial part, with c_n = -sum A_i rho_i^{-n-1}, A_i = 1/q'(rho_i), valid for every n>=0 (all |rho_i|>0). So B_i = -1/q'(rho_i) is correct. Fix: state this in the proof. It is a one-line check.
6. (Medium) Explicit N0. Requires n+1 > log(S/B_R)/log(rmin/R) with S = sum over i!=R of |B_i| (upper bound of ball abs), B_R lower bound, rmin lower bound, R upper bound. Round up with outward rounding and add 1 for safety. Then for n >= N0: |c_n - B_R R^{-n-1}| <= S rmin^{-n-1} < B_R R^{-n-1}, so c_n>0. Conjugate pairs make c_n real, so no complex issue. The "N0 ~ 1.7 m^2" is consistent with my values (about m^2 at their looser bound; mine are smaller, see table). A looser N0 is harmless.
7. (Low) Initial coefficients. Interval power-series inverse is valid but if a ball ever straddles 0, "raise precision" must stop on failure rather than loop. I prefer exact rational recurrence c_n = -sum_{j>=1} a_j c_{n-j} (a_j in Q), which needs no precision issue. Fix: use Fractions or fmpq as a cross-check; the c_n are positive rationals and huge-denominator growth is fine for n<=N0 ~ 2e5 at m=361 (maybe slow; interval is acceptable).
8. (Low) Silent failure modes: (a) the nearest competing zero pair gap ratio rmin/R-1 shrinks like ~1/m^2 (1.094, 1.036, 1.019, 1.0117, 1.0080 for m=3..11), so precision needed grows only logarithmically; but ensure precision >> log10 of N0*gap. (b) Proof of claim is only for odd m listed; even m has a real negative root or none and the argument is not claimed. (c) The unique-root claim must be per m; no pattern argument is used, so no extrapolation gap, good. (d) Floating `float(L.upper())` ceil can mis-round when L is near an integer; add 1.

## (3) Steps verified and how
- Partial-fraction formula and sign of B_i derived by hand and by the numerical sequence check.
- Exact gcd(q,q')=1 (fmpq_poly) for m=3..11.
- Exact Sturm count: exactly 1 positive real zero and exactly 1 real zero in total, m=3..11.
- python-flint acb_poly.roots(tol=2^-(prec/2)) at prec 100: m disjoint balls, a unique real-positive ball, abs(others)>R certified, B_R>0 certified.
- N0 computed from certified S, B_R, rmin/R; exact Fraction recurrence gives c_n>0 for all n<N0+50.
- Independent exact Fraction check of positivity of all c_n, n<=3000, for m=3,5,7,9,11,13,15,31: all positive (no deviations). (Printed minimum is 0.0 only due to float underflow of tiny c_n ~ R^-n; the exact check is on Fractions.)
Code: /tmp/claude-0/-home-user-findformula3/311c4a72-0704-5321-ad61-ef26a3a0bc55/scratchpad/myref.py

## (4) Table (my own run)
| m | R | min modulus others | B_R | S=sum|B_i| (others) | rmin/R | N0 (n+1>L) | c_n>0, n<N0 |
|---|---|---|---|---|---|---|---|
| 3 | 4.6443707093 | 5.0830828022 | 9.0595843 | 9.39704 | 1.0944610 | 1 (L=0.44) | yes |
| 5 | 7.2934771907 | 7.5557873219 | 41.726662 | 66.3096 | 1.0359650 | 14 | yes |
| 7 | 9.9435737171 | 10.132412300 | 192.89741 | 389.633 | 1.0189910 | 38 | yes |
| 9 | 12.594038363 | 12.741941439 | 893.01752 | 2137.70 | 1.0117439 | 75 | yes |
| 11 | 15.244679692 | 15.366355823 | 4137.1224 | 11294.4 | 1.0079815 | 127 | yes |

Deviations: none in the mathematics. Only the python-flint default-tolerance trap (issue 4).
