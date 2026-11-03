# Referee report, round 1: S_q = sum_k H_k...H_{k+q}/(k...(k+q))

## (1) Verdict: COMPLETE MODULO MINOR

The method is a valid proof scheme, and the S_4 closed form and the S_3 value both agree with my independent numerics to 40 digits. Several things must be stated explicitly in a paper, and one step (MZV reduction by PSLQ) is not a proof as described. See the issues below.

## (2) Issues

1. **MZV -> zeta-product reduction by PSLQ (severity: moderate, easily fixed).**
   - Step 5 finds the reductions by PSLQ at 150 digits. A PSLQ relation is evidence, not proof.
   - The claim "every MZV of weight <= 7 is a polynomial in single zetas" is a theorem, but it is not a theorem about the particular rational coefficients PSLQ returned.
   - Fix, either of:
     - (a) Derive the reductions exactly. Linear algebra over Q on the double-shuffle plus regularised-stuffle relations (or duality plus sum formulas) in weights <= 6 or 7 gives each MZV as a rational combination of products of single zetas. Record that this was done in exact arithmetic.
     - (b) Cite explicit evaluations from the literature (Borwein-Girgensohn for weights <= 7, or the MZV Data Mine), and state that PSLQ was used only to select a candidate that was then confirmed by (a) or by the citation.
   - Until then, the closed forms are "proved modulo the MZV table". The structural statement (Q-span of MZVs of weight <= q+2) is proved without it.

2. **Stuffle regularisation must be justified, and it must be set at finite K (severity: moderate, a presentational gap).**
   - The logic is sound when stated as follows.
     - Truncated sums zeta_K(s_1..s_r) = sum_{K>=n_1>...>n_r>=1} satisfy the stuffle (quasi-shuffle) product exactly for every finite K. So all algebra can be done at finite K with no regularisation.
     - Then one needs the asymptotic statement: for s_1 = 1, zeta_K(s) = P_s(H_K) + O(log^j K / K), where P_s is the stuffle-regularised polynomial in T = H_K and its constant coefficients are the MZVs. This is Hoffman / Ihara-Kaneko-Zagier. The paper should state it as a lemma and cite it.
   - Pitfall: the variable must be T = H_K exactly (stuffle regularisation). Using log K + gamma would be the shuffle regularisation, which differs by explicit zeta-values.
   - Because the divergent T-powers cancel identically in the total, the regularisation only needs to be consistent between pieces, not canonical. That is correct. But the lemma that the constant term is a Q-combination of true MZVs (s_1 >= 2) still needs the cited theorem.

3. **Cancellation of divergent powers of T (severity: minor).**
   - The assertion made by the program is legitimate in a computer-assisted proof, provided the arithmetic is exact (Fractions or sympy Rationals, no floats).
   - It is automatically guaranteed in principle. The original series converges, so the K-truncated total is a convergent sequence, and the polynomial in T must have no positive-degree terms.
   - The paper should say that the assert is a consistency check, and that its success is also forced by convergence. A failure would indicate a bug rather than a mathematical gap.

4. **Convergence of intermediate sums (severity: minor, needs one sentence).**
   - The first claim "R_m = O(k^-(q+1)), so each block converges" is true. Each H_k^m R_m sum converges absolutely.
   - After partial fractions the individual pieces sum H^m/(n+a)^s with s = 1 diverge. These are legitimate only as K-truncated sums that are combined before the limit.
   - State that all pieces are handled as sums over 1 <= n <= K (with the same K), that finite-sum identities are exact, and that the limit is taken only at the end.
   - The simple-pole coefficients of each R_m are not individually zero. The cancellation happens across the different m after reducing to T-polynomials, and that is exactly what the assert checks.

5. **Shift reductions (severity: minor).**
   - Reindexing p = n+a changes the summation range from n <= K to p <= K+a, and the lower limit from 1 to 1+a. Both changes are finite corrections:
     - The low end gives finite rational heads.
     - The upper end gives terms H_p^m/p^s for p in (K, K+a], which are O(log^m K / K^s) -> 0 for s >= 1 (a fixed).
   - Also H_{p-a} = H_p - sum_{i=0}^{a-1} 1/(p-i), which uses p-i, not p+i, for a > 0 (sign convention). The packet's "+/-" and "p+i" are loose. The paper must fix the convention.
   - Finite sums of 1/(p-i) are rational functions of p and re-enter the partial fractions. Termination is by induction on m (the power of H strictly drops each time), which the paper should state.
   - For negative a (p = n - |a|), poles at p <= 0 never occur because the original poles are at k = 0..-q, so the shift runs the other way. The paper should state which direction is used.

6. **Weight bound "<= q+2" (severity: minor, but the packet claims it without proof).**
   - Here is the argument. In H_k^m R_m(k), R_m is a sum of products of (q+1-m) factors 1/(k+i) with 1/(k...(k+q)). A pole at k = -i has order at most 1 + (q+1-m). So each partial-fraction term H^m/(k+a)^s has m + s <= q+2.
   - Shift reductions trade H-power for 1/(p+i)-powers without raising m+s. Nested-sum expansion of H_p^m / p^s has weight m+s. So all MZVs appearing have weight <= q+2 and mixed-weight rational coefficients (as expected from S_1 = zeta(2) + 2 zeta(3)).
   - Note that naive homogeneity gives weight 2q+2, and partial fractions at distinct shifts is what lowers it.
   - Also record that depth/weight are mixed. The Q-span claim is a span of MZVs of weights 2..q+2 together with rational numbers (weight 0, the heads).

7. **Weight 8 caveat (severity: informational).** For q >= 6 the weight bound is q+2 >= 8. zeta(5,3) is then an independent generator, so closed forms in single zetas are not guaranteed. The packet already says so. Keep the statement of the theorem as "MZVs", not "zeta products".

8. **Reproducibility of the proof (severity: minor).** For a paper, the program must be published, it should use exact rationals, and one should list the checks: the T-cancellation assert, and a numerical comparison with an independent summation (done below).

## (3) Steps verified, and how

- Numerics: independent code of mine (Euler-Maclaurin with exact Taylor-series derivatives of the digamma-based terms, quad for the tail integral, N = 70 and N = 90 agreeing to 1e-49, mp.dps = 50).
- S_3 = -4/9 z2 - 1/6 z2 z3 - 7/24 z3 + 191/144 z4 + 1/2 z5: matches to 40 digits.
- S_4 closed form in the packet: matches to 40 digits.
- S_1 derived by hand, independently of the method:
  - H_{k+1} = H_k + 1/(k+1) splits the term as H_k^2 (1/k - 1/(k+1)) + H_k/(k(k+1)^2).
  - Abel summation gives sum H_k^2(1/k - 1/(k+1)) = sum (2 H_k/k - 1/k^2)/k = 2 * 2 z3 - z3 = 3 z3.
  - Partial fractions give sum H_k/(k(k+1)^2) = z2 - z3.
  - So S_1 = z2 + 2 z3 = 4.0490478731674...  This agrees with the numerics, and with a PSLQ relation [1, 0, -1, -2].
- S_2: PSLQ at 50 digits against {1, z2, z3, z4} gives S_2 = -z2/2 + 5 z3/4 + 5 z4/8 (relation [8, 0, 4, -10, -5]). The coefficients are small and the identification is stable, but this is VERIFIED, not PROVED (from me).
- The weight-bound argument (item 6), the shift reduction termination (item 5) and the convergence structure (item 4): checked by reasoning, not by running the authors' code, which I was told not to read.

## (4) Numerical comparison (50-digit working precision, 40 shown)

| q | S_q numerical (my EM code) | closed form | difference |
|---|---|---|---|
| 1 | 4.049047873167415007271891489668925170749 | z2 + 2 z3 (hand derivation) | < 1e-40 |
| 2 | 1.356556116594841008210967428904529833081 | -z2/2 + 5 z3/4 + 5 z4/8 (PSLQ) | < 1e-40 (relation found at 50 digits) |
| 3 | 0.5428129263265657674837597015263889172081 | Chen-Nguyen value as given | < 1e-40 |
| 4 | 0.2128907376496087409111708832939020867858 | packet closed form | < 1e-40 |

No discrepancy found.
