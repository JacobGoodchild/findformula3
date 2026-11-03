# Fasi-Higham positivity conjecture for Pade approximants of exp: the diagonal case and the true region of validity
Source: F. Scardino, arXiv:2610.39051 (Oct 2026), "On a positivity conjecture of Fasi and Higham for Pade approximants to the matrix exponential".
Conjecture 1 (Fasi-Higham): for odd m and every k >= 0, all Taylor coefficients c_n(k,m) of 1/q_{k,m}(z) are positive, where
q_{k,m}(z) = sum_{j<=m} (-1)^j C(m,j) (k+m-j)!/(k+m)! z^j.  The paper proves it for k = 0, eventual positivity for k large, **disproves** the unrestricted conjecture
(exact counterexamples c_38(66,5) < 0, c_37(44,7) < 0, c_42(45,9) < 0) and says: "the diagonal case k = m, which is the case relevant in practice, remains open".

## Results
1. **Diagonal case, odd m <= M: PROVED for each m (computer-assisted, rigorous ball arithmetic)** -- all c_n(m,m) > 0 for ALL n >= 0.   (`rigorous_diag.py`; the runs covered all odd 3 <= m <= 359, logs `rigorous_diag_*.log` (several files, because the machine restarted overnight): 179 values of m, all proved; N0 reaches 368413 at m=359.)
   Proof for a given m: (i) isolate all m complex zeros of q_{m,m} with certified balls; exactly one is real positive (R) and every other zero has certified modulus > R;
   (ii) c_n = sum_i B_i rho_i^{-n-1}, B_i = -1/q'(rho_i); B_R > 0 (certified), so for n >= N0 the other zeros contribute less than the R term (explicit N0 from the residues and the spectral gap);
   (iii) positivity of c_n for n < N0 is verified with the interval power-series inverse (python-flint, precision raised until every ball is positive). N0 grows like 1.7 m^2.
2. **Where the conjecture really fails (new, computational):** for each odd m let k*(m) = smallest k with a negative coefficient. The failing set is exactly {k >= k*(m)} (checked contiguous for m = 15..71, k < 400).
   k*(m) = 2m + 12 or 13 or 14 for all m tested between 109 and 909 (m=9: 42, 19: 54, 29: 73, 39: 91, 49: 111, 59: 131, 69: 151, 79: 172, 89: 192, 99: 210, 109: 230, 209: 430, 309: 630, 409: 831, 509: 1031, 709: 1431, 809: 1631, 909: 1832).
   So the diagonal k = m is far from the boundary (k*/m -> 2) and positivity for k <= 2m + 11 looks true for large m; the first negative coefficient sits at n ~ k + m - 3.
   m = 3: no negative coefficient for any k < 1500 (n <= 4k+200); m = 1 is positive for all k (paper).
   (`kstar.py`, `kmin.py`; the smaller counterexample (k,m,n) = (42,9,41) beats the paper's (45,9,42); k*(5)=66, k*(7)=44 as in the paper.)
3. The numbers are consistent with the paper's transient-scaling picture but give the quantitative boundary k ~ 2m + O(1) that the paper does not state.

## Honest status
* (1) is a theorem for each listed m, not for all m (the general diagonal statement is still open).  (2) is numerical (interval arithmetic for each coefficient, but the pattern k* = 2m+12..14 and the contiguity are observations).
