# Referee report, round 1: Gurland partial-sum claim (open problems 1 and 2)

## (1) Verdict: COMPLETE MODULO MINOR

The claim is correct and the proof is essentially rigorous. It is a standard consequence of the Taylor expansion of ln Gamma at 1+m together with its radius of convergence. It is mathematically short and nearly trivial once you see it: no deep step, and no numerics are needed for the proof. Issues 1-5 below are all minor presentation points.

## (2) Issues

1. (minor) Notation clash. The packet uses m for the partial-sum index (S_m, R_nm) and also for the mean (x+y)/2 in the proof ("1+m", "nearest singularity at -(1+m)"). Define m := (x+y)/2 and a := 1+m = 1+(x+y)/2. Write the partial sums with another index, e.g. N. R_nm is also never defined (n is unexplained). Also state delta := (x-y)/2 explicitly, and note that delta enters only through delta^2, so its sign is immaterial. The proof uses delta without defining it, and the setting section does not name it.
2. (minor) The identification x = m-delta, y = m+delta (or the reverse) is never stated. Without it, ln G* = f(delta)+f(-delta)-2f(0) is not visibly the same as ln Gamma(1+x)+ln Gamma(1+y)-2 ln Gamma(1+m). The identity is correct. Suggested fix: add one line.
3. (minor) The meaning of "ln Gamma" on the complex disc is not stated. Suggested fix: say that Gamma has no zeros and is analytic and non-vanishing on the simply connected half-plane Re w>0, so there is a unique analytic branch of ln Gamma there that is real on w>0. Its derivative is psi, which is analytic on Re w>0. For real z in the disc, the analytic f(z) equals the real ln Gamma(1+m+z). Otherwise "f is analytic" is a slight abuse of notation. Also say that the disc |z|<a is contained in Re(a+z)>0 because Re z > -a.
4. (minor) "The radius of convergence in delta is exactly 1+m" is asserted via the nearest singularity of f. This is fine for f, but the series of interest is the even part. The cleaner justification is that zeta(2k,a) >= a^{-2k}, so the terms are at least (delta/a)^{2k}/k, which diverges for |delta|>=a. Convergence for |delta|<a is the claim of the theorem. Suggested fix: add this one-line argument. I did not need the radius for the main claim, so this does not affect correctness.
5. (minor) Numerical sanity line is understated or misleading. "3000 terms give agreement to 1e-10" for delta/a=0.98: the true truncation remainder after N terms is about r^{2N}/(N(1-r^2)) with r^2=0.9608. At N=500 this is about 1e-10, and at N=3000 it is about 1e-55. The 1e-10 figure matches N=500, not 3000. I do not think the author's "ratio 0.96" is wrong (it is r^2); only the term count is off. At 3000 terms the residual I saw at 60 digits was about 1e-18; that is an mpmath working-precision floor (it drops to 1e-25 at 80 digits and 1e-37 at 120 digits), not a failure of the series. Suggested fix: correct or drop the sentence. It is not part of the proof.
6. (minor, optional) Edge cases not mentioned. For x=y, delta=0, the sum is empty or zero, and ln G* = 0 trivially. The proof applies. The margin is: a-|delta| = 1+min(x,y) > 1 for all x,y>0. This is a uniform gap, with the ratio |delta|/a <= (max-min)/(max+min+2) < 1. It tends to 1 only when max/min -> infinity or max -> infinity. This is worth stating, since it also gives the explicit geometric rate. The proof says only "<", which is enough. Also note that the argument works for x,y > -1 (not just >0), since then a+z still has positive real part. This is not needed.
7. (minor) The comparison "paper's Q(x,y)=|x-y|/(2(1+sqrt(xy))) < 1 is far from necessary" is correct, since sqrt(xy) <= m gives delta/a <= Q. For example, (0.01,100) has Q about 12.5 yet the series converges. It is rhetoric, not part of the proof. Fine as is.

No fatal or major issues.

## (3) Steps verified and how

- Analyticity: the disc |z|<1+m maps into Re(1+m+z)>0 because Re z >= -|z| > -(1+m). On this half-plane ln Gamma is analytic, because Gamma is non-vanishing and analytic, and the half-plane is simply connected. The Taylor series therefore converges to f on the whole disc (Cauchy-Taylor theorem). The nearest singularity is at z=-(1+m), where Gamma has its pole at argument 0. Checked by reasoning.
- |delta| < 1+m: (x+y)/2+1-|x-y|/2 = 1+min(x,y) > 1. Checked algebraically, and numerically in the table below (the margin column equals 1+min(x,y)).
- ln G* = f(delta)+f(-delta)-2f(0) with delta=(y-x)/2. Checked algebraically.
- Odd Taylor terms cancel in f(delta)+f(-delta), the constant terms cancel against -2f(0), and the even terms double. Checked algebraically.
- f^{(2k)}(0) = psi^{(2k-1)}(1+m) = (-1)^{2k}(2k-1)! zeta(2k,1+m) = (2k-1)! zeta(2k,1+m). This uses psi^{(n)}(a)=(-1)^{n+1} n! zeta(n+1,a). Checked symbolically, and it is consistent with the numerics, which use exactly this coefficient.
- Combination: 2*(2k-1)!*zeta(2k,a)*delta^{2k}/(2k)! = zeta(2k,a)*delta^{2k}/k. Checked algebraically.
- Numerical test with mpmath at 60-120 digits. ln G* = loggamma(1+x)+loggamma(1+y)-2 loggamma(1+m) compared with the partial sums sum_{k<N} (delta^{2k}/k) zeta(2k,a), for the following inputs.

| (x,y) | ratio^2 (delta/a)^2 | margin a-delta | remainder at N=10 / 100 / 500 / 3000 |
|---|---|---|---|
| (0.01,100) | 0.9608 | 1.01 | 1.5, 3.9e-3, 1.0e-10, floor at precision (about 1e-18 at 60 digits) |
| (1,2) | 0.04 | 2.0 | 1e-15, below 1e-61 from N=100 on |
| (50,0.5) | 0.889 | 1.5 | 0.29, 6.5e-7, floor 1e-25 at N=500 |
| (3,3.001) | 1.6e-8 | 4.0 | below 1e-61 already at N=10 |
| (5,5), (1e-6,1e-6) | 0 | | exactly 0 |
| (0.01,1000) | 0.99597 | 1.01 | 25, 1.4, 0.052, 4.2e-7 |

- Convergence rate: the observed remainders match the predicted tail r^{2N}/(N(1-r^2)) with r^2=(delta/a)^2 to within a factor of about 1.2 up to N=500 for (0.01,100), (50,0.5) and (0.01,1000). The ratio is about 0.96, 0.89 and 0.996 respectively. This confirms the geometric rate (delta/(1+m))^2 per term. The leveling-off values are mpmath precision floors, confirmed by rerunning at 80 and 120 digits: the floor drops as expected, and mpmath's zeta(2k,a) agrees with a direct sum to relative error 5e-55 at k=10 and better at larger k.
- Conclusion "R_N(x,y) -> 0 and ln G* = S_inf for every x,y>0" follows directly from convergence of the Taylor series and the identity above. Verified.

## Summary
Correct, short, standard (Taylor series of ln Gamma at 1+m, radius of convergence 1+m). Proof is rigorous once the notation and the branch of ln Gamma are made explicit. The only substantive slip is the numerical sanity line (the term count in the 1e-10 claim). Verdict: COMPLETE MODULO MINOR.
