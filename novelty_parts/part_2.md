# Novelty check, part 2 (3 Nov 2026)

Method: WebSearch + WebFetch only. Semantic Scholar citation API returned HTTP 429 for both papers (one attempt each, not retried), so citing papers could NOT be listed that way; citing-paper checks below rely on searches only.

## ITEM A: harmonic products S_q

### Queries run
1. Furdui Sintamarian series products of consecutive harmonic numbers H_k H_{k+1}...H_{k+q} / k(k+1)...(k+q) zeta closed form
2. Chen Nguyen "series involving a product of four consecutive harmonic numbers" arXiv 2507.19502
3. "harmonic numbers" series H_k ... H_{k+4} / k(k+1)...(k+4) closed form zeta(5,3)
4. Euler sums products of harmonic numbers reduce to multiple zeta values algorithm weight general theorem
5. math.stackexchange sum H_k H_{k+1} H_{k+2}/(k(k+1)(k+2)) closed form
6. Furdui Sintamarian Gazeta Matematica 2023 consecutive harmonic conjecture zeta(2)..zeta(q+2)
7. "consecutive harmonic numbers" series zeta values Furdui Valean Chen Nguyen citation (extended)
8. Flajolet Salvy "Euler sums and contour integral representations" products of harmonic numbers reduction MZV
9. Wang Lyu "Euler sums and Stirling sums" quartic Au-Yeung zeta(5,3)
10. Integers 26A 2026 "product of four consecutive harmonic numbers" follow-up general q conjecture resolved
11. Semantic Scholar citations API for arXiv:2507.19502 -> 429 error.

### Opened (full/partial text read)
- https://arxiv.org/abs/2507.19502 (abstract page): only v1 (10 Jul 2025), 10 pages, math.NT. No later version.
- https://arxiv.org/html/2507.19502 (full text): Theorem 1 gives S_3 = -4/9 zeta(2) - 1/6 zeta(2)zeta(3) - 7/24 zeta(3) + 191/144 zeta(4) + 1/2 zeta(5). Conjecture 1 (Furdui-Sintamarian) as stated in the task; authors say it holds iff zeta(2)zeta(3) in Q-span{zeta(2..5)}, i.e. "possibly fails" at q=3. General q is left open ("Perhaps we can learn more by computing the closed form for ... q in N"). Cites Flajolet-Salvy, Xu-Cai (JMAA 2018), Xu-Yan-Shi (JNT 2016), Wang-Lyu (JNT 2018, "Euler sums and Stirling sums"; notes quartic Au-Yeung / S_{2,6} not reducible to zeta products), Bowman-Bradley, Hoffman, Zhao's book.
- Seen only in search snippets: published as Integers 26A (2026), #A6, https://math.colgate.edu/~integers/aap6/aap6.pdf (PDF fetched but unreadable binary, so I could not check whether the published version adds anything about q>=4).
- Other pages seen only in snippets (not opened): Xu-Wang "Explicit formulas of Euler sums via MZVs" https://arxiv.org/abs/1805.08056 ; Xu-Cai https://arxiv.org/pdf/1609.04924 ; Flajolet-Salvy https://projecteuclid.org/euclid.em/1047674270 ; Sun survey https://arxiv.org/pdf/2210.07238 ; Nguyen https://arxiv.org/pdf/2304.11614 ; Wang-Lyu quartic (cited via 2507.19502 only).

### Findings
- No source found containing S_4 (or any S_q, q>=4) in closed form. No arXiv/MSE/MO hit for the q=4 product of five consecutive harmonic numbers. No paper found citing Chen-Nguyen that addresses the conjecture (but citation API failed, so this is weaker than intended). Chen-Nguyen's own text says general q is open.
- Prior art that makes the ALGORITHM (not the values) essentially known in principle: any sum of products of harmonic numbers H_{k+j} times a rational function with poles at integers can be expanded (partial fractions, shifting H_{k+j} = H_k + finite sums) into Euler sums / multiple harmonic sums; the stuffle product and the standard fact that Euler sums of weight w are Q-combinations of (alternating) MZVs of weight w (Flajolet-Salvy 1998; Xu-Wang arXiv:1805.08056; Xu-Cai arXiv:1609.04924; Borwein-Girgensohn "Evaluation of triple Euler sums"; Bowman-Bradley; Zhao book) gives a reduction to MZVs. The structural claim "S_q is a Q-combination of MZVs of weight <= q+2" is therefore not surprising; the explicit q=4..8 values and the algorithm applied to this family appear new.
- The weight reductions are consistent with the literature: weight <=7 and 9 are all products of zeta values; weight 8 needs zeta(5,3) (Wang-Lyu; Xu-Wang), matching the claim that zeta(5,3) first appears for q>=7 (weight 9 total for q=7 ... note: S_q mixes weights up to q+2, so q=6 reaches weight 8; the claimed appearance of zeta(5,3) at q>=7 should be double-checked by the caller against own data; this is not something I could verify from sources).
- Top-weight law (zeta(q+2)+zeta(q+1,1))/q! = (1/q!) sum H_n/n^{q+1}: no source found stating it.

### Label: NOT FOUND (closed forms q>=4, top-weight law); algorithm is "probably known" in principle (general Euler-sum-to-MZV reduction). Honest wording: "closed forms for q=4..8 not found in the literature; the reduction to MZVs follows from standard theory (Flajolet-Salvy, Xu-Wang)". Credit: Furdui & Sintamarian (conjecture, q=1,2), Chen & Nguyen (q=3, arXiv:2507.19502), Flajolet-Salvy, Xu-Wang, Wang-Lyu. Note result bears on the conjecture: since S_3 contains zeta(2)zeta(3), the conjecture holds iff zeta(2)zeta(3) is a Q-combination of zeta(2..5), which is open (not refuted); S_4 etc. likewise cannot decide it.

## ITEM B: Gregory coefficients Gr(l)

### Queries run
1. Gregory coefficients higher order (x/log(1+x))^l sign alternation threshold Gr(l) Xu Zhao Cauchy numbers conjecture 3^l
2. Blagouchine Gregory coefficients higher order asymptotics Nörlund (x/log(1+x))^l sign eventually alternating
3. Rational Approximations for Reciprocals of Multiple Zeta Values and Trivariate Cauchy Numbers Xu Zhao
4. Nörlund polynomials B_n^{(n)} asymptotics higher order Gregory G_n^{(k)} Stirling Blagouchine Coppo
5. "Gregory coefficients" "higher order" eventually alternating G_n^{(k)} exp(pi cot(pi/k)) OR "largest real root"
6. oeis 11, 36, 113, 346, 1030, 2995, 8580 (web search)
7. OEIS direct: https://oeis.org/search?q=11,36,113,346,1030,2995,8580,24303&fmt=short -> "terms do not match anything in the table" (opened).
8. Semantic Scholar citations API for arXiv:2609.11072 -> 429 error.

### Opened
- https://arxiv.org/abs/2609.11072: Xu & Zhao, only v1 (10 Sep 2026), 24 pages; no later version listed. Abstract: eventual alternation of each fixed-order sequence proved; trivariate Cauchy numbers; conjecture of eventual positivity in general.
- https://arxiv.org/html/2609.11072 (read first 100000 of 105996 chars): Conjecture 6.1 reads "For all l>=5 we have 0.47*3^l < Gr(l) < 0.477*3^l". Values Gr(3)=11, Gr(4)=36, Gr(5)=113, Gr(6)=346, Gr(7)=1030 stated as exact from computer search. Lower bound at l=5: 0.47*243 = 114.21 > 113, so the conjecture fails on the paper's own value (confirmed by me from the text). Remark: largest real root r=exp(pi rho_l) of H_l(log z/pi) "seems to increase by roughly tripling", authors wonder why; upper bound A = exp(pi sqrt((l-1)(l-2)/6)) (growth ~3.606 per step). References cited on this topic: Schröder, Blagouchine (arXiv:1408.3902 and a Bernoulli-second-kind note), Nörlund pp.150-151 (via Howard), Candelpergher-Coppo, Carlitz, Comtet, Ishii-Shinohara. No separate asymptotic theory for higher-order coefficients is given.
- OEIS exact-number search: no match for 11,36,113,346,1030,2995,8580,24303. The web-search snippets showed only coincidental partial overlaps (A392076: 11,37,113,...; A018167 contains 1030) which are not matches.
- Seen in snippets only (not opened): Blagouchine https://arxiv.org/pdf/1408.3902 (order-1 asymptotics |G_n| ~ 1/(n ln^2 n), Steffensen/Van Veen/Davis); Blagouchine "Three notes..." https://arxiv.org/pdf/1606.02044 (Nörlund B_n^{(n)}(x) asymptotics; (-1)^n B_n^{(n)}(a) n^a/n! ~ sum (log n)^{-(i+1)} d^i/da^i 1/Gamma(1-a)); Coppo-Blagouchine definition G_n^{(k)} = (1/n!) sum S1(n,m)/(m+k) (https://hal.univ-cotedazur.fr/hal-01499011/document); 2312.14475 "Asymptotic coefficients of multiple zeta functions at the origin and generalized Gregory coefficients" (https://arxiv.org/pdf/2312.14475, different generalisation, not checked); 2604.01578 Gregory polynomials (not checked).

### Findings
- Conjecture 6.1 refutation at l=5 is verifiable directly from the paper's text; no erratum or later version exists (only v1). No citing paper found (citation API failed).
- No source found on the threshold Gr(l) beyond Xu-Zhao, nor on exp(pi cot(pi/l)) growth, nor Gr(8..14). The relevant classical background for a theoretical explanation is Nörlund's asymptotics of B_n^{(n-l)} (generalised Bernoulli polynomials of the second kind), where the complex saddle/zero structure of 1/Gamma-type factors determines when sign alternation sets in; I found no paper doing this for the threshold.
- Gr values not in OEIS.

### Label: NOT FOUND (new exact values Gr(8..14), growth law, and refutation of Conj 6.1). The l=5 inconsistency is a simple arithmetic observation about the paper's own numbers ("known" only in the trivial sense that it follows from their stated data). Caveat: absence is based on a handful of searches and an unreadable tail (last ~6k chars) of the Xu-Zhao html.
Credit: Xu & Zhao (definition of Gr, Gr(3..7), Conj 6.1), Blagouchine / Coppo-Blagouchine / Nörlund (background on G_n^{(k)} and asymptotics).
