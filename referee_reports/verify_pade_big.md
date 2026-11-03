# Independent re-run of the Pade certificate, m = 101, 201, 301

Fresh code (python-flint 0.9.0, ball arithmetic), written without reading the repo. Script: /tmp/verify_pade_big2/cert.py (not committed).

Method: integer polynomial P(z)=sum_j (-1)^j C(m,j)(2m-j)! z^j = (2m)! q(z). Roots isolated with fmpz_poly.complex_roots (disjoint balls, each with exactly one root, multiplicity 1, so m distinct roots). Each ball refined by interval Newton (N(c,r)=c-P(c)/P'(r) contained in r). Exactly one ball is real with positive real part -> R; all other balls have certified larger modulus (lower bound of modulus > upper bound of R). B_i=-(2m)!/P'(rho_i). S = upper bound of sum |B_i| over the other roots, N0 = ceil(ln(S/B_R)/ln(rho_min/R))+1. Then c_0..c_{N0-1} come from arb_series inversion of q at precision p, accepted only if every coefficient ball has lower bound > 0 (precision doubled until this held).

| m | R | rho_min/R (certified lower bd) | B_R | S | N0 | root prec (bits) | series prec | runtime |
|---|---|---|---|---|---|---|---|---|
| 101 | 134.5370933614 | 1.00010158 | 4.0139e33 | 4.025e34 | 22697 | 2000 | 2000 (ok) | 1.3 s |
| 201 | 267.0856882821 | 1.00002577 | 8.4137e66 | 1.2228e68 | 103850 | 4000 | 4000 (ok) | 16 s |
| 301 | 399.6343422069 | 1.00001151 | 1.7641e100 | 3.175e101 | 251082 | 6000 | 6000 FAILED (coefficients n >= 125541 not certified positive), 12000 ok | 129 s |

All steps certified for all three m: (1) distinct roots, unique positive real root R, all others strictly larger modulus; (2) B_R > 0 certified; (3) N0 as above; (4) c_n > 0 for n < N0 certified at the stated precisions.
Smaller sanity cases also certified: m=21 (N0=623), m=51 (N0=4881).

Comparison with expectations: N0 = 22697 (expected ~2e4), 103850 (~1e5), 251082 (~2.5e5), all within a factor 1.2. Ratios rho_min/R match (1.0001, 1.00003). No discrepancy above a factor 2.

Note for m=301: series inversion needed more than 6000 bits (certified at 12000 bits); at 6000 bits the ball radii swallowed the second half of the coefficients. This is a precision issue, not a positivity failure.
m=361 was started but not finished within the time limit; not verified here.

Addendum, m=361 (partial): steps (1)-(3) certified at 7000 bits: R = 479.16354251, rho_min/R >= 1.0000080073, B_R = 1.7356e120 > 0, S = 3.437e121, N0 = 372888. Step (4) (c_n > 0 for n < N0) was NOT completed: the process was terminated during the series inversion (by my own cleanup). Not verified.
