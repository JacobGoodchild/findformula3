# Independent numerical verification: S_q = sum_{k>=1} H_k...H_{k+q} / (k...(k+q)), q = 5..8

Verifier: fresh code (own scripts, /tmp/verify_hs2), mpmath 1.3 + cypari (for zeta(5,3), convention sum_{n>m} n^-5 m^-3 = 0.03770767298...). No repo files read.
All PSLQ outcomes are numerical identifications, not proofs.

## Method for S_q
f(k)=prod_{j=0..q} H_{k+j}/(k+j), H_x = digamma(x+1)+gamma. S_q = sum_{k<N} f(k) + int_N^inf f + Euler-Maclaurin boundary terms
(f(N)/2 - sum_{k<=K} B_2k/(2k)! f^(2k-1)(N)); derivatives of f at N from exact Taylor-series products (polygamma coefficients); the integral by mpmath tanh-sinh on a geometric partition.
Error control: two independent runs with different (N,K,working precision) compared.
- q=5 (80 dps): N=150,K=14 vs N=250,K=15 agree to 5e-61. S_5 minus the stated closed form = -1e-61 (residual at the noise floor): **S_5 formula confirmed to 60 digits.** (S_4 formula not separately tested.)
- q=6: two runs (N=600,800; 270 dps) agree to 2.5e-163. q=7: (N=800,1000; 520 dps) agree to 6e-287. q=8: (same N, 520 dps) agree to 7e-288.
Values (first 55 digits):
- S_6 = 0.0271069253370172439393273451372452367140136611585747907723349
- S_7 = 0.0087236781658610275303913998680343149705151520776910811099559
- S_8: see files in /tmp/verify_hs2/vh_8_*.txt (not reproduced here)

## S_6: relation found WITHOUT zeta(5,3)
Basis: all monomials z2^a z3^b z5^c z7^d (z9 not needed), weight 2..8 (13 monomials; 14 unknowns with S). PSLQ at tol 1e-150 (data good to 163 digits), residual 4.8e-164, found in both bases (with and without zeta(5,3), where zeta(5,3) gets coefficient 0):
 1088640000 S_6 = 2892680 z2 - 17822035 z3 - 169061095 z2^2 + 50498350 z5 + 42288120 z2 z3 - 57615600 z3^2 + 81709536 z2^3 + 146336400 z7 + 4838400 z2 z5 - 21561120 z2^2 z3 - 1512000 z3 z5 + 466560 z2^4.
(An earlier attempt at 58 digits returned a spurious relation with random 5-digit coefficients; the 150-digit run is the credible one: 14 unknowns with 10-digit coefficients, residual 1e-164 far below the chance level.)
=> **zeta(5,3) is NOT needed for S_6** (claim confirmed).

## S_7: zeta(5,3) needed
- Basis products only (19 unknowns, weights 2..9, incl. z9, z2 z7, z2^2 z5, z2^3 z3, z3^3): PSLQ at tol 1e-274 (data 286 digits, coefficient bound 1e14): **no relation**.
- Adding zeta(5,3) (20 unknowns): relation found, residual 3.8e-288 (full data precision), tol 1e-274:
 9601804800000 S_7 = 12632348120 z2 - 22473282090 z3 - 577473429085 z2^2 - 1964254731600 z5 - 238752602970 z2 z3 + 19046645100 z3^2 + 354867366924 z2^3 + 2221658929350 z7 + 424791183600 z2 z5 - 313131162960 z2^2 z3 - 248173632000 z3 z5 + 15685488000 z2 z3^2 + 120320087904 z2^4 + 9525600000 z9 - 1905120000 z2 z7 - 762048000 z2^2 z5 - 435456000 z2^3 z3 - 70400534400 zeta(5,3).
 (the weight-9 coefficients are small and highly composite, as for a genuine relation.)
=> **zeta(5,3) IS needed for S_7** (supported: relation with it at 286 digits; none without it up to coefficient size 1e14 and 274 digits; this is numerical evidence, not a non-existence proof, since a relation with larger coefficients cannot be excluded by PSLQ alone). Earlier attempts at ~150 digits (both bases) gave only spurious relations, so the 286-digit run is the one that matters.

## S_8: INCONCLUSIVE at the precision reached
Basis weights 2..10 (23 monomials incl. z2^5, z2^2 z3^2, z2 z3 z5, z5^2, z3 z7) with and without zeta(5,3), at 286 digits, coefficient bound 1e14: only spurious relations (random-looking 13-digit coefficients, residual at the tolerance 1e-275). 24-25 unknowns with expected coefficients of order 1e14-1e15 need roughly 350-400 digits. The claim "zeta(5,3) first needed at q=7, and again at q=8" is therefore NOT independently tested for q=8 by this run. (Weight-10 candidate z(7,3), z2*zeta(5,3) not tried in a completed run.) A higher-precision (720 dps) run for q=8 was launched; see the addendum below if it finished.

## Summary
- S_5 formula: confirmed (60 digits).
- S_6: closed form in single-zeta products, no zeta(5,3) (confirmed, 150-digit PSLQ).
- S_7: no relation in single-zeta products (274 digits, coeff <= 1e14); relation exists once zeta(5,3) is added (286 digits). Consistent with the claim.
- S_8: not decided here (insufficient precision).

Addendum: the 720-dps q=8 run had not finished at the 40-minute limit and was stopped; S_8 remains undecided.
