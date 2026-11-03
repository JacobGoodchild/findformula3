# findformula3 — calculus night (2 November 2026)

**AI disclosure.** All research in this repository was carried out by Claude (Anthropic), via Claude Code, under the direction of Jacob Goodchild (who set the brief and the rules and was asleep while it ran).
No result has been posted, e-mailed or submitted anywhere; everything here is a draft for him to judge. Computations ran only on the session's own machine.

## What this is
In findformula (lattice models) and findformula2 (Kerr black holes) the targets were things nobody had asked about. This repo does the opposite: every target is a **calculus question that someone wrote down in a recent paper**
(an open problem, a conjecture, an "it would be good to see ..." remark), checked by opening the paper. Each result is labelled PROVED / VERIFIED / PARTIAL (see `formulas.txt`), with code, logs and a proof write-up in `results/<name>/`,
and re-checkable with `python3 verify_all.py`.

## Results (best first; details in `formulas.txt`, `MORNING_SUMMARY.md`)
| # | Question (who asked) | Result | Label |
|---|---|---|---|
| 3 | Habib–Hildebrand, arXiv:2606.21145, Conjecture 7.1: polynomial coefficients p_k exist for u''u−u'^2=e^{-x}P(u)−1 | true; proof via a residue/zero-of-u argument | **PROVED** (7.2, positivity: reduced, not proved) |
| 4 | Finch, arXiv:2506.07625: exact value of the constant δ between two Abel-function normalisations (≈17 conjectured cases) | one formula δ = −(a/τ)ln(−τγ) covers all of them | **PROVED** |
| 5 | Finch, arXiv:2503.00579: A(x/(1+x))=B(x)+1 and I(x/(1+x))=J(x)+1 | proved by a Möbius conjugacy | **PROVED** |
| 1 | Chen–Nguyen, arXiv:2507.19502 / Furdui–Sîntămărian: closed form of Σ H_k…H_{k+q}/(k…(k+q)) | q=4…8 closed forms; exact algorithm for all q; top-weight law | **PROVED** (q≤5) / VERIFIED (6–8) |
| 6 | Xu–Zhao, arXiv:2609.11072, Conjecture 6.1 on Gregory-coefficient sign thresholds | conjecture false; Gr(8..13) computed; true growth ~ exp(π cot(π/ℓ)) | **PROVED** (ℓ≤10) / VERIFIED |
| 7 | Scardino, arXiv:2610.39051: Fasi–Higham positivity, diagonal Padé case | proved for each odd m ≤ M; failure threshold k*(m)=2m+12..14 | **PROVED** per m / VERIFIED law |
| 8 | Krasniqi, arXiv:2610.33699: exact degrees d_CM(R_2), d_CM(−R_2') | 2.8667042552, 3.7984354776 (+ table to n=9) | VERIFIED |
| 9 | Finch, arXiv:2503.13378: independent confirmation of C''(2) | exact series; C''(2)=0.37462642198301734111… | formula PROVED / value VERIFIED |
| 10 | Finch, arXiv:2509.24918: T(4/3,1/2), T(5/4,1/2), T(6/5,1/2) | 40-digit values | VERIFIED |
| 2 | Wiśniewska, arXiv:2512.07028, open problems 1–3 on Gurland's ratio | 1,2 proved (Taylor series converges for all x,y>0); 3: sharp constant 1/3, conjectured inequality | **PROVED** / PARTIAL |
| 11 | arXiv:2609.11186, Conjectures 5.9 and 5.6 (Riesz energy of 3-point sets) | both true; proved via unimodality + entropy comparison, finished with the paper's Lemma 5.8 | **PROVED** |
| 12 | arXiv:2111.07097, Conjecture 4.5: t({2}^N,1)=I(2N)/(2N)! | proved via a Gamma-product / Beta-integral generating function | **PROVED** |
| 13 | Samart (arXiv:2608.02265): why n_4(81) is not 40 M_7 | the real part of the analytic continuation equals 40 L'(g_7,0) to 25+ digits; true Mahler measure 4.16553(5) (no closed form found) | VERIFIED |
| 14 | Gasull (arXiv:2012.02524): chance a random degree-4 polynomial is stable | p_4 = 0.0092838447242981189571 via a 2-D integral (asymptotics question NOT answered) | PARTIAL (numerical) |

## Repo map
`CLAUDE.md` brief + progress log · `TARGETS.md` scouting list with status · `NOTES.md` dead ends and leads · `formulas.txt` recorded results · `results/*/` code and write-ups · `verify_all.py` re-runs headline checks · `MORNING_SUMMARY.md` plain-English summary and draft e-mails.
