# Independent verification: Gr(l) for higher-order Gregory coefficients (Xu-Zhao, arXiv:2609.11072)

Verifier code (written from scratch, python-flint 0.9.0, arb balls): /tmp/verify_gr/{gc.py,roots.py,tail.py,run_tail.py,chk.py}.
No file of /home/user/findformula3 was read.

## Definition used
G_n^{(l)} = [x^n] (x/ln(1+x))^l. Gr(l) = 1 + (largest n >= 1 with (-1)^(n-1) G_n^{(l)} <= 0).
Small n: n=0 is excluded (Gr is a positive integer, G_0=1 would give sign -1 trivially, and the paper's Theorem
concerns n >= Gr >= 1). Exact zeros (Theorem 3.1): G_{l+1}^{(l)}=0 for even l, G_l^{(l)}=0 for odd l>=3. These
count as "<= 0" (not strictly positive) but are far below the last bad n, so they do not affect Gr for l>=3.
In the code the ball of such a coefficient contains 0 and is accepted only at exactly those two indices
(any other ball containing 0 would make the run "uncertified" and double the precision).

## (1) Sign scan (RIGOROUS, ball arithmetic)
arb_series: log(1+x), divide by x, invert, power by repeated multiplication; precision 128 bits sufficed
(the loop would double it until all signs n=1..N_max were certified; no doubling was needed). Every
coefficient 1..N_max has a certified sign (except the 2 exact zeros).
Cross-check: exact rational series (Fractions) for l=3..7, n<=300: every ball contains the exact value
(tested via ball*denominator - numerator containing 0), exact sign patterns agree.

| l | N_max scanned | last n with wrong sign (<=0) | Gr(l) (mine) | paper | ratio Gr/3^l |
|---|---|---|---|---|---|
| 3 | 6000 | 10 | 11 | 11 | 0.407 |
| 4 | 6000 | 35 | 36 | 36 | 0.444 |
| 5 | 6000 | 112 | 113 | 113 | 0.4650 |
| 6 | 6000 | 345 | 346 | 346 | 0.4746 |
| 7 | 6000 | 1029 | 1030 | 1030 | 0.4710 |
| 8 | 6000 | 2994 | 2995 | - | 0.4565 |
| 9 | 60000 | 8579 | 8580 | - | 0.4359 |
| 10 | 60000 | 24302 | 24303 | - | 0.4116 |
| (11, bonus) | 120000 | 68282 | 68283 | - | 0.3855 (scan only, tail not certified) |

## (2) Tail n > N_max (RIGOROUS for l=3..10 modulo the cited paper facts below)
Own re-derivation following the paper's proof (not reading it blindly):
* (6) of the paper: (-1)^(n-1) G_n = int_1^inf h(z) f_n(z) dz, f_n=(1-(-1)^l z^(n-l-1))/(z+1)^(n-l+1).
  Numerically cross-checked against exact coefficients (l=4,5,6; n=12,20,30,150; 30 digits) - agreement, but formula not re-proved by me.
* H_l roots: flint fmpz_poly.complex_roots() (certified isolation) gives exactly l-1 simple real roots for
  l=3..12, matching Lemma 4.1(i). R := exact upper endpoint of the enclosure of r=exp(pi*rho_max)
  (enclosure width ~1e-150). Any R >= r works; z->1/z maps int_R^inf to int_0^{1/R} h f_n (checked algebraically).
* h > 0 on (0,1/R): from h = (-pi)^(l-1) H_l(log z/pi)(log^2 z+pi^2)^(-l) (identity checked to 1e-92) and sign of H_l beyond its largest root.
* f_n decreasing on (0,1) for n >= l+3 (derivative computed by hand, both parities) => int_0^{1/R} h f_n >= alpha f_n(1/R).
  alpha_low = int_{ln R}^{400} h(e^-t) e^-t dt (lower bound because h>0; endpoint = exact upper endpoint of ln R), via arb integral (rigorous Petras bound).
* On [1,R]: |f_n(z)|/f_n(1/R) <= u_m(z), m=n-l-1, u_m = z^m q^(m+2)/(1-R^-m) (l even), (1+z^m) q^(m+2) (l odd), q=(1+1/R)/(1+z)<1.
  u_m is decreasing in m for each z in [1,R] (z q <1 iff z<R), so a single check at n0 covers all n>=n0.
  (This is my own cleaner majorant; it is a bit weaker than the paper's split at z=2 for odd l, yet reproduces the paper's n2 exactly for l>=4 and is better for l=3.)
* Criterion: alpha_low - int_1^R |h| u_m dz > 0 (|h| handled by splitting at the certified roots with sign fixed per cell by a ball evaluation; the thin
  slivers around the root enclosures bounded by width*sup|h|*sup u with ball evaluation). All integrals: acb.integral (rigorous), 300-bit working precision.
  Margin is certified positive as a ball.

| l | R | n0 (smallest n passing, certified for all n>=n0) | paper n2 | margin(n0) | margin(n0-1) | N_max >= n0-1 ? |
|---|---|---|---|---|---|---|
| 3 | 6.1337 | 15 | 16 | +1.6e-5 | -2.9e-5 | yes |
| 4 | 23.1407 | 52 | 52 | +2.1e-7 | -7.0e-8 | yes |
| 5 | 75.4924 | 168 | 168 | +1.4e-9 | -5.2e-10 | yes |
| 6 | 230.7646 | 519 | 519 | +1.1e-11 | -6.2e-13 | yes |
| 7 | 681.0150 | 1548 | 1548 | +1.1e-14 | -6.0e-14 | yes |
| 8 | 1967.4146 | 4514 | 4514 | +1.9e-16 | -1.8e-16 | yes |
| 9 | 5605.2273 | 12944 | 12944 | +1.7e-18 | -1.1e-19 | yes |
| 10 | 15816.8007 | 36685 | 36685 | +7.3e-21 | -6.5e-22 | yes |

(The paper's Table 1 R for l=9 says 5065; I get 5605.23 - the paper table has a digit transposition; their n2(9) agrees with mine.)
Since the scan covers all n<=60000 >= n0-1 for each l, Gr(l) values in the table are rigorous (l=3..10, relying on the paper's identity (6), which I checked numerically, and on my own argument above).
Note: the n0 values are only a "passes" bound; Gr is the exact scan result. For l=10 the integral at m=60000-5 returned NaN (arb evaluation limit), so l=10 search used N_max 45000; irrelevant to the result.

## (3) Do l=8,9,10 give 2995, 8580, 24303?
YES: 2995, 8580, 24303 exactly (certified scan + certified tail).

## (4) Conjecture 6.1 (0.47*3^l < Gr(l) < 0.477*3^l for l>=5)
0.47*3^5 = 114.21 > 113 = Gr(5) (paper's value and mine): the lower bound FAILS at l=5. It also fails at l=8 (0.47*6561=3083.7 > 2995), l=9 (9250.4 > 8580), l=10 (27753 > 24303), and (scan) l=11. At l=6,7 it holds (6: 342.6<346<347.7; 7: 1027.9<1030<1043.1). The ratio Gr/3^l peaks near l=6 (0.4746) and then decreases (0.4565, 0.4359, 0.4116, 0.3855 for l=8..11); successive ratios Gr(l+1)/Gr(l) = 2.85, 2.86, 2.83 (8->9... precisely 2.865, 2.833, 2.810) drift below 3, so growth is not ~3^l.

## Caveats
* Identity (6) and Lemma 4.1 are the paper's; I checked (6) numerically and the root count by certified root isolation, not by proof.
* Positivity of h on (0,1/R) and monotonicity of f_n are argued by hand, spot-checked numerically only for h.
* l=11 is scan only (no tail certificate).
