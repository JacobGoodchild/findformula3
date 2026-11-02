# Samart's conjecture n_4(81) = 40 M_7: where the 0.0587 discrepancy comes from  (arXiv:2608.02265, status report; question: closed form of the true n_4(81))

n_4(s) = 4 m(x^4+y^4+z^4+1+s^{1/4} x y z), M_7 = L'(g_7,0), g_7 = eta(tau)^3 eta(7 tau)^3. The status report proves "EK_4(tau_2) = 40 M_7", refutes n_4(81) = 40 M_7 by a 20-digit torus integration (difference +0.0587), and says a closed form for the true n_4(81) "remains open".

## What I computed
* **Analytic-continuation value.**  For s > 256: n_4(s) = log s - sum_{n>=1} (4n)!/((n!)^4 n) s^{-n}, and s n_4'(s) = 3F2(1/4,1/2,3/4;1,1;256/s) = 2F1(1/8,3/8;1;256/s)^2 (Clausen).  Continuing along the real axis through the conifold s = 256 and taking the real part
  (`n4fast.py`, 2F1 route; `n4.py`, direct 3F2 route -- they agree to all digits) gives
  **n_4^{cont}(81) = 4.10686431115608044841826379593**  and  **40 L'(g_7,0) = 40 x 0.1026716077789020112104565949 = 4.1068643111560804484182638 :  equal to 25 digits.**
  So the L-value side of Samart's conjecture is exactly the real part of the analytic continuation of the large-s series (consistent with the report's proof that EK_4(tau_2) = 40 M_7).
* **The true Mahler measure** (Jensen's formula in z plus a 2-D periodic grid, `direct_check.py`, no continuation involved): n_4(256) = 5.41273982 (agrees with the series, so the code is right), n_4(625) = 6.39548445 (agrees with the series), and
  **n_4(81) = 4.16553(5)** (grid 400/800/1600: 4.165541, 4.165533, 4.165535) -- i.e. the report's refutation is confirmed independently: n_4(81) - 40 M_7 = 0.05867(1).
  Other points: D(s) := n_4^{true}(s) - n_4^{cont}(s): D(231.3) = 5.1e-4, D(150.1) = 1.36e-2, D(81) = 5.87e-2, D(39.1) = 0.143, D(16) = 0.277 (`correction.py`).
* **Conclusion.** For 0 < s < 256 the Mahler measure is NOT the real part of the analytic continuation of the large-s series; Samart's conjectured identity compares the continuation (which equals 40 M_7) with the true measure. D(s) is a new non-trivial real-analytic function
  (it vanishes at s = 256 to order ~2 and is not a multiple of the integral of Im 3F2, nor of the pure exponent-1/2 solution -- both tested). Whether D(81) has a closed form is not answered here (7 reliable digits only, too few for PSLQ).
  Tried and failed: modelling the true derivative as (a) the pure exponent-1/2 Frobenius solution at s=0 fixed by C^1-continuity at 256 (`true_n4.py`, `true_n4_float.py`: off by 0.3 at s=81), (b) a combination of all three Frobenius solutions at s=0 plus the constant 14 zeta(3)/pi^2 = 4 m(1+X+Y+Z), fitted to 8 direct values (`fit_frobenius.py`: residuals 1e-2, so the true function near s=0 has non-Frobenius (logarithmic) terms). Direct values: `direct_values.json` (k = 0.5 ... 3.9, grids 1200 and 2400).
Label: VERIFIED (numerical): the continuation value equals 40 M_7 to 25 digits; true n_4(81) = 4.16553(5) to 6 digits. No closed form for the true value. Novelty: explanation not found in the report (they say the continuation 'cannot be reached', not that it already equals 40 M_7 numerically).
Files: n4fast.py (continuation), direct_check.py (torus integral), correction.py, cmforms.py + pslq_search.py (CM L'(g,0) library of weight-3 rational CM newforms for the closed-form search; not run on the true value).
