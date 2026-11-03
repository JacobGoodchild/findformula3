# Novelty check part 4 (items A-D), run 3 Nov 2026

Caveat: WebSearch is a summarising search tool; "opened" below means fetched with WebFetch or downloaded. Semantic Scholar citation API: A returned an empty list (paper 6 days old, so not informative), B and C returned HTTP 429 (not retried, to avoid hammering). No papers citing any of the four sources were found by any route.

## ITEM A: Pade positivity (Scardino, arXiv:2610.39051)

Queries (11):
1. Fasi Higham conjecture positivity Taylor coefficients reciprocal Pade denominator matrix exponential odd m
2. reverse Bessel polynomial reciprocal power series coefficients positive
3. Scardino "positivity conjecture" Fasi Higham Pade approximants matrix exponential
4. zeros of Pade approximants to exp smallest modulus real zero denominator Bessel polynomial Saff Varga
5. Taylor coefficients of 1/y_n(1/z) Bessel polynomial zeros positive real zero minimal modulus odd degree
6. Fasi Higham arbitrary precision scaling and squaring ... "conjecture" denominator reciprocal coefficients positive
7. diagonal Pade approximant exponential denominator 1/q_m(z) power series nonnegative coefficients proof computer-assisted 2026
8. Carpenter Varga Waldvogel asymptotics zeros partial sums exp / Pade denominator zeros Bessel polynomial smallest modulus
9. WebFetch arxiv listing math.NA/new (any Pade positivity paper?) -> none
10. WebFetch Semantic Scholar citations of 2610.39051 -> empty
11. WebFetch eprints.maths.manchester.ac.uk/2691 (Fasi-Higham)

Opened:
- https://arxiv.org/abs/2610.39051 : Scardino, v1 only (28 Oct 2026), math.NA/math.CA. Abstract confirms: positivity for k=0; eventual positivity under a condition on the unique positive real zero, computable threshold; holds for each fixed odd m and large k (Hermite scaling); unrestricted conjecture false with exact rational counterexamples (limiting profile negative for m=5); "leaves the diagonal case k=m ... open". I only saw the abstract, not the body, so I did not check whether the paper contains any numerical remarks about the diagonal case or about k*(m).
- https://eprints.maths.manchester.ac.uk/2691/ : Fasi & Higham, "An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential" (PDF https://eprints.maths.manchester.ac.uk/2691/1/fahi19.pdf; later version https://eprints.maths.manchester.ac.uk/2721/). I did not open the PDF, so I did not personally confirm "Conjecture 3.2" numbering/wording.
Snippets only (not opened): Driver & Temme on diagonal Pade zeros (https://www.nisc.co.za/products/abstracts/9130/zero-and-pole-distribution-of-diagonal-pad-approximants-to-the-exponential-function); Stahl ETNA survey (https://emis.dsd.sztaki.hu/journals/ETNA/vol.25.2006/pp480-510.dir/abstr480-510.pdf); Dunster-Gil-Ruiz-Antolin-Segura reverse generalized Bessel zeros (https://arxiv.org/pdf/2510.14295); zeros of Bessel polynomials, real zero asymptotics (https://arxiv.org/pdf/1105.0957); Wikipedia Bessel polynomials; OEIS A001880.

Findings: No paper found that settles the diagonal case, treats positivity of the Taylor coefficients of 1/q_{m,m}, or states a law k*(m) ~ 2m+12..14. No citing paper found. Classical zero-location results (Saff-Varga 1970s, Driver-Temme 1999, Stahl) concern asymptotic zero distributions, not the sign pattern of the reciprocal's Taylor series or the minimal-modulus real zero. A claim that the real zero of reverse Bessel polynomials of odd degree has minimal modulus was not found stated anywhere, though I could not read Saff-Varga or Grosswald directly (so this is an absence in what I could reach, not proof of absence).

Label: NOT FOUND (diagonal case closed up to m<=361, and the k*(m) numerical law). Credit: Fasi-Higham for the conjecture; Scardino for eventual positivity, the (66,5),(44,7),(45,9) counterexamples, and for posing the diagonal case. Caution: Scardino's paper is 6 days old and only v1; a v2 or follow-up could appear, and I only read its abstract.

## ITEM B: Stirling remainder CM degrees (Krasniqi, arXiv:2610.33699)

Queries (9):
1. Krasniqi "Noninteger completely monotonic degrees of Stirling remainders"
2. exact completely monotonic degree remainder Stirling formula ln Gamma R_2 numerical value 2.8667
3. Mahmoud Qi completely monotonic degree remainder asymptotic expansion log gamma conjecture 2(n-1)
4. completely monotonic degree Stirling remainder "Cin" asymptotic constant 2pi^2 fractional excess Laplace representation Bernoulli
5. Bouali completely monotonic degree remainders ln Gamma digamma conjectures Qi Zhu 2022-2025
6. arXiv 2026 completely monotonic degree real noninteger remainder log gamma digamma exact value computed
7. WebFetch arxiv.org/abs/2610.33699
8. WebFetch arxiv.org/abs/2202.01801 (Bouali)
9. Semantic Scholar citations -> HTTP 429

Opened:
- https://arxiv.org/abs/2610.33699 : Krasniqi, v1 only (24 Oct 2026), listed math.CO. Abstract: disproves three real-degree conjectures of Mahmoud and Qi; unified proof of integer-degree formula (resolves Zhu's conjectures for higher derivatives in this range); every real CM degree lies strictly between the integer and next integer; fractional lower bound, rational bound, uniform upper bound fixing the order of decay of the excess; "The exact real degrees and the optimal asymptotic constants remain open."
- https://arxiv.org/abs/2202.01801 : Bouali, abstract only: confirms some conjectures, double inequalities (snippet: 2(n-1) <= deg < 2n-1 style bounds) for gamma/digamma remainders.
Snippets only: Qi-Mahmoud https://arxiv.org/pdf/1912.07989 (MIA 25 (2022) 291-306); Qi https://arxiv.org/abs/2003.05300 (trigamma); Zhu, AIMS Math 2020 https://www.aimspress.com/article/doi/10.3934/math.2020224 (integer degrees).

Findings: No source found that gives numerical real values of d_CM(R_n) (nothing containing 2.8667 or 3.798), nor the limit constant ~8.0974 / sharpness of 2 pi^2/Cin(2 pi). The literature found is all bounds/integer degrees. Note Krasniqi's own statement that exact degrees and optimal constants are open, 9 days before today.

Label: NOT FOUND. Credit: Krasniqi (bounds and the 2pi^2/J limsup bound), Mahmoud-Qi, Qi-Liu, Zhu, Bouali (integer-degree line). Note the claimed numerics are only numerical (not proved), so they should be presented as numerical evidence; nothing found contradicts them. Not verified: whether Krasniqi's body or Mahmoud-Qi's paper has a numeric table (only abstract read).

## ITEM C: Gurland ratio (Wisniewska, arXiv:2512.07028)

Queries (9):
1. Gurland's ratio gamma functions inequalities Wisniewska
2. Gurland ratio Gamma(x)Gamma(y)/Gamma((x+y)/2)^2 series representation Hurwitz zeta Taylor expansion log gamma
3. Merkle "Gurland" ratio gamma function bounds Comput. Math. Appl. 2005
4. Gurland ratio mean value theorem t(x,y) location (x+y+sqrt(xy))/3
5. Taylor series ln Gamma(a+z) polygamma Hurwitz zeta radius of convergence, even part
6. Alzer Gurland ratio gamma sharp bounds Natalini Laforgia Kairies convexity log gamma
7. WebFetch arxiv.org/abs/2512.07028 and arxiv.org/html/2512.07028v1
8. WebFetch DLMF 25.11 and DLMF 5.15
9. Semantic Scholar citations -> HTTP 429

Opened:
- https://arxiv.org/html/2512.07028v1 : v1 only (7 Dec 2025). Open problems quoted: (1) "Does R_n^m(x,y)->0 hold for every x,y>0?" (2) "Does ln G*(x,y)=S_inf(x,y) hold generally ...?" (3) location of t(x,y) in (sqrt(xy),(x+y)/2) and distance to midpoint. Theorem 1: ln G*(x,y)=sum_{k=1}^{m-1}(1/k)((x-y)/2)^{2k} zeta(2k,1+(x+y)/2)+R, G* defined with Gamma(1+x)Gamma(1+y)/Gamma(1+(x+y)/2)^2. Sufficient condition Q=|x-y|/(2(1+sqrt(xy)))<1. The paper does NOT mention the Taylor expansion of ln Gamma or a radius of convergence.
- https://dlmf.nist.gov/25.11 (first 100k chars): eq 25.11.12 zeta(n+1,a)=(-1)^{n+1}psi^{(n)}(a)/n!; 25.11.17; 25.11.18. https://dlmf.nist.gov/5.15 : polygamma facts. Neither page displays the Taylor expansion of ln Gamma(a+z) with its radius explicitly in what I read; DLMF 5.7 not opened.
Snippets: Merkle 2005 (Comput. Math. Appl. 49, 389-406) cited via https://arxiv.org/pdf/0902.2514; Chen-Choi MIA 2017; Yang MIA 22 (2019) https://neomath.ele-math.com/mia/22-07/...; https://neomath.ele-math.com/mia/20-43/...; Alzer, Math. Comp. 60 (1993) https://www.ams.org/journals/mcom/1993-60-201/S0025-5718-1993-1149288-7/.

Findings:
- Problems 1 and 2: my own check of the argument: ln Gamma(a+z)+ln Gamma(a-z)-2 ln Gamma(a) has even Taylor part sum_k 2 psi^{(2k-1)}(a) z^{2k}/(2k)! = sum_k zeta(2k,a) z^{2k}/k (using 25.11.12), with a=1+(x+y)/2, z=(x-y)/2; nearest singularity of ln Gamma(a+z) is at z=-a, radius a, and |z|<a always holds for x,y>0 (|x-y|<2+x+y). So the claimed one-line argument is sound and the coefficient 1/k is consistent with Theorem 1. The Taylor expansion of ln Gamma about a point with polygamma/Hurwitz coefficients is elementary and standard (it is the identity DLMF 25.11.12 plus Taylor's theorem), but I did not find it written out with this exact radius statement in DLMF pages I read, so cite it as "standard consequence of DLMF 25.11.12", not as a numbered DLMF formula. One caveat: the paper's R_n^m remainder is defined via a Weierstrass-product splitting, so "R_n^m->0" should be matched to the Taylor remainder; the Taylor argument gives S_inf convergence and equality directly, which answers Problem 2, and Problem 1 follows if the paper's partial sums are the same objects.
- Problem 3: no source found for the 1/3 constant or t > (x+y+sqrt(xy))/3. Remains numerics only.
- No follow-up paper found answering the open problems.

Label: Problems 1-2: "probably known" in the sense that the argument is an elementary standard special-function fact (not stated in any source I found as an answer to this question; no prior answer found). Problem 3 inequality: "not found".

## ITEM D: p_4 (Gasull, arXiv:2012.02524, Problem 21)

Queries (8):
1. probability asymptotically stable random linear differential equation Gaussian coefficients Routh-Hurwitz p_4 Monte Carlo 0.0092
2. probability that a random polynomial is Hurwitz stable all roots left half-plane iid Gaussian degree n asymptotics
3. Litvin Boreisha stochastic Routh-Hurwitz problem
4. Cima Gasull Manosa "Stability index of linear random dynamical systems" citations follow-up
5. probability random Hurwitz polynomial stable Gaussian exact value degree 4 closed form integral decay rate p_n
6-8. WebFetch arxiv abs 2012.02524, full PDF of 2012.02524 (read locally with pdftotext), full PDF of 1904.05725 (pdftotext)

Opened:
- https://arxiv.org/pdf/2012.02524 : Problem 21 text confirmed: p_n for iid N(0,1) coefficients A_n..A_0; "In [34] it is proved that p_n <= 1/2^n ... p_1=1/2, p_2=1/4, p_3=1/16, p_4<1/32, and, by Monte Carlo, p_4 ~ 0.0092 and p_5 ~ 0.0007." Asks for asymptotic expansion and strict monotonicity. Ref [34] = Cima, Gasull, Manosa, "Stability index of linear random dynamical systems", EJQTDE 2021, No. 15 (DOI 10.14232/ejqtde.2021.1.15).
- https://arxiv.org/pdf/1904.05725 (the [34] paper, v2 Dec 2020): abstract/intro states r_4 ~ 0.00925, r_5 ~ 0.00071 from a "two step approach" (Monte Carlo + least-squares with linear constraints), r_k<10^-4 for larger k; only r_1,r_2,r_3 exact. Text says analytic solution only for n=1 in other settings. No closed form, no elliptic integral, no more digits found for p_4 or p_5.
Snippets only: Litvin & Boreisha, "Stochastic Routh-Hurwitz problem", Cybern. Syst. Anal. 27 (1991) 527-534, https://link.springer.com/article/10.1007/BF01130362 (abstract only: probability of stability for polynomial with random coefficients; could not read, distributional assumptions unknown, so it is possible it contains exact results for small n; this is a gap). Ghosal-Mukherjee persistence https://www.arxiv.org/abs/2410.20714 (different event). Citation count for [34]: UAB repository lists WoS 1, Scopus 3 (https://ddd.uab.cat/record/239773), unidentified citers.

Findings: The estimate 0.0092838447243 is consistent with 0.00925 in [34] and 0.0092 in Gasull (Monte Carlo accuracy ~1e-4). No source found with more digits or a closed form. No paper found on the asymptotics of Hurwitz-stability probability of Gaussian polynomials. Unresolved: Litvin-Boreisha 1991 (paywalled) may contain exact formulas/integral reductions for small n; the claim should say it was not checked.

Label: NOT FOUND for high-precision p_4 (prior: Monte Carlo 0.00925 in Cima-Gasull-Manosa; 0.0092 in Gasull). Problem 21 itself not answered, as stated.
