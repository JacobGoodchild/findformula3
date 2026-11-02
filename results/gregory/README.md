# Sign thresholds Gr(l) of higher-order Gregory coefficients, and Conjecture 6.1 of arXiv:2609.11072 (C. Xu, J. Zhao)

G_n^{(l)} are the Taylor coefficients of (x/log(1+x))^l. Theorem 5.1 of the paper: (-1)^{n-1} G_n^{(l)} > 0 for all n >= Gr(l). The authors list Gr(3..7) = 11, 36, 113, 346, 1030
and ask (Conjecture 6.1): is 0.47 * 3^l < Gr(l) < 0.477 * 3^l for all l >= 5?

## Results
| l | Gr(l) | Gr/3^l | r(l)=exp(pi cot(pi/l)) | Gr/r | tail bound n2(l) |
|---|---|---|---|---|---|
see `table.txt` (copied below)

```
ell  Gr(ell)   Gr/3^ell   r(ell)=exp(pi*cot(pi/ell))   Gr/r    Gr(l)/Gr(l-1)   tail-bound n2(ell)
  3       11   0.40741             6.13   1.7934      -     16
  4       36   0.44444            23.14   1.5557   3.2727   52
  5      113   0.46502            75.49   1.4968   3.1389   168
  6      346   0.47462           230.76   1.4994   3.0619   519
  7     1030   0.47096           681.02   1.5124   2.9769   1548
  8     2995   0.45649          1967.41   1.5223   2.9078   4514
  9     8580   0.43591          5605.23   1.5307   2.8648   12944
 10    24303   0.41157         15816.80   1.5365   2.8325   36685
 11    68283   0.38546         44324.02   1.5405   2.8097   103104
 12   190698   0.35883        123572.51   1.5432   2.7928   287998
 13   530152   0.33252        343156.69   1.5449   2.7801   800744
```
* Gr(3..7) agree with the paper. **Gr(8)=2995, Gr(9)=8580, Gr(10)=24303 are new (rigorous, see below); Gr(11)=68283, Gr(12)=190698, Gr(13)=530152, Gr(14)=1468691 are new (numerically certified tail).**
* **Conjecture 6.1 is false**: Gr(5)=113 < 0.47*3^5 = 114.2 (already visible in the paper's own table), and Gr(l) < 0.47*3^l for every l from 8 to 13 (ratio Gr/3^l: 0.456, 0.436, 0.412, 0.385, 0.359, 0.333).
  Among l >= 5 only l = 6, 7 satisfy it.
* **What the data say instead:** the largest real zero of the paper's polynomial H_l is exactly r(l) = exp(pi cot(pi/l))  [h(z) ∝ sin(l*theta)/|log z + i pi|^l with theta = arg(log z + i pi), zeros at log z = pi cot(k pi/l), k=1..l-1],
  so r(l) = exp(l - pi^2/(3l) - ...) grows like e^l, NOT 3^l (the paper's table value r(9)=5065 is a misprint of 5605.2). Gr(l)/r(l) = 1.4968 (l=5), ..., 1.5405, 1.5432, 1.5449, 1.5460 (l=11,12,13,14), still creeping up by ~0.002/step,
  and Gr(l)/Gr(l-1) decreases 3.27, 3.14, ..., 2.78, 2.77 towards e = 2.718. So the data suggest Gr(l) ~ c * exp(pi cot(pi/l)) with c ~ 1.55, hence Gr(l)/3^l -> 0 geometrically; the factor 3 in the conjecture was an artefact of small l.
  (Observation only; no proof.)


## Asymptotics of Gr(l): Gr(l) ~ e^{l + 1 - gamma}   (numerically verified to l = 100+, heuristic derivation; NOT a proof)
* **Exact integral representation** (checked here against the power-series coefficients for l = 3, 4, n up to 50, ratio 1.0000 to 12 digits; `integral_form.py`): for n > l + 3,
  (-1)^{n-1} G_n^{(l)} = int_0^infty h(e^L) f_n(e^L) e^L dL,  h(e^L) = (-1)^{l-1} Im[(L + i pi)^l] / (pi (L^2+pi^2)^l),  f_n(z) = (1 - (-1)^l z^{n-l-1})/(z+1)^{n-l+1}.
  Because n enters only as an exponent this lets me compute the (real-n) last sign change n*(l) for large l without any power series (`big_ell.py`; it reproduces the exact thresholds: n* = 112.63, 2994.71, 24302.57, 190697.75 for l = 5, 8, 10, 12 against Gr = 113, 2995, 24303, 190698).
* Data (n*(l)/r(l), r(l) = exp(pi cot(pi/l))): l = 14: 1.5460, 16: 1.54689, 20: 1.54645, 25: 1.54469, 30: 1.54294, 40: 1.53967, 50: 1.53747, 70: 1.53508, 100: 1.53265. The ratio peaks near l = 16 and then decreases slowly.
* **Heuristic derivation.** For large n only the z^{n-l-1} term of f_n matters and with w = n e^{-L}, Lambda = ln n, lambda = l/Lambda:  J(n) ~ n^{-1} Lambda^{-l} int_0^infty w^lambda e^{-w} sin( pi lambda + (pi lambda/Lambda) ln w ) dw ~ Gamma(lambda+1) [ sin(pi lambda) + (pi lambda/Lambda) cos(pi lambda) psi(lambda+1) ].
  With lambda = 1 + eps this vanishes when eps = -(1/Lambda) psi(2) = -(1-gamma)/Lambda, i.e. Lambda = ln n* = l + (1 - gamma) + O(1/l).  Since ln r(l) = l - pi^2/(3l) + ..., this predicts **n*(l)/r(l) -> e^{1-gamma} = 1.52620...**
  A polynomial-in-1/l extrapolation of the computed ratios (l = 20..100) gives 1.5250 - 1.5254, consistent with e^{1-gamma} (differences O(1/l): the data minus e^{1-gamma} times l is about 0.56 (l=50), 0.62 (l=70), 0.64 (l=100)).
* Consequence: Gr(l) = (1+o(1)) e^{l+1-gamma}, so Gr(l)/3^l -> 0 geometrically; Conjecture 6.1 (a 3^l law) is false for every large l, not just for l = 5, 8, ...

## Method / rigour
* `gr.py`: coefficients of (x/log(1+x))^l as an arb power series (python-flint, exp(-l*log(log(1+x)/x))), with rigorous error balls. `grscan2.py` doubles the precision until every coefficient with n >= 50 is certified
  to have a definite sign (the only exact zeros are at tiny n, e.g. G_l^{(l)}=0 for odd l as in the paper's Theorem 3.1). Gr(l) = 1 + (last n with the wrong sign), for all n <= N (N = 8e4 for l<=10, 2e5/5.5e5/1.5e6 for l=11/12/13).
* Tail n > N: the paper's proof gives an explicit n2(l) (their Table 2, l <= 10) beyond which the sign is right. `n2_bound.py` re-implements that criterion (mpmath quadrature, not interval arithmetic) and reproduces
  their n2(l) exactly for l = 5..10 (168, 519, 1548, 4514, 12944, 36685; for l=3,4 it gives 18, 53 instead of their 16, 52 -- I did not chase this), and gives 103104, 287998, 800744 for l = 11, 12, 13, all below the scan limits.
  Hence: l <= 10 rigorous given the paper's theorem + interval signs; l = 11..13 rigorous up to the accuracy of the quadrature in n2_bound.py.
