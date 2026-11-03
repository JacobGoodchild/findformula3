# CITATIONS.md — Phase A check of every cited paper

Checked 3 Nov 2026 (UTC). For each paper: the arXiv abstract page and the PDF were opened (PDF converted to text with `pdftotext`); title, authors, date and ID are as shown on arXiv. Quoted statements are copied from the PDF text (mathematical formulas are as extracted by `pdftotext` and may be garbled in layout; the paper is the authority).

## Corrections found (to be applied everywhere)

1. **arXiv:2608.02265 is by Huimin Zheng, not by Samart.** Title: "Samart's conjecture n4(81) = 40M7: the exact CM evaluation and the two obstructions. A status report, companion to Mahler measures at interior CM points". Samart is the author of the conjecture (cited by Zheng as [3]); the paper we answered is Zheng's. Earlier docs said "Samart (arXiv:2608.02265)". WRONG; fixed.
2. **Zheng's paper already contains our "Samart" result.** Its abstract states that the identity n4(81) = 40M7 is "refuted" numerically (n4(81) - 40M7 = +0.0586706795972872...), Theorem 3.4 gives EK4(tau_2) = 40M7 = 4.10686..., and Section 6 gives n4(81) = 4.1655349907533676508(5). Our result (continuation equals 40 L'(g7,0); true value 4.16553(5)) is therefore **known**. See NOVELTY.md.
3. **Finch's Abel-function identities A(x/(1+x)) = B(x)+1, I(x/(1+x)) = J(x)+1 (arXiv:2503.00579) were already explained by the author himself.** Section 5 "Corrigendum" of the arXiv version (v3) says "The interrelation between A and B turns out to be frivolous" and shows, by reciprocating the recurrences, that one is a reparametrisation of the other, and likewise for I and J. Our "proof by Möbius conjugacy" is the same argument. Result is **known**; dropped from the paper.
4. **"Hoffman proved N = 1, 2, 3" (formulas.txt [12], results/t_values/README.md) was written from memory and is not what the paper says.** Chavan–Kobayashi–Layja (Section 4, after Example 4.4) say Hoffman [10, Appendix] "highlights the relations" t(2,1) = t(2)log2 - t(3)/2, t(2,2,1) = ..., t(2,2,2,1) = ..., and that, with their equations (2.5),(2.7),(2.9), "we observe that" t(2,1) = I(2)/2!, t(2,2,1) = I(4)/4!, t(2,2,2,1) = I(6)/6!, adding "This pattern seems to continue further. However, we have not figured out why yet." So N = 1, 2, 3 are verified in that paper (using Hoffman's appendix relations). Corrected wording: "the cases N = 1, 2, 3 are checked in [CKL, Section 4], using relations from Hoffman's appendix".
5. **Samart/Zheng "Declaration on the use of AI tools"**: Zheng's note says it was prepared with the AI system Kimi. Not relevant to correctness but noted.
6. **Björck and Clark–Laugesen** are used only as quoted in Fan's paper: Björck [1, Theorem 12] (Ark. Mat. 3 (1956) 255-269; for r > 2 an equilibrium measure in R^2 is supported on at most 3 points) and Clark–Laugesen [5, Theorem 8] (Fan's Lemma 5.7, energy of a 3-point set). **I did not open Björck 1956 or Clark–Laugesen myself**; the paper must say "as quoted in Fan".
7. **Kitaev 2025** (cited in formulas.txt [3] from the Habib–Hildebrand reference list): the references in 2606.21145 are [2] A. V. Kitaev, "Painlevé property and generating functions for asymptotics", Zapiski Nauchnykh Seminarov POMI 548 (2025), 101-152, and [7] A. V. Kitaev and A. Vartanian, "The degenerate third Painlevé equation: Complete asymptotic classification of solutions in the neighbourhood of the regular singular point", arXiv 2503.11912 (2025). **Not opened by me** — only cite as "cited in 2606.21145".
8. Furdui–Sîntămărian's conjecture is known to me only **as quoted in Chen–Nguyen** (their ref. [21]: O. Furdui and A. Sîntămărian, "A series involving a product of three consecutive harmonic numbers", Gazeta Matematică, Seria A, 41(120) (2023), 35-38). **Not opened** (journal not accessible). Cite the conjecture as "Conjecture 1 of Chen–Nguyen, attributed there to Furdui and Sîntămărian".
9. Dropped targets (not in paper; not relied on): arXiv:2609.22318 = J. Matuzas, "A quadratic critical-value conjecture for the fifth Bessel moment" (the PDF's own "Generative-AI disclosure" says the conjecture was obtained with an AI chatbot); arXiv:2606.21574 = V. Bravo, P. Carrasco, R. Hernández, O. Venegas, "Sharp coefficient, logarithmic and Schwarzian estimates for alpha-convex functions on the real line" (abstract opened only). Other IDs in TARGETS.md (2610.27261, 2609.34516, 2609.32072, 2609.28707, 2609.26120, 2609.25333, 2301.09699) are scouting leftovers, **not verified, not cited anywhere in results**.

## Verified papers (title, authors, date, quoted statement)

### [HH] arXiv:2606.21145
Rahaf Habib, Roland Hildebrand, "Necessary conditions for the existence of exponential-polynomial expansions for solutions of certain differential equations", submitted 19 Jun 2026 (math.CA).
ODE (1): u''u - (u')^2 = e^{-x} P(u) - 1. Expansion (3): u(x) = sum_{k>=0} p_k(x+c) e^{-kx}, p_k polynomials, p_0(x) = x.
> **Conjecture 7.1.** Let P(t) = sum_{j=0}^d pi_j t^j be a polynomial satisfying the conditions pi_0 = 0, pi_1 = pi_2, and set p_0(x) = x. Then for all k in N_+ there exist polynomials p_k such that the formal series (3) satisfies ODE (1).
> **Conjecture 7.2.** Assume the conditions of Conjecture 7.1, and suppose in addition that pi_j >= 0 for all j = 0, ..., d. Then the coefficients of all resulting polynomials p_k are nonnegative.
Our claim: Conjecture 7.1 proved (results/painleve_series); 7.2 NOT proved. Statement matches.

### [Fi-delta] arXiv:2506.07625
Steven Finch, "Half-Iterates and Delta Conjectures", v1 9 Jun 2025, v6 3 Sep 2025 (math.NT). (the version read is v6.)
Setting: theta(x) = x + sum_{m>=1} c_m x^{m tau + 1}, c_1 = gamma < 0, tau >= 1 integer; Abel's equation g(theta(x)) = g(x) + 1; two algorithms "EJ" and "ML" give g that differ by a constant delta.
> (Addendum III) "Given a polynomial of type x(1 - sigma x^tau - rho x^{2 tau}) where sigma > 0, we believe that delta = ((tau+1)/(2 tau) + rho/(tau sigma^2)) ln(1/(tau sigma)). This extends to transcendental functions, e.g., the Fresnel cosine [4] has delta = (55/108) ln(10/pi^2)."
> (Addendum II, read off the rendered page 7) "The cubics in this paper are all of type x(1 - sigma x - rho x^2), where -infinity < rho < infinity and sigma >= 0. We conjecture, assuming sigma > 0, that delta = (1 + rho/sigma^2) ln(1/sigma)." (This is Addendum III at tau = 1. An earlier version of this file misquoted it as (1 + 2 rho/sigma) ln(1/sigma); that was a transcription error from garbled text extraction and is corrected here.)
> (Section 1 "Clarification", page 7) "A software programming error led to false conclusions in an earlier draft (v3) ... every EJ-based result in that draft about g_14, g_15, g_16 is regretably wrong." We use v6.
> (end of Section 3, page 8) "In essence, delta seems to be completely determined by the parameter tau and two coefficients c_1 & c_2."
Also individual conjectures delta_13 = -(3/4) ln 2, delta_14 = 0, delta_15 = -(3/4) ln 2, delta_16 = -(2/3) ln 3, delta_17 = -(5/9) ln 6, and the listed pairs (e.g. sin x: delta = (3/5) ln 3).
Our claim: one formula delta = -(a/tau) ln(-tau gamma), a = (tau+1)/2 - c_2/gamma^2, which with gamma = -sigma, c_2 = -rho reproduces Addendum III exactly. Need: precise definition of delta in the paper (EJ vs ML) and the hypotheses we assume (see VERIFICATION.md).

### [Fi-AB] arXiv:2503.00579
Steven Finch, "Abel's Functional Equation and Interrelations", v1 1 Mar 2025, v3 18 Mar 2025.
> "the following two conjectured identities are new: A(x/(1+x)) = B(x) + 1, I(x/(1+x)) = J(x) + 1 over the domain (0, infinity)." ... "A formal proof of both identities would be good to see someday."
> **Corrigendum (Section 5):** "The interrelation between A and B turns out to be frivolous." [then shows both are reparametrisations]
Result: KNOWN (author's own corrigendum). Dropped.

### [CN] arXiv:2507.19502
Wilson J. Chen, Vincent Nguyen, "A series involving a product of four consecutive harmonic numbers", 10 Jul 2025 (math.NT).
> "Conjecture 1. If q >= 1 is an integer, then sum_{k=1}^infty H_k H_{k+1} ... H_{k+q} / (k(k+1)...(k+q)) = alpha_{q,2} zeta(2) + alpha_{q,3} zeta(3) + ... + alpha_{q,q+2} zeta(q+2) where alpha_{q,2}, ..., alpha_{q,q+2} are rationals." (attributed to Furdui and Sîntămărian)
> "We note that Conjecture 1 possibly fails when q = 3 ..." [they then prove the q = 3 value contains zeta(2)zeta(3)].
> (last page) "Perhaps we can learn more by computing the closed form for sum_{k=1}^infty H_k H_{k+1}...H_{k+q} / (k(k+1)...(k+q)), (q in N)."
Statement matches our description.

### [XZ] arXiv:2609.11072
Ce Xu, Jianqiang Zhao, "Rational Approximations for Reciprocals of Multiple Zeta Values and Trivariate Cauchy Numbers", 10 Sep 2026.
> "Theorem 5.1. For each order l >= 1, there is some positive integer Gr(l) such that (-1)^{n-1} G_n^{(l)} > 0 for all n >= Gr(l)." [G_n^{(l)}: coefficients of x^l / log^l(1+x)]
> "In particular, we found the exact values Gr(3) = 11, Gr(4) = 36, Gr(5) = 113, Gr(6) = 346, and Gr(7) = 1030 by an easy computer search using the new bound n2(l) ... we would like to know if the following conjecture always holds. **Conjecture 6.1.** For all l >= 5 we have 0.47 * 3^l < Gr(l) < 0.477 * 3^l."
Check of the claim "their own table breaks the conjecture": 0.47 * 3^5 = 114.21 > 113 = Gr(5), the value the paper itself states. So the lower bound of Conjecture 6.1 fails at l = 5 on the paper's own numbers. (Also 0.47*3^8 = 3083.67 > 2995 = our Gr(8).) We read Gr(l) as the *least* integer with the stated property, which is how the paper's exact values are used; their definition in Theorem 5.1 only says "some positive integer", so the paper must be read as intending the minimal one. Their values 11, 36, 113, 346, 1030 are reproduced by our computation (Phase C will re-run).
Also in the paper (same page): r(l) = largest real root of H_l(log z)/pi... "seems to increase by roughly tripling"; upper bound r(l) <= A(l) = exp(pi sqrt((l-1)(l-2)/6)).

### [Sc] arXiv:2610.39051
Francesco Scardino, "On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential", 28 Oct 2026 (math.NA).
> "Conjecture 1. Let k >= 0 and m >= 1 be integers. If m is odd, then all the coefficients of the Taylor expansion of q_{k,m}^{-1}(z) at 0 are positive." (Fasi–Higham [1, Conjecture 3.2])
> "Theorem 8.5. Conjecture 1 is false. In exact rational arithmetic, c_38(66,5) < 0, c_37(44,7) < 0, c_42(45,9) < 0."
> "The counterexamples are not diagonal, and the diagonal case k = m, which is the case relevant in practice, remains open."
q_{k,m}(z) = sum_{j=0}^m (-1)^j C(m,j) (k+m-j)!/(k+m)! z^j. Matches the diagonal-case description. Note: our "failure threshold k*(m) = 2m+12..14" is a statement about where positivity first fails for fixed m as k grows; Scardino's explicit counterexamples have larger k (66 for m = 5). Phase C re-checks the meaning of k*(m).

### [Fan] arXiv:2609.11186
Qiuling Fan, "Riesz capacity ratios with negative exponents", 10 Sep 2026 (math.CA).
> "**Conjecture 5.6 (N odd).** Let r > 2 and P_N be the vertex set of a regular N-gon inscribed in the unit circle (N >= 3). Suppose N is odd. Let theta_N = (N-1)pi/(2N). Then the energy equals U_r(P_N) = 2^{r-1} sin^r theta_N / (1 - 2^{r-2} cos^r theta_N), and an equilibrium measure is supported on the three points 1, e^{2 theta_N i}, e^{2(pi - theta_N) i} (up to rotation), with masses ..."
> "**Conjecture 5.9.** Suppose r >= 2. Let A, B, C be three points on the unit circle. Fix B and C such that they are symmetric with respect to the x-axis, having polar angles phi and -phi, respectively, where phi in (pi/2, 2pi/3]. Move A along the circle with polar angle psi in [0, 2pi - 3phi], so that BC remains the longest side of the triangle ABC. Then the capacity of the three-point set {A,B,C} is maximized when psi = 2pi - 3phi, i.e., when AC = BC."
> "Conjecture 5.6 would follow from applying Conjecture 5.9 and then Lemma 5.8." Lemma 5.8: for r >= 2, A = (1,0), B = e^{i alpha}, C = e^{-i alpha}, alpha in [2pi/3, pi), the capacity of {A,B,C} is nondecreasing in alpha, strictly increasing for r > 2.
Lemma 5.7 (energy of a 3-point set) is quoted from Clark–Laugesen [5, Theorem 8]; Björck [1, Theorem 12]: for r > 2 equilibrium measure in R^2 supported on at most 3 points. Matches; note Conjecture 5.9 is for r >= 2 and 5.6 for r > 2.

### [Kr] arXiv:2610.33699
Valmir Krasniqi, "Noninteger completely monotonic degrees of Stirling remainders and their derivatives", 24 Oct 2026 (math.CO).
> "Theorem 1.2 ... 2 + beta_H <= d_CM(R_2) < 3, 3 + beta_K <= d_CM(-R_2') < 4. In particular, 8/3 < d_CM(R_2) < 3, 32/9 < d_CM(-R_2') < 4."
> "Theorem 1.3. ... delta_{n,m} = d_CM(f_{n,m}) - (2n+m-2), J = int_0^{2pi} (1 - cos u)/u du > 0. Then limsup_{n->infinity} (2n-1) sup_m delta_{n,m} <= 2 pi^2 / J. For each fixed m >= 0, liminf (2n-1) delta_{n,m} >= 3/pi."
> Abstract: "The exact real degrees and the optimal asymptotic constants remain open."
Our values d(R_2) = 2.8667042552, d(-R_2') = 3.7984354776 lie inside the proven intervals. Our numerical extrapolation (2n-1) delta_{n,0} -> 8.0974 +- 3e-4 versus the bound 2 pi^2 / J = 8.0976 is a numerical observation only. (2 pi^2/J with J = Cin(2 pi) = 2.4379...; value 8.097627 as computed earlier.)

### [Fi-C] arXiv:2503.13378
Steven Finch, "Exercises in Iterational Asymptotics III", 17 Mar 2025.
> "C(x0) = lim_{n->inf} (x_n - n)" ... "C''(2) ~ [f(2+e) - 2f(2) + f(2-e)]/e^2 = 0.37462642198301734111.... The latter does not match the earlier 0.3909 estimate, contradicting our uniformity supposition. An independent confirmation of the 0.3746 estimate remains open."
Our claim: exact series for C''(2) with value 0.374626421983017341116776...; agrees with Finch's 20 digits. So this is an independent confirmation (as asked), not a new value.

### [Fi-T] arXiv:2509.24918
Steven Finch, "Exercises in Iterational Asymptotics IV", 29 Sep 2025.
> "It would be good to see the values of T(4/3, 1/2), T(5/4, 1/2) and T(6/5, 1/2) someday."
Our claim: values to 40 digits (VERIFIED numerically; Phase C will recompute with fresh code and check definition of T).

### [Wi] arXiv:2512.07028
Halina Wiśniewska, "Some inequalities for Gurland's ratio of the gamma functions", 7 Dec 2025 (math.CA). Author name appears as "Halina Wisniewska" in the abstract listing.
> "Open problems: 1. In Corollary 1 we showed that R_{nm}(x,y) -> 0 under a sufficient condition. Does R_{nm}(x,y) -> 0 hold for every x,y > 0? 2. Does ln G*(x,y) = S_infinity(x,y) hold generally, and if not, how large the difference ln G*(x,y) - S_infinity(x,y) can be? 3. How is t(x,y) located in the interval [sqrt(xy), (x+y)/2]? What is the distance from t(x,y) to the midpoint of this interval?"
Matches.

### [CKL] arXiv:2111.07097
Sarth Chavan, Masato Kobayashi, Jorge Layja, "Integral Evaluation of Odd Euler Sums, Multiple t-Value t(3,2,...,2) and Multiple Zeta Value zeta(3,2,...,2)", 13 Nov 2021 (math.NT). No journal reference listed on the arXiv page.
> "**Conjecture 4.5.** Let N in N, then the following identity holds. t({2}^N, 1) = I(2N)/(2N)! = (1/2^{2N}) ( sum_{j=0}^{N-1} (-1)^j pi^{2N-2j}/(2N-2j)! * eta(2j+1) + (-1)^N * 2 (1 - 2^{-2N-1}) * zeta(2N+1) )." (read off the rendered page 9 of the PDF, not from the garbled text extraction; eta is the Dirichlet eta function. Check N = 1: (1/4)((pi^2/2) ln 2 - (7/4) zeta(3)) = (pi^2/8) ln 2 - 7 zeta(3)/16 = t(2,1), as in the paper's display.)
> "Notice that t({2}^N, 1) is a MtV appearing in Saha's conjecture [16]."
Here I(n) = int_0^{pi/2} theta^n cot(theta) d theta (as defined in the paper), t = Hoffman's multiple t-value. See correction 4. Whether anyone proved Conjecture 4.5 after 2021 is a Phase B question (NOVELTY.md).

### [Zh] arXiv:2608.02265
Huimin Zheng, "Samart's conjecture n4(81) = 40M7: the exact CM evaluation and the two obstructions. A status report, companion to Mahler measures at interior CM points", 3 Aug 2026 (math.NT).
> "n4(81) - 40M7 = +0.0586706795972872..., five orders of magnitude above the integration error floor, so the identity as literally stated is refuted; a closed form for the true value n4(81) remains open" ; "EK4(tau_2) = 40M7" (Theorem 3.4); n4(81) = 4.1655349907533676508(5).
Result: our Samart item is KNOWN (see correction 2).

### [Ga] arXiv:2012.02524
Armengol Gasull, "Some open problems in low dimensional dynamical systems", 4 Dec 2020 (math.DS).
> "In [34] it is proved that p_n <= 1/2^n, so lim p_n = 0. Furthermore, it is also shown that p_1 = 1/2, p_2 = 1/4, p_3 = 1/16, p_4 < 1/32, and, by using Monte Carlo simulation, that p_4 ~ 0.0092 and p_5 ~ 0.0007. Hence the following questions arise: **Problem 21.** Let p_n be the probability that the zero solution of the n-th order linear random differential equation (18) is globally asymptotically stable. Find the asymptotic expansion of p_n at n = infinity. Is it true that the sequence p_n is strictly decreasing?" (coefficients i.i.d. N(0,1); stable iff all roots of the characteristic polynomial have negative real part).
Our p_4 = 0.0092838447... agrees with the paper's Monte Carlo 0.0092. **Our computation does not answer Problem 21** (it asks for an asymptotic expansion and monotonicity).

### [FH] Fasi & Higham, MIMS EPrint 2018.36
Massimiliano Fasi, Nicholas J. Higham, "An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential", MIMS EPrint 2018.36, Manchester Institute for Mathematical Sciences, version of 19 March 2019 (https://eprints.maths.manchester.ac.uk/2691/1/fahi19.pdf; opened and read; 25 pages). **Only the eprint is cited** (journal details were not verified by me).
> "Conjecture 3.2. Let k, m in N. If m is odd, then all the coefficients of the series expansion of q_{km}(z)^{-1} at 0 are positive." (Section 3, after the remark that "most optimal degrees are, in fact, odd"; "since we do not have a proof of the conjecture we will bound the truncation error of r_{km} for any k and m.")
Matches the statement as quoted by Scardino. Added after Phase B noted this had not been opened.

### Papers added after Phase A (opened and read by me)
* **[HH2]** Roland Hildebrand, Rahaf Habib, "Sufficient conditions for the existence of exponential-polynomial expansions for solutions of certain differential equations", arXiv:2606.24182, submitted 23 Jun 2026 (math.CA). Authors in the order printed on the PDF: Roland Hildebrand, Rahaf Habib. Quote: "Theorem 2.5. Let deg P = d >= 2, pi_0 = 0, pi_1 = pi_2. Then for all k >= 1 there exist polynomials p_k(x;P) with degree deg p_k = (d-2)k+1, such that with p_0(x) = x and for every c in C the formal series (4) is a solution of ODE (1)." Abstract: "These conditions amount to P(0) = 0 and P'(0) = (1/2)P''(0). Here we show that these two conditions are also sufficient."
* **[Charlton]** Steven Charlton, "On motivic multiple t values, Saha's basis conjecture, and generators of alternating MZV's", arXiv:2112.14613v1, 29 Dec 2021 (math.NT). Section 3.3 "Evaluation of t(1,{2}^n)": "In order to answer a question posed in [6], we turn to the special case of t(1,{2}^n), for n >= 1. ... This confirms Conjecture 4.5 on the evaluation of t(1,{2}^n) stated in [6] (be aware, the opposite MZV/MtV convention is used therein). The authors of [6] also write the Dirichlet eta function eta(m) = (1-2^{1-m})zeta(m), with eta(1) = log(2), in place of -zeta(m) used herein." ([6] = arXiv:2111.07097.)
* **[LY]** Oscar Lanford III, Michael Yampolsky, "The fixed point of the parabolic renormalization operator", arXiv:1108.2801 (v1 13 Aug 2011; v3 13 Oct 2012). Section 2.2: for f(z) = z + z^2 + alpha z^3 + O(z^4) and F(w) = -1/f(-1/w) = w + 1 + A/w + O(w^-2), A = 1 - alpha; "Proposition 2.14. There is a unique sequence b_1, b_2, ... of complex coefficients such that Phi_ps(w) = w - A log(w) + sum_j b_j w^{-j} satisfies Phi_ps o F = Phi_ps + 1 in the sense of formal power series." (This is the logarithmic coefficient a = (tau+1)/2 - c_2/c_1^2 of our Proposition at tau = 1, c_1 = 1, c_2 = alpha.)
* **[XW]** Ce Xu, Weiping Wang, "Explicit formulas of Euler sums via multiple zeta values", arXiv:1805.08056 (v1 17 May 2018, v3 5 Jul 2019), math.NT; abstract opened only (explicit formulas expressing Euler sums through multiple zeta values).
* **[FS]** P. Flajolet, B. Salvy, "Euler sums and contour integral representations", Experiment. Math. 7 (1998), no. 1, 15-35: bibliographic details taken from a Project Euclid listing seen in search results; **not opened**; cited only as the standard reference for reducing Euler-type sums to zeta values.
* **[Arb]** arblib.org (opened): Arb, a C library for arbitrary-precision ball arithmetic by Fredrik Johansson and contributors; the page says Arb was merged into FLINT in 2023 and gives no citation text, so no paper is cited.

## Not opened
* Furdui–Sîntămărian (Gazeta Matematică 2023): journal not accessible.
* Björck (1956), Clark–Laugesen (SIAM J. Math. Anal. 2025, Anal. Math. Phys. 2025), Hoffman (Commun. Number Theory Phys.), Saha (arXiv:1712.06325), Fasi–Higham: used only through the papers above.
* Kitaev 2025 and Kitaev–Vartanian arXiv:2503.11912: referenced by [HH] only.
