# NOVELTY.md — Phase B literature checks (3 Nov 2026)

Method: four search agents (one per group of results) each ran 5-11 distinct web queries per item (queries and every URL are listed in `novelty_parts/part_1.md` ... `part_4.md`), looked at the source papers' follow-ups, the authors' later work, OEIS (for the Gr(l) integers) and classical references. **Limits:** the Semantic Scholar citation API returned HTTP 429 for most papers, so "who cites paper X" was reconstructed from web searches only; behind-paywall papers could not be read. "Not found" means only that we could not find it.
Links marked (**opened**) were opened and read by me (the lead session); links marked (agent) were opened by a search agent and not re-checked by me; links marked (snippet) were seen only in search snippets.

## Summary table

| # | Result | Novelty label | Decision |
|---|---|---|---|
| 1 | Habib–Hildebrand Conj. 7.1 true (Painlevé-type ODE) | **KNOWN** | dropped (same authors proved it 4 days later) |
| 2 | Finch A(x/(1+x)) = B(x)+1, I(x/(1+x)) = J(x)+1 | **KNOWN** | dropped (Finch's own Corrigendum) |
| 3 | Finch delta conjectures: delta = -(a/tau) ln(-tau gamma) | proof of the conjectures **not found**; formula **probably known** (easy corollary of the classical Fatou-coordinate expansion) | short proposition, credited |
| 4 | Chavan–Kobayashi–Layja Conj. 4.5 (t({2}^N,1)) | **KNOWN** | dropped (Charlton 2021/2025); at most an alternative-proof remark |
| 5 | Fan Conj. 5.9 and 5.6 (Riesz capacity, 3 points on a circle) | **not found** | main result |
| 6 | Xu–Zhao Conj. 6.1 false; Gr(8..14); growth law | not found (conjecture refutation is immediate from the authors' own Gr(5)=113); OEIS: no match | included |
| 7 | Padé diagonal positivity for odd 3 <= m <= 361; k*(m) law | not found | included (computer-assisted) |
| 8 | Chen–Nguyen/F–S harmonic series: S_4..S_8 closed forms; top-weight law | closed forms **not found**; the reduction method is standard theory | included (computer-assisted / numerical) |
| 9 | Krasniqi CM degrees d_CM(R_2), d_CM(-R_2') | not found | included as numerics |
| 10 | Gurland problems 1,2 | **probably known** (elementary: radius of convergence of the Taylor series of ln Gamma) | short proposition; problem 3 partial |
| 11 | Finch C''(2) series and value | not found in literature; elementary | short note |
| 12 | Finch T(4/3,1/2), T(5/4,1/2), T(6/5,1/2) | not found | numerical table |
| 13 | Samart n_4(81) explanation | **KNOWN** | dropped (Zheng, arXiv:2608.02265 contains it) |
| 14 | Gasull p_4 | high-precision value not found; **does not answer Problem 21** | dropped |
| 15 | Habib–Hildebrand Conj. 7.2 (nonnegativity): reduction + exact checks | no proof found in the literature | partial remark in open-problems section |

## Details and links

**1. Painlevé Conjecture 7.1 — KNOWN.** R. Hildebrand and R. Habib, "Sufficient conditions for the existence of exponential-polynomial expansions for solutions of certain differential equations", arXiv:2606.24182, submitted 23 Jun 2026 (**opened**): Theorem 2.5: "Let deg P = d >= 2, pi_0 = 0, pi_1 = pi_2. Then for all k >= 1 there exist polynomials p_k(x;P) with degree deg p_k = (d-2)k+1, such that with p_0(x) = x and for every c in C the formal series (4) is a solution of ODE (1)." The abstract says the necessary conditions of [2606.21145] "are also sufficient". Our argument (obstruction at order s vanishes via expansion at the zero of the truncated series) is essentially the same as theirs. Conjecture 7.2 (nonnegativity of the coefficients) and convergence (7.3) are not addressed there as far as the agent's reading of the full text goes (agent). Related: A. V. Kitaev, Zap. Nauchn. Sem. POMI 548 (2025) 101-152, and Kitaev–Vartanian, arXiv:2503.11912 (cited in 2606.21145; not read).

**2. Finch A/B and I/J — KNOWN.** S. Finch, arXiv:2503.00579 (v3), Section 5 "Corrigendum" (**opened**): "The interrelation between A and B turns out to be frivolous", and a derivation that one recurrence is a reparametrisation of the other, likewise for I and J.

**3. Finch delta conjectures.** Finch's v6 (arXiv:2506.07625, **opened**) states them as conjectures ("formal proofs would be good to see someday") and no proof was found elsewhere; his later paper arXiv:2510.25606 (agent) does not address them. The logarithmic coefficient (tau+1)/2 - c_2/c_1^2 of the Fatou coordinate is classical (Ecalle's "résidu itératif"; e.g. Lanford–Yampolsky, arXiv:1108.2801, Prop. 2.14-2.15 (agent); Milnor's Jackfest talk, https://www.math.stonybrook.edu/jackfest/Talks/Milnor.pdf (agent, snippet)). Label: the delta formula is an easy corollary of known expansions plus the definitions of the two algorithms; we present it as a short proposition with credit to these sources. Caveat from the agent: Finch's v3 had a coding bug, so older printed values differ; we use v6.

**4. t-values — KNOWN.** S. Charlton, "On motivic multiple t values, Saha's basis conjecture, and generators of alternating MZV's", arXiv:2112.14613 (Math. Ann. 392 (2025) per the agent; **opened** arXiv version v1, 29 Dec 2021), Section 3.3 "Evaluation of t(1,{2}^n)": "In order to answer a question posed in [6], we turn to the special case of t(1,{2}^n) ... This confirms Conjecture 4.5 on the evaluation of t(1,{2}^n) stated in [6] (be aware, the opposite MZV/MtV convention is used therein)" ([6] = arXiv:2111.07097). Related: Li–Yan, arXiv:2212.09070, Thm 4.3 (star version) (agent); Charlton–Hoffman, arXiv:2204.14183 (agent). Our generating-function proof is an independent short proof of the same formula.

**5. Fan Conjectures 5.9/5.6 — not found.** Agent searched Clark–Laugesen (arXiv:2410.14809, 2603.04649), Fan's other papers, tori/distance-energy papers, arXiv:2610.04811, and found no proof. Fan's paper itself (**opened**) proves only the symmetric case (Lemma 5.8) and calls its attempt at 5.9 "unsuccessful". **Caveat:** a bot-posted GitHub issue (https://github.com/the-omega-institute/trureturing/issues/16136, 13 Oct 2026, snippet/agent only) says a "public project exclusion page records 5.9 as proved" in an AI/Lean project with no reviewed proof; I did not verify it and treat it as an unverified claim (it also says it is not a proof of 5.6). Should be re-checked by a human before publication.

**6. Gregory.** Xu–Zhao v1 only (no later version seen). OEIS direct search for 11,36,113,346,1030,2995,8580,24303: no match (agent; the agent's snippet overlaps A392076, A018167 are coincidental partial matches). No source on the thresholds Gr(l), the exp(pi cot(pi/l)) growth or Gr(8..14) was found. Background to credit: Nörlund, Blagouchine (arXiv:1606.02044 (snippet)), Coppo–Blagouchine, Comtet, Carlitz, Schröder (cited by Xu–Zhao).

**7. Padé.** Scardino v1 only (**opened**). No source settling the diagonal case or stating k*(m) found. Classical zero-distribution literature (Saff–Varga, Driver–Temme, Stahl; agent, snippets) concerns zeros not coefficient signs.

**8. Harmonic products.** Chen–Nguyen (**opened**; published in Integers 26A (2026) #A6 per the agent) give only S_3; no source with S_q, q >= 4 or the top-weight law. The reduction of products of harmonic numbers over rational weights to Euler sums/MZVs is standard: Flajolet–Salvy (1998), Xu–Wang arXiv:1805.08056, Xu–Cai arXiv:1609.04924, Wang–Lyu (agent, titles not verified by me). Our contribution is the explicit values and an algorithmic bookkeeping, not the method.

**9. Krasniqi numerics.** Not found (agent: Bouali arXiv:2202.01801, Qi–Mahmoud arXiv:1912.07989 only give bounds/integer degrees).

**10. Gurland.** Wiśniewska's Theorem 1 (**opened**) gives the expansion with sufficient condition Q < 1; she does not mention the radius of convergence of the Taylor series of ln Gamma. The statement is a direct consequence of DLMF 25.11 (Hurwitz zeta, Taylor series of psi) (agent); cite as standard.

**11-12. Finch C''(2), T(b,1/2).** Not found in later Finch papers or the tetration literature (agent); regular iteration convention per Finch (checked consistent for sqrt 2). Kouznetsov–Trappmann show other 'regular' super-exponentials exist at repelling fixed points, so the convention must be stated.

**13. Samart.** H. Zheng, arXiv:2608.02265 (**opened**): n_4(81) = 4.1655349907533676508(5), 40 M_7 = 4.10686431115608044841826..., difference +0.0586706795972872; Theorem 3.4: EK_4(tau_2) = 40 M_7.

**14. Gasull p_4.** Reference [34] of Gasull's paper is Cima–Gasull–Mañosa, "Stability index of linear random dynamical systems", arXiv:1904.05725 (agent), which has Monte Carlo r_4 ~ 0.00925 only; Litvin–Boreisha (Cybern. Syst. Anal. 1991, paywalled) may contain exact small-n results and could not be read.
