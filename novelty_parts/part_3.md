# Novelty check, part 3 (items A, B, C), done 3 Nov 2026

Tools: web search plus page fetches only. Nothing was posted or submitted anywhere.
Fetch limits: the Semantic Scholar citations API returned HTTP 429 (rate limit) on the first try for all three papers, so **citing-paper lists could not be obtained that way**. I did not retry in a loop. As a substitute I used the arXiv author listing for Finch, the arXiv abs pages, and web searches for "cited by" style hits.

## What was opened (full text read, via pdftotext of the fetched PDFs)
- Finch, arXiv:2506.07625v6 (3 Sep 2025), https://arxiv.org/pdf/2506.07625 . Fully read, including Addenda I-III and the reference list.
- Finch, arXiv:2509.24918v1 (29 Sep 2025), https://arxiv.org/pdf/2509.24918 . Section 1.5 read.
- Finch, arXiv:2503.13378v1 (17 Mar 2025), https://arxiv.org/pdf/2503.13378 . Section 3 read.
- Lanford and Yampolsky, arXiv:1108.2801, https://arxiv.org/pdf/1108.2801 . Sections 2.3 and 2.4 read.
- Milnor, Jackfest talk "Curvature and Résidu Itératif", https://www.math.stonybrook.edu/jackfest/Talks/Milnor.pdf . Read the definition.
- Finch author listing, https://arxiv.org/a/finch_s_1 . Opened.
- arXiv abs pages for 2506.07625 (versions v1..v6, no journal ref), 2509.24918 (only v1), 2503.13378 (only v1).
- Finch, arXiv:2510.25606v3 (https://arxiv.org/html/2510.25606v3), skimmed through a summariser.
- Tetration forum thread https://www.tetrationforum.org/showthread.php?tid=1199 .

Everything else listed below was seen only as a search-result snippet.

---

## ITEM A: delta constant

### Queries (all run)
1. `Finch "Half-Iterates and Delta Conjectures" Abel equation`
2. `Finch delta conjecture Abel equation Ecalle Jagy Mavecha Laohakosol proof`
3. `parabolic fixed point Fatou coordinate asymptotic expansion logarithmic term "résidu itératif" coefficient`
4. `Fatou coordinate parabolic germ x - x^{p+1} asymptotic expansion -1/(p x^p) + ((p+1)/2 - ...) log x "iterative residue" Ecalle`
5. `de Bruijn "Asymptotic Methods in Analysis" iteration x_{n+1} = x_n - x_n^2 asymptotic expansion log n/n^2 coefficient`
6. `Milnor Dynamics in one complex variable Fatou coordinate "résidu itératif" "iterative residue" invariant parabolic`
7. `Abel equation parabolic fixed point f(x)=x - a x^{p+1} + b x^{2p+1} Abel function -1/(p a x^p) + log x coefficient (p+1)/(2p) - b/a^2 Kuczma`
8. `Mavecha Laohakosol "Asymptotic expansions of iterates of some classical functions" Applied Mathematics E-Notes`
9. `"Finch" "delta" Abel equation Écalle Jagy algorithm constant -(3/4) ln 2 x(1-x^2) half-iterate proof` (extended mode)
10. `Julia equation λ(θ(x)) = θ'(x) λ(x) Jagy half iterate x - x^3 power series Abel function constant term ambiguity logarithm`
11. `"résidu itératif" Écalle parabolic germ z + z^{p+1} + a z^{2p+1} formal invariant (p+1)/2 - a`
12. Semantic Scholar citations of arXiv:2506.07625: HTTP 429, no data.

### Relevant pages
- https://arxiv.org/abs/2506.07625 (v1 9 Jun 2025 to v6 3 Sep 2025; opened). The source paper. It states the delta values as conjectures: "Formal proofs would be good to see someday." Addendum II says "δ seems to be completely determined by the parameter τ and two coefficients c1 & c2". Addendum III gives the general formula for x(1 - σx^τ - ρx^{2τ}). Opened.
- https://arxiv.org/pdf/1108.2801 (Lanford and Yampolsky, "The fixed point of the parabolic renormalization operator"; opened). Prop. 2.14 and 2.15: for F(w) = w + 1 + A/w + O(w^-2), with A = 1 - α, the Fatou coordinates have the expansion Φ(w) = w - A log w + Σ b_j w^-j. In the z coordinate: φ(z) = -1/z + A log(±z) + C + O(z). This is the classical log coefficient. I checked by hand that for f = z + z² + b z³ one gets A = 1 - b, which is the τ=1 case of (τ+1)/2 - c2/γ².
- https://www.math.stonybrook.edu/jackfest/Talks/Milnor.pdf (Milnor, résidu itératif; opened). Defines résit(f,z0) = n/2 - ind(f,z0) and notes résit(f^k) = résit(f)/k. Buff and Epstein extended the definition. The term is due to Écalle. This is the invariant (τ+1)/2 - c2/c1² in a different normalisation.
- https://www.math.univ-toulouse.fr/~buff/Exposes/GTI.pdf and https://www.ma.imperial.ac.uk/~dcheragh/PPAD/slides/Buff.pdf (snippet only): résit(g) = (νq+1)/2 - α in Buff's slides.
- https://numdam.org/articles/10.1016/j.crma.2014.11.003/ (Dudko and Sauzin, snippet only), and https://arxiv.org/abs/1307.8095 (snippet only): the Fatou coordinate has a resurgent asymptotic expansion in the Écalle framework.
- https://arxiv.org/abs/1710.01268 (Mardešić et al., snippet only): Fatou coordinate for parabolic Dulac germs.
- https://arxiv.org/abs/2210.11211 (Chéritat and Le Meur; PDF fetched). Contains Φ(w) = w - A log w + C + ... notation (checked via grep, not read in detail).
- https://arxiv.org/abs/2411.01591 (Finch, "What do sin(x) and arcsinh(x) have in common?"; snippet). Quotes de Bruijn's expansion x_n ~ 1/n - ln n/n² - C/n² ...
- Not opened (no free text): de Bruijn, Asymptotic Methods in Analysis (1958); Kuczma-Choczewski-Ger, Iterative Functional Equations (1990), pp. 346-347 and 351-352 (cited by Finch as ref [6] for the EJ algorithm); Écalle, J. Math. Pures Appl. 54 (1975); Mavecha and Laohakosol (2013); Bencherif and Robin (1994); Ionascu and Stanica, Acta Math. Univ. Comenianae 73 (2004) 75-87 (https://emis.univie.ac.at/journals/AMUC/_vol-73/_no_1/_stanica/stanica.pdf ; snippet only; it treats a_{n+1} = a_n - a a_n^α + b a_n^β expansions with log terms).

### Check of the claimed formula against Finch's own statements
Claimed: δ = -(a/τ) ln(-τγ), a = (τ+1)/2 - c2/γ². I verified by hand that it reproduces every conjecture in the v6 text:
- θ13 = x - x³: τ=2, γ=-1, c2=0, a=3/2, giving -(3/4) ln 2. Matches.
- x(1 - x^k): giving -((k+1)/(2k)) ln k. Matches.
- θ16 = x - 3x² + 3x³: τ=1, γ=-3, c2=3, a = 1 - 3/9 = 2/3, giving -(2/3) ln 3. Matches.
- θ17 = x(1 - 6x + 16x²): γ=-6, c2=16, a = 1 - 16/36 = 5/9, giving -(5/9) ln 6. Matches.
- Addendum III, x(1 - σx^τ - ρx^{2τ}): γ=-σ, c2=-ρ, a = (τ+1)/2 + ρ/σ², giving ((τ+1)/(2τ) + ρ/(τσ²)) ln(1/(τσ)). Matches exactly.
- x - x²/2 + x³/3 (with ln(1+x)): -(1/3) ln 2. Matches.
(Caveat: I did not recompute the numerics; this only compares the algebra of the claimed formula against Finch's stated conjectures.)

Also note: the ML expansions Finch prints (e.g. "(k+1)/(2k²) · ln n / n^((k+1)/k)") already contain the log coefficient (k+1)/2 as the ln-n term, which is exactly de Bruijn-type orbit inversion. So the ingredient behind the claimed proof is in Finch's own formulas.

### Finding on prior proofs
No source found (arXiv, web search, Finch's later papers) that proves or even revisits the delta conjectures. Finch's later arXiv paper 2510.25606v3 (Oct to Dec 2025) cites 2506.07625 as ref [4] but, per the summary, mentions neither a delta proof nor a residual-iterative invariant. The arXiv listing of Finch shows no later paper (to Oct 2026 IDs, titles seen) on Abel equations; the later titles are on other topics. Note v1 and v2 of 2506.07625 are different papers (half-iterates of x(1+x), sin x, exp(x/e); and of x exp(x), x+1/x, arcsinh x) that share the arXiv number.

### Label for A
- The log coefficient (τ+1)/2 - c2/c1² (the résidu itératif up to normalisation) in the Fatou-coordinate expansion: **known/classical** (Écalle; Lanford-Yampolsky Prop. 2.14-2.15; Milnor/Buff-Epstein).
- delta as a statement relating EJ's zero-constant normalisation to ML's limit normalisation: **probably known / easy corollary** of classical expansions plus asymptotic inversion (de Bruijn; Ionascu-Stanica method). I found no source that states it or proves Finch's conjectures, so for the specific claim "proof of Finch's delta conjectures" the label is **not found** in the literature, but the content should be presented as a short corollary, crediting Écalle, de Bruijn, Mavecha-Laohakosol, Lanford-Yampolsky for the ingredients.
- Honest caution: whether EJ really returns the series with zero constant term and exactly this log term depends on the exact EJ definition (Finch refs [7,8]); the proof should state that normalisation explicitly. Also Finch v3 had a coding bug (his Section 1 "Clarification"), so earlier delta values (e.g. 0.1940811) were wrong.

---

## ITEM B: tetration half-iterates T(4/3,1/2), T(5/4,1/2), T(6/5,1/2)

### Queries
1. `Finch "Exercises in Iterational Asymptotics IV" tetration half-iterate T(4/3,1/2)`
2. `tetration base 4/3 half iterate 1.2058374 regular iteration b<e^{1/e}`
3. `half-exponential "b^x" regular iteration attracting fixed point Koenigs fractional tetration base less than e^(1/e) values table`
4. `tetration forum "base 4/3" OR "b=4/3" OR "base 1.3333" tetration regular iteration half-iterate value`
5. `Paulsen "Tetration for complex bases" Advances in Computational Mathematics 2019 base less than e^{1/e}`
6. `Kouznetsov Trappmann "Portrait of the four regular super-exponentials to base sqrt(2)" Mathematics of Computation`
7. `Finch "Exercises in Iterational Asymptotics V" OR "VI" arXiv 2026`
8. `Finch arXiv 2026 iterates Abel's equation half-iterate tetration superexponential 4/3 5/4 6/5`
9. `Finch "Fractional Iterates and Oscillatory Convergence" corrigendum addendum`
10. Semantic Scholar citations of 2509.24918: HTTP 429.

### Relevant pages
- https://arxiv.org/abs/2509.24918 (opened; only v1 exists, 29 Sep 2025). Sec. 1.5 text read: "T(e^{1/e},1/2)=1.2571...; using Kneser's construction, T(e,1/2)=1.6463... but using Szekeres' construction T(e,1/2)=1.6451.... Other examples via Kneser include T(3/2,1/2)=1.2808..., T(2,1/2)=1.4587... and T(10,1/2)=2.4770... [13,14]. It would be good to see the values of T(4/3,1/2), T(5/4,1/2) and T(6/5,1/2) someday." The paper's own computed value for base √2: f^[1/2](1) = 1.24362162766852180429509898360940293168819835661552... (via Paulsen's method), i.e. T(√2,1/2)=1.2436....
- I recomputed with a quick mpmath script (Koenigs/Schröder at the attracting fixed point, base b, start 1): √2 gives 1.2436216276500..., agreeing with Finch's 1.24362162766852 to about 10 digits (my quick script is less accurate than 40 digits); b=4/3 gives 1.2058374340430956 (agrees with the claimed 1.2058374340430955949 to the digits shown). I did not rerun 5/4 or 6/5 (my findroot failed there; that is a limitation of my quick script, not evidence against the claim). So the convention (regular iteration at the attracting fixed point) is the same as Finch's √2 value.
- https://www.ams.org/mcom/2010-79-271/S0025-5718-10-02342-2/ (Kouznetsov and Trappmann; snippet only): four regular super-exponentials for base √2; notes there are two regular choices at each fixed point, so "regular" must specify which fixed point. For b < e^{1/e} the one at the attracting (lower) fixed point is the standard real-analytic one, but it is not the only "regular" one, so the convention must be stated.
- https://arch.astate.edu/scm-mathfac/8 and https://link.springer.com/10.1007/s10444-018-9615-7 (Paulsen, "Tetration for complex bases"; snippets): gives iteration methods for bases inside and outside the Shell-Thron region.
- https://tetrationforum.org/showthread.php?tid=355 and https://www.tetrationforum.org/showthread.php?tid=1199 (opened tid=1199): informal; says "Nixon's approach" covers real bases in (1, e^{1/e}), unpublished. No numeric values for base 4/3.
- https://arxiv.org/abs/1105.4735 (Kouznetsov-Trappmann, base exp(1/e); snippet) and https://arxiv.org/abs/2509.24049 (snippet; "Analytical and numerical approaches for finding functional iterates and roots"): not checked in full; no 4/3 hit in snippets.
- Tetration forum has a thread "AIS iteration series: half-iterate" (https://tetrationforum.org/showthread.php?tid=760) with values for base 1.3 modified exponentials, not 4/3 tetration (snippet only).

No page found giving T(4/3,1/2), T(5/4,1/2) or T(6/5,1/2). Not in the later Finch arXiv papers I could see (2510.25606v3 summary mentions 4/3 only in unrelated Lucas-ratio examples).
Caveat: web search cannot do numeric full-text search of forum posts, so a forum post with these digits could exist unseen.

### Label for B
**Not found.** (Values are straightforward to compute by the standard method, so "easy but unrecorded".) Convention note for the write-up: state explicitly "regular iteration at the attracting fixed point (Koenigs/Schröder), real-analytic, starting from T(b,0)=1". This is canonical for b<e^{1/e}, but Kouznetsov-Trappmann show that other "regular" super-exponentials (at the repelling fixed point) exist, and Finch himself computed such curves (F_{4,3}, F_{4,5}) for √2. Credit: Koenigs, Szekeres, Kouznetsov-Trappmann, Paulsen; Finch for the question.

---

## ITEM C: second derivative C''(2)

### Queries
1. `Finch "Exercises in Iterational Asymptotics III" x_{n+1} = x_n + 1 + 1/x_n^2 second derivative`
2. `recurrence x_{n+1} = x_n + 1 + 1/x_n^2 limit x_n - n derivative of limit function with respect to initial value`
3. `Ionascu Stanica "Effective asymptotics for some nonlinear recurrences and almost doubly-exponential sequences"`
4. `Finch "Exercises in Iterational Asymptotics V" OR "VI"` (shared with B)
5. `Finch arXiv 2026 iterates ...` (shared with B)
6. `Finch "Fractional Iterates and Oscillatory Convergence"` (shared with B)
7. Semantic Scholar citations of 2503.13378: HTTP 429.
8. (Also the de Bruijn search under item A.)

### Relevant pages
- https://arxiv.org/abs/2503.13378 (opened; only v1, 17 Mar 2025). Section 3 ("Dixième exercice"): C(x0) = x0 + Σ 1/x_n²; C'(x0) = Π(1 - 2/x_n³) = 0.66156132404868...; Finch's series C'' = C' Σ (1-2/x_n³)^-1 6/x_n⁴ = 0.3909...(?) (with a "uniformity" supposition, flagged as apparently wrong); finite-difference value C''(2) ≈ 0.37462642198301734111; "An independent confirmation of the 0.3746 estimate remains open." Cited background: Ionascu and Stanica (2004) (ref [11]), Little-Teo-van Brunt, An Introduction to Infinite Products (ref [12]), de Bruijn, Mavecha-Laohakosol.
- https://emis.univie.ac.at/journals/AMUC/_vol-73/_no_1/_stanica/stanica.pdf (snippet only): Ionascu-Stanica, asymptotics of a_{n+1} = f(a_n); no derivatives of the limit function were seen in the snippet.
- Author listing https://arxiv.org/a/finch_s_1 shows no later Finch paper revisiting this recurrence.

### Independent check I ran
The claimed series is just the chain rule: C'(x0) = Π f'(x_k) with f'(x) = 1 - 2/x³ and x_j' = D_j = Π_{k<j} f'(x_k), so log C' has derivative Σ f''(x_j) D_j / f'(x_j) with f'' = 6/x⁴. Finch's printed series omits the factor D_j, which explains 0.3909 vs 0.3746. A quick double-sum in mpmath, truncated at 2*10^5 terms, gave C'(2) = 0.6615613240652 and C''(2) = 0.3746264219924, which agrees with Finch's 0.37462642198301734 to about 10 digits (the discrepancy is from the truncated tail, ~1/N). So the claim holds numerically.

No source found where anyone else computes C''(2), and no literature on derivatives of this limit function.

### Label for C
**Not found** in the literature as a published statement. But the content is an elementary chain-rule differentiation of the product formula for C', so it should be presented as an easy derivation, not a new theorem ("probably known" in the sense of being trivial once seen). It does settle Finch's explicitly stated open confirmation item for C''(2). Credit: Finch for the question and the finite-difference value; the infinite-product formula for C' is in Finch's paper.

---

## Summary of labels
- A: classical ingredients **known** (résidu itératif / Fatou-coordinate log term); delta formula **probably known (easy corollary)**; proof of Finch's delta conjectures **not found** elsewhere.
- B: **not found** (three values), with the convention caveat.
- C: **not found** (but elementary chain-rule corollary).
