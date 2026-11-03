# Referee report: "Answers to some recent conjectures and questions in classical analysis, with computer assistance" (paper/main.pdf)

Only the compiled PDF was read from the repository. Checks were done with sympy, mpmath, exact rational arithmetic, and the arXiv PDFs of the cited papers.

## Verdict: MINOR REVISION

The mathematics I could check is correct. The labelling is mostly honest. The problems are a few typos, one inconsistency between the introduction and Section 5, one numerical inconsistency in the Padé section, and some wording that is a little stronger than the evidence.

## What I checked

**Riesz section (Thm 2.3).** I re-derived every step.
- The derivative formula of Lemma 2.4 is correct.
- The identity R_2 = cot λ / cot η is correct.
- Lemma 2.5 is correct. I checked the unimodality of G, the substitution w = q^{ρ1}, σ = 2/ρ1, the bound on χ', and the concavity of E.
- The branch argument in Prop 2.6 (s>0 persists once it starts, F continuous) is correct.
- The reduction of Conj 2.2 is correct. The acute-triangle step uses (a/c)^r ≤ (a/c)^2. The parametrisation by φ, ψ, the congruence to the isosceles case, and L ≤ ℓ giving α ≤ 2θ are all correct. I recomputed U_r(T_N), the masses (sum 1, positive) and the energy of µ_N by hand.
- Fan's Conj 5.9, Conj 5.6, Lemma 5.7 (Clark–Laugesen Thm 8) and Lemma 5.8 are quoted accurately; I compared them with the arXiv PDF. Björck Thm 12 is quoted as in Fan (at most n+1 extreme points).

**Gurland (Prop 7.1).** Correct. The Taylor series of ln Γ(a+z) has radius a, and a − |d| = 1 + min(x,y). Divergence at |d| = a is correctly argued. The Conj 7.2 constant 1/3 and the limit ϑ → −hψ'''/(6ψ'') → 1/3 are correct. Wiśniewska's Corollary 1 condition and open problems 1–3 match the paper's description.

**Finch Prop 6.1.** I re-derived A = 1/κ, a = (τ+1)/2 − c_2/γ², the existence of g_EJ, and the g̃ limit. All are correct, including the claim that the ln n terms cancel, and the formula reproduces δ_13 = −(3/4) ln 2 and Addendum III. The recursion for C'' is also consistent: E_{k+1} = f' E_k + f'' D_k^2 gives eq. (2).

**Padé certificate (Lemma 4.3).** The proof is correct, and the count of 180 odd m in [3,361] is right. I recomputed the following.
- m = 3: R = 4.644370709…, gap 1.09446104.
- m = 11: R = 15.24467959, gap 1.00798155.
- m = 101: R = 134.5370833, gap 1.0001017.

These agree with Table 2. With exact rational arithmetic I confirmed these cases:
- (k,m) = (66,5), first negative n = 38; (65,5), none up to 120.
- (44,7), n = 37; (43,7), none.
- (42,9), n = 41; (41,9), none.

The large-m runs themselves I did not re-run.

**Gregory.** With exact rationals up to n = 140 I reproduced Gr(2) = 4, Gr(3) = 11, Gr(4) = 36 and Gr(5) = 113. The vanishing coefficients (G_3 for ℓ = 2 and 3, G_5 for ℓ = 4 and 5) are as stated. Conj 6.1, the values 11, 36, 113, 346, 1030, Table 2 (n_2(ℓ) = 16, 52, 168, …) and the r(9) ≈ 5065 entry in Xu–Zhao's Table 1 are all as quoted. The r(ℓ) formula and the e^{1−γ} constant are arithmetically right, and 3.606 = e^{π/√6} is right. Table 1 ratios are right.

**Harmonic sums.** S_1 and S_2 are right. S_3 (with −4/9 ζ(2); the rendered page is correct) agrees numerically with the sum to 1e-26. S_4 = 0.21289073764960874091117… matches an independent Euler–Maclaurin sum. The top-weight formula is right for q = 1, 2, 3. The count of weight-8 and weight-9 MZV generators (d_8 = 4, d_9 = 5) is consistent with "ζ(5,3) first appears in S_7". The Chen–Nguyen quotation (Conjecture 1, "possibly fails when q = 3") and the Perhaps-sentence match the arXiv paper.

**Stirling.** The Laplace density formulas are correct. Table 4's (2n−1)δ_n column is consistent with the d_CM column for all rows I tested. 2π²/Cin(2π) = 8.0976273569. Krasniqi's Thm 1.2 (8/3 < d < 3, 32/9 < d < 4) and Thm 1.3 match the arXiv paper.

**Other citations opened.** I fetched and read the abstracts or text of these:
- Fan 2609.11186 (author Qiuling Fan; title correct).
- Xu–Zhao 2609.11072 (title and authors correct).
- Scardino 2610.39051 (diagonal case "remains open"; counterexamples c38(66,5), c37(44,7), c42(45,9) all present).
- Chen–Nguyen 2507.19502.
- Wiśniewska 2512.07028.
- Krasniqi 2610.33699.
- Habib–Hildebrand 2606.21145 (Conjectures 7.1–7.3).
- Hildebrand–Habib 2606.24182 (Thm 2.5 proves the existence of the polynomials).
- Charlton 2112.14613 (evaluation of t*,V({2}^a,1,{2}^b)).
- Zheng 2608.02265 (author H. Zheng, title as cited).

Not checked: Finch's three papers, Chavan–Kobayashi–Layja, Flajolet–Salvy, Xu–Wang 1805.08056, Lanford–Yampolsky 1108.2801, and the Fasi–Higham MIMS EPrint (not opened, so no comment on them).

## Issues

1. **(minor) Typos and notation in Section 2.**
   - Lemma 2.5's proof reads "q = w^σ, p² = (1−w)^σ". It must say q² = w^σ.
   - Lemma 2.4 states the hypothesis "0 < λ < µ"; the symbol should be η.
   - ℓ denotes the Gregory order in Section 3, a chord length in Section 2.5 and a Hurwitz-zeta index elsewhere, and ψ is the angle in Section 2 but the digamma function in Section 7. ρ is overloaded (Padé zeros, Finch's ρ, root ρ_ℓ).
   - Fix: rename, or add a notation remark at the start of each section (Section 2 has only a partial one).

2. **(major, labelling) Section 5 is inconsistent about what is proved.**
   - The introduction lists "the exact reductions in Section 5" among computer-assisted theorems.
   - Theorem 5.1 says "the expression is the output of a program", which is not a mathematical statement.
   - Section 5.3 says the closed forms come from PSLQ identification of MZV reductions, and that they are labelled numerical.
   - Intro and Theorem 5.1 say q ≤ 9; the closed forms are for q ≤ 8.
   - The justification of step 3 (stuffle regularisation with T = H_K and cancellation of powers of T) is only sketched.
   - Fix: restate Theorem 5.1 as an algorithm plus a verified numerical agreement (about 1e-62), and say which parts are exact.
   - Fix: classify the explicit S_4 … S_8 formulas as "exact MZV reduction + PSLQ-identified zeta reductions, numerically verified", not as a computer-assisted theorem.
   - Fix: make the q ranges consistent (q ≤ 9 for the MZV reductions, q ≤ 8 for the zeta closed forms).

3. **(minor) Numerical inconsistency in Section 4.3.** The text says the gap ρ_min/R is "1 + 3.5·10⁻⁵ at m ≈ 240". Table 2 gives 1.0001017 at m = 101 and 1.0000258 at m = 201. The gap scales like 1.04/m², so about 1.8·10⁻⁵ is expected at m = 240 (3.5·10⁻⁵ would correspond to m ≈ 170). Fix: correct the number or the m value.

4. **(minor) The claim that the Padé method "cannot be pushed to all odd m" is an inference.** N_0 grows like m², and the cost is polynomial but large. This is not a proof of impossibility. Fix: say "does not obviously extend, because the gap tends to 1 and the required precision and N_0 grow".

5. **(minor, honesty) Gregory abstract.** The abstract says the thresholds are computed "rigorously for orders up to 10". The tail relies on identity (6) and the monotonicity structure of [2], which are not re-proved. This is disclosed in Section 3.2, but not in the abstract or the summary list. Fix: add "relying on the integral representation of [2]". The ambiguity in the definition of Gr(ℓ) (Xu–Zhao only assert the existence of some integer) is handled correctly in the text. The agreement of the computed values 11, 36, 113, 346, 1030 with [2] supports the reading "least such integer".

6. **(minor) Finch derivation is classical.** The text admits this (résidu itératif). The proof is correct, but the novelty is the matching to Finch's conjectured constants, not new asymptotics. This is clearly stated, so no change is needed beyond not listing it among "theorems" of the paper in the abstract. Also state in 6.1 which definition of g̃ is used for general θ (the paper says it takes the displayed limit as the definition).

7. **(minor) The C''(2) derivation in 6.2 leaves the interchange of limit and differentiation unproved.** This is stated. The numerical agreement to 20 digits with Finch and to 33 digits with a second implementation is fine. The wording "independent confirmation" is acceptable. The product/sum symbols in the extraction for C'(x_0) = ∏ f'(x_k) should be checked in the typeset PDF (the text extraction was ambiguous).

8. **(minor) Stirling extrapolation (Section 8.3 and open problem 5).** The data stop at (2n−1)δ_n = 7.21 for n = 27, and the extrapolated limit 8.0975 depends on high-degree polynomial fits in 1/n. The paper hedges, but open problem 5 says "the numerical evidence suggests that the bound of [14] is attained". Fix: say "is consistent with", and note that Krasniqi's bound is a sup over m and the attainment at m = 0 is only a numerical suggestion.

9. **(minor) Triviality of Prop 7.1 and the Gurland results.** The answer to Problems 1 and 2 is a one-line consequence of the radius of convergence of the Taylor series of ln Γ. The paper says so honestly. It is a legitimate answer to the stated questions; the abstract describes it as "two of three open problems … answered", which is accurate. Keep the "we do not regard it as deep" sentence.

10. **(minor, citations)**
    - [20] and [21] are cited from [1] and not read. This is disclosed, and the statements are quoted as in [1]. I confirmed the Björck Thm 12 wording from Fan. Clark–Laugesen Thm 8 (the three-point energy formula) is also confirmed as quoted by Fan (Lemma 5.7).
    - Add the page or section for the Finch citations in Section 6.
    - [19] is a note whose author states that it was written with an AI system. Mentioning this in the text would be consistent with the paper's own disclosure.

11. **(minor) Remark 3.3.** The suggestion that "5065" in [2] is a digit transposition of 5605 is right by the formula. It is stated as belief, which is appropriate.

12. **(AI disclosure; fine, one suggestion).** The disclosure is transparent. Suggest adding one sentence saying which numerical results are not interval-certified (Section 6.3 tables, Section 8, Gr(ℓ) for ℓ ≥ 11), since the current statement only says that "proofs" were checked.

## No fatal or major mathematical errors found
The main results (Thm 2.3, Lemma 4.3, Prop 6.1, Prop 7.1) are correct as stated. Every quoted conjecture or question I compared (Fan 5.6/5.9, Xu–Zhao 6.1, Scardino, Chen–Nguyen Conjecture 1, Wiśniewska problems, Krasniqi Thm 1.2/1.3, Habib–Hildebrand Conjectures 7.1–7.3) matches the source.
