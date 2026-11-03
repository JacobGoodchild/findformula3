# Novelty check, part 1 (items A, B, C), done 3 Nov 2026

Tools: WebSearch + WebFetch only. Nothing posted anywhere. Semantic Scholar citation API returned data for paper A only; for B and C it returned HTTP 429 (not retried more than once). "Opened" = full text read (PDFs downloaded by the fetch tool and converted with pdftotext); "snippet" = seen only in search results.

## ITEM A: Habib-Hildebrand arXiv:2606.21145, Conjecture 7.1

**LABEL: KNOWN.** Conjecture 7.1 was proved by the same authors four days after the source paper, with essentially the same proof idea as our claimed proof.

### Queries run
1. Semantic Scholar citations of arXiv:2606.21145 (WebFetch, worked: one citing paper)
2. `Habib Hildebrand exponential-polynomial expansions solutions differential equation u''u-(u')^2 = e^{-x}P(u)-1 conjecture`
3. `Vartanian trans-series degenerate third Painlevé equation SIGMA 21 (2025) 067 exponential-polynomial expansion`
4. `Kitaev "Painlevé property and generating functions for asymptotics" Zapiski Nauchnykh Seminarov POMI 548`
5. `Hildebrand Habib degenerate Painlevé III trans-series nonnegative coefficients polynomials p_k conjecture proof 2026`
6. `Kitaev Vartanian degenerate third Painlevé equation complete asymptotic classification regular singular point Conjecture C.1 arXiv 2503.11912`
7. WebFetch of arxiv abs pages 2606.21145, 2606.24182, 2512.14970; full text of 2606.24182; html of 2503.11912v2 (two chunks, Appendix C not reached)

### Pages
- https://arxiv.org/abs/2606.24182 and PDF https://arxiv.org/pdf/2606.24182 (OPENED, full text). R. Hildebrand and R. Habib, "Sufficient conditions for the existence of exponential-polynomial expansions for solutions of certain differential equations", submitted 23 Jun 2026 (v1), math.CA. Abstract: the necessary conditions P(0)=0, P'(0)=P''(0)/2 "are also sufficient". Theorem 2.5: for deg P = d >= 2, pi_0 = 0, pi_1 = pi_2, for all k >= 1 there exist polynomials p_k with deg p_k = (d-2)k+1 such that the formal series sum p_k(x+c) e^{-kx} solves ODE (1) for every c. This is exactly Conjecture 7.1 (and adds the degree formula). Paper does not mention "Conjecture 7.1" by number but cites 2606.21145 as [1] and says it "shows by induction" the conditions are sufficient.
  - Proof method (read in full): induction on s; Lemma 2.2 solvability iff (q_{s,s} e^{-sx})''|_{x=0}=0; Kitaev's trick (insert parameter a, replace e^{-x} by a e^{-x}, from Kitaev's Zapiski POMI 548 paper) in Lemma 2.3; Lemma 2.4 expands the residual D_s''(x;a) at the zero x_0(a) of the truncated series U_{s-1}(x;a) (implicit function theorem) and finds D_s'' = O(a^{s+1}) there, hence Phi_{s,s}(0)=0. This is the same "local expansion at the zero of the truncated series" argument as the claimed result. Section 3 also discusses solutions near a zero (conditions pi_0=0, pi_1=pi_2 equivalent to existence of holomorphic solutions near a zero with u'=1).
  - Section 4 spells out consequences for degenerate PIII: P=t^3 (D7, y = t u(-2 log t)), P=t^4 (D8, y = t u(-2 log t)^2), P=t^6 (y = 8 t^{-1} u(-4 log t + 9 log 2)^{-2}). So P = t^3, t^4, t^6 are covered as formal series.
  - Section 5: does NOT prove convergence of the series, nor nonnegativity of coefficients of p_k (numerically suggested; this is the other conjecture of the source paper and is still open as far as found).
- https://arxiv.org/abs/2606.21145 (OPENED abstract page only; PDF not read by me beyond search snippets). Habib-Hildebrand, submitted 19 Jun 2026, v1 only. Necessary conditions + numerical evidence for sufficiency.
- Semantic Scholar API for 2606.21145 (OPENED): exactly one citing paper, 2606.24182.
- https://arxiv.org/abs/2512.14970 (abstract only) A. Kitaev, "Painlevé property and generating functions for asymptotics" (Zap. Nauchn. Sem. POMI 548, 2025, pp. 101-152; https://m.math-net.ru/eng/znsl7659 seen in snippet). Formal series in two variables for degenerate PIII; supplies the parameter trick used by Hildebrand-Habib. I did not read it; no evidence it states Conj. 7.1.
- https://arxiv.org/abs/2503.11912 (Kitaev-Vartanian, "The degenerate third Painlevé equation: complete asymptotic classification ... regular singular point") opened partially via html v2 (only first ~100k and a middle chunk; Appendix C, which has Conjecture C.1, NOT reached). 2606.24182 says only that "[3, Conjecture C.1] has already suggested that such series exist for special families of solutions of other degenerate PIII equations". So C.1 is a conjecture, not a theorem implying Conj 7.1; it concerns small-tau (regular singular point) regime, different from the x->+inf trans-series here. I could not read its statement.
- https://imath.kiev.ua/~sigma/2025/067/sigma25-067.pdf (snippet/search only) Vartanian, "Trans-series asymptotics of solutions to the degenerate Painlevé III equation: a case study", SIGMA 21 (2025) 067 (arXiv:2010.11235). Isomonodromy trans-series for one particular degenerate PIII; does not address general P nor exponential-polynomial expansions with polynomial coefficients. Not read in full.

### Justification
Known: a complete proof (Theorem 2.5 of 2606.24182) by the original authors, 23 Jun 2026, the same technique. Any write-up of our proof should be presented as an independent re-derivation, not as new. What remains open (per what I found): convergence of the series, nonnegativity of coefficients of p_k, and the other conjecture 7.2 (whatever it is in our notes). Credit: Habib and Hildebrand (2606.21145, 2606.24182); Kitaev (parameter-a technique).

---

## ITEM B: Fan arXiv:2609.11186, Conjectures 5.6 and 5.9

**LABEL: not found** (no proof in the literature that I could locate), with one unverified third-party claim noted below.

### Queries run
1. Semantic Scholar citations of arXiv:2609.11186 (HTTP 429, twice; no data)
2. `Qiuling Fan Riesz capacity ratios with negative exponents`
3. `equilibrium measure vertex set regular N-gon odd N Riesz energy negative exponent supported on three vertices`
4. `maximal Riesz energy subsets of the circle exponent s<0 Björck support equilibrium measure finitely many points`
5. `Clark Laugesen Riesz capacity three-point set regular polygon odd N equilibrium measure conjecture proof`
6. `Riesz capacity negative exponents three points circle Fan Conjecture 5.9 proved`
7. `maximizing sum |x_i-x_j|^r over probability measures on finite subset of circle r>2 Björck 1956 distributions of positive mass which maximize a certain generalized energy integral`
8. `Laugesen Fan arXiv 2026 Riesz capacity regular simplex ball ratio negative exponents equilibrium measure polygon`
9. `"regular polygon" vertices maximal energy sum of r-th powers of distances r>2 three vertices odd number of points circle maximum probability measure`
10. `arXiv October 2026 Riesz capacity polygon vertex set equilibrium measure odd conjecture Fan proof` (extended)
11. `the-omega-institute trureturing FanCircleCapacity Conjecture 5.9 three-point capacity`

### Pages
- https://arxiv.org/pdf/2609.11186 (OPENED, full text via pdftotext). Q. Fan, submitted 10 Sep 2026, v1 only (as seen), code at GitHub vhdvhd/Riesz-capacity-ratios-with-negative-exponents (not opened). Conjecture 5.6 and 5.9 statements match the task text. Paper proves "Step 1" (Lemma 5.8: symmetric isosceles case, derivative of U_r(alpha) = 2^{r-1} sin^r(alpha/2)/(1-2^{r-2}cos^r(alpha/2))), says Conj 5.9 would imply 5.6, and that its attempt at 5.9 is "unsuccessful" (monotonicity in psi; sign of l(psi)=AB^r+AC^r-BC^r not monotone). Numerics checked exhaustively only for odd N <= 50 on plotting grids. Tools it uses: Björck [1, Thm 12] (support on at most 3 points in the plane for r>2), Clark-Laugesen [5, Thm 8] (three-point capacity formula, Lemma 5.7). Even N is done (Cor. 5.5, two antipodal points).
- https://arxiv.org/pdf/2410.14809 (snippet/search; PDF saved but not read) Clark-Laugesen, "Maximizing Riesz capacity ratios: conjectures and theorems": Theorem 8 (capacity of three-point set), regular k-point set result. Search snippets give no odd-polygon statement.
- Björck, "Distributions of positive mass which maximize a certain generalized energy integral", Ark. Mat. 3 (1956) 255-269, https://doi.org/10.1007/BF02589412 (snippet only; full text not opened). Gives the support-size theorem and the continuous results; I found no statement for finite vertex sets of odd regular polygons.
- https://arxiv.org/abs/2609.05622 (abstract) "Distance energies and negative type of flat tori": maximizers on tori, finite supports (2-torsion pairs, order-3 cyclic subgroups on hexagonal torus). Related flavour but different setting (tori, d>=2), no polygon vertex-set result.
- https://arxiv.org/abs/2602.19311 (abstract) Steinerberger, distance equilibrium measures and curvature: not relevant to polygons.
- https://arxiv.org/abs/2603.04649 (abstract) Clark-Laugesen, "Riesz energy deformation through insulated strips" (4 Mar 2026): not relevant.
- https://arxiv.org/html/2610.04811v1 (OPENED abstract/text summary) Riesz vs logarithmic capacity inequalities; no negative exponents, no mention of Fan's conjectures.
- https://arxiv.org/pdf/1108.4652 and https://arxiv.org/pdf/1211.2975 (snippets) Nikolov-Rafailov on sums of powered distances from a point to polygon vertices: a different problem (extremum over position of a point), not equilibrium measures.
- https://github.com/the-omega-institute/trureturing/issues/16136 (OPENED). Issue dated 13 Oct 2026 by a bot account in an AI/Lean-formalisation project ("Preregistration: Fan Conjecture 5.6, equilibrium on every odd regular polygon"). It explicitly says it is NOT a proof and claims no settlement of 5.6. It says that a "public project exclusion page records 5.9 as proved" and that a Lean declaration `D5/S3/Geometry/Distances/FanCircleCapacity.result` "supplies the three-point comparison of Conjecture 5.9". No URL for that page and no compiled/reviewed proof; I could not locate the claimed proof (repo front page https://github.com/the-omega-institute/trureturing and commit be6ac13 opened; neither mentions Fan or Riesz). TREAT AS AN UNVERIFIED, UNREVIEWED CLAIM. It means a competing (possibly machine-generated) argument for 5.9 may exist; worth a re-check before sending anything to the author.

### Justification
No arXiv paper, journal article or author page found that proves either conjecture or contains the odd-N three-vertex statement before Fan. Björck's theorem plus Clark-Laugesen Theorem 8 give the tools but not the statement; the even-N case is in Fan's own Cor. 5.5. Earlier work on "equilibrium measures of regular N-gon vertex sets" for logarithmic/Riesz kernels with r>2 turned up nothing (note that for 0<r<2 the answer is uniform weights, Fan Lemma 5.3, a standard symmetry fact). Caveats: Semantic Scholar was unreachable, so a citing paper could have been missed; I only checked arXiv-level search up to ~13 Oct 2026; Björck's 1956 paper was not read, so I cannot exclude that a remark there covers vertex sets of polygons (unlikely: Fan, an expert, cites it only for the 3-point support). Credit: Fan (conjectures, Lemma 5.8), Clark-Laugesen (Thm 8), Björck (support theorem).

---

## ITEM C: Chavan-Kobayashi-Layja arXiv:2111.07097, Conjecture 4.5, t({2}^N,1)

**LABEL: KNOWN.** Proved by S. Charlton, arXiv:2112.14613 (posted Dec 2021, about six weeks after the conjecture), Section 3.3, which states that it "confirms Conjecture 4.5".

### Queries run
1. `multiple t-values t({2}^n,1) evaluation conjecture Chavan Kobayashi Layja`
2. Semantic Scholar citations of 2111.07097 (HTTP 429, no data)
3. `Charlton "On motivic multiple t values, Saha's basis conjecture" t(1,{2}^n) evaluation confirms conjecture Chavan Kobayashi Layja`
4. `Hoffman "An odd variant of multiple zeta values" t(2,...,2,1) evaluation`
5. `Murakami "On Hoffman's t-values of maximal height and generators of multiple zeta values" Mathematische Annalen`
6. `integral ∫_0^{π/2} θ^{2n} cot θ dθ multiple t-value t({2}^n,1) Euler sum eta zeta formula`
7. WebFetch: arxiv abs and full text of 2111.07097, 2204.14183, 2212.09070, 2112.14613

### Pages
- https://arxiv.org/pdf/2112.14613 (OPENED, full text). S. Charlton, "On motivic multiple t values, Saha's basis conjecture, and generators of alternating MZV's" (published Math. Ann. 392 (2025) 1995-2079 per search snippet). Theorem 1.1 / 3.3: evaluation of stuffle-regularised t^{*,V}({2}^a,1,{2}^b) in terms of zeta(2r+1) t({2}^{a+b-r}), log 2 and V; Prop 3.7 gives the shuffle-regularised version. Section 3.3 "Evaluation of t(1,{2}^n)": derives
  t(1,{2}^n) = (1/2^{2n}) sum_{r=0}^{n-1} (-1)^r (-zeta(2r+1)) pi^{2(n-r)}/(2(n-r))! + (-1)^n 2 (1-2^{-2n-1}) zeta(2n+1) (/2^{2n} overall), and says verbatim: "This confirms Conjecture 4.5 on the evaluation of t(1,{2}^n) stated in [6] (be aware, the opposite MZV/MtV convention is used therein). The authors of [6] also write the Dirichlet eta function eta(m) = (1-2^{1-m}) zeta(m), with eta(1)=log 2, in place of -zeta(m) used herein." Here [6] is Chavan-Kobayashi-Layja arXiv:2111.07097 (checked in its reference list). Charlton's convention has n_1<...<n_k, so his t(1,{2}^n) is CKL's t({2}^N,1); the formulas agree term by term (the r=0 term, -zeta(1) replaced by log 2 = eta(1), is the log 2 term).
- https://arxiv.org/pdf/2111.07097 (OPENED, full text). v1 only (13 Nov 2021), no journal ref listed; Conjecture 4.5 verified only for N=1,2,3 (text: "This pattern seems to continue further. However, we have not figured out why yet"), notes t({2}^N,1) appears in Saha's conjecture.
- https://arxiv.org/pdf/2212.09070 (OPENED) Z. Li and L. Yan, "Generating functions of multiple t-star values" (Dec 2022). Theorem 4.3: evaluation of t*({2}^a,1,{2}^b) (star version) with b=0 giving t*({2}^a,1) = -(4/pi) t(2a+2)... plus double-sum; a closely related, independent route (star variant), also implying the non-star value by standard relations. Does not mention the conjecture explicitly (searched text for "Chavan", "Kobayashi": none).
- https://arxiv.org/pdf/2204.14183 (OPENED) Charlton-Hoffman, "Symmetry results for multiple t-values": Section 3.2 uses "the evaluations of reg t({2}^a,1,{2}^b) given in [5,6]" (Charlton's two papers) for t(1,{2}^n,1). Confirms the evaluation is regarded as established and used.
- https://arxiv.org/abs/2112.15349 (snippet) Charlton, "On the evaluation of the alternating multiple t value t({1}^a,1,{1}^b)": companion paper.
- Hoffman, "An odd variant of multiple zeta values", https://arxiv.org/abs/1612.05232 (snippet): tables to weight 7 and t(2,1) = -t(3)/2 + t(2) log 2. Did not find the general formula in his paper.
- Murakami (Math. Ann. 2021, DOI 10.1007/s00208-021-02209-3, snippet only): evaluation of t({2}^a,3,{2}^b), not of t({2}^N,1).
- Lai-Lupu-Orr https://arxiv.org/abs/2201.09262 (snippet): elementary proofs of Zagier/Murakami formulas; not the 1-case.
- Related, same era: https://arxiv.org/pdf/2403.04727 (snippet, T-values of the form (2,1,...,1)), https://arxiv.org/pdf/2301.06067 (snippet, multiple T-values and iterated log-tangent integrals), Kobayashi's Kyoto note https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/277176/1/2222-02.pdf (snippet only, has a section "Conjecture on t({2}^{n+1},1)").

### Justification
The identical statement (modulo index-order convention and eta vs -zeta notation) is proved in Charlton 2112.14613 Section 3.3 via the generating series of Thm 3.3 (hypergeometric 3F2 asymptotics, Evans-Stanton), and Charlton explicitly says it confirms the conjecture. Our generating-function proof (Gamma-function ratio, cosh(u theta) cos^{2S-1}) would be a different, elementary proof of an already-proved statement; it can be offered as an alternative short proof, with credit to Charlton (and Chavan-Kobayashi-Layja for the conjecture and the I(2N)/(2N)! form). I did not check whether the integral form t({2}^N,1) = I(2N)/(2N)! with I(n)=int theta^n cot theta is proved separately in print (it follows from the closed form since I(2N) has a known closed form; CKL verified it for N=1,2,3 and presumably the equality of the closed form with I(2N)/(2N)! is a separate elementary check that I did not locate in the literature: status of that integral identity alone is "not checked").

## Summary of labels
- A: known (Habib-Hildebrand 2606.24182, Thm 2.5, 23 Jun 2026, same technique)
- B: not found (one unverified bot-project claim that 5.9 is proved; Semantic Scholar unavailable)
- C: known (Charlton 2112.14613 Sect. 3.3, explicitly "confirms Conjecture 4.5")
