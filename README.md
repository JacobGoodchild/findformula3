# findformula3 — answers to recent conjectures and questions in classical analysis (calculus night, 2 November 2026; verified and written up 3 November 2026)

**AI disclosure.** This work was carried out with extensive use of an AI system, Claude (Anthropic), via the Claude Code software, under the direction of Jacob Goodchild. The AI system chose the problems from the recent literature, carried out the derivations, proofs and computations, searched and checked the literature, and wrote the manuscript. Proofs were checked by independent AI referee passes and by computer algebra and interval arithmetic, but have not been checked by a human expert or peer reviewed. Novelty assessments are based on literature searches and may be incomplete. Jacob Goodchild directed the work and is responsible for its publication.
Nothing here has been posted, e-mailed or submitted anywhere. All computations ran on the session's own machine.

## What this is
In findformula (lattice models) and findformula2 (Kerr black holes) the targets were things nobody had asked about. This repository does the opposite: every target is a **question or conjecture that someone wrote down in a recent paper**, checked by opening the paper. A first overnight session produced 13 results; a second session (3 November) **checked every citation, searched the literature again for each result, had each proof read by independent referee agents, recomputed the numerical results with fresh code, dropped what was already known, and wrote one preprint**:

* **`paper/main.pdf`** (source `paper/main.tex`): *Answers to some recent conjectures and questions in classical analysis, with computer assistance.*
* `CITATIONS.md` — every cited paper opened; exact titles/authors; the conjectures quoted word for word; corrections found.
* `NOVELTY.md` — literature search for each result (queries in `novelty_parts/`), with labels not found / probably known / known.
* `VERIFICATION.md` — for each result: what was checked, by which method, the outcome, the final label (referee reports and fresh-code reports are in `referee_reports/`).
* `PAPER_SUMMARY.md` — plain-English account of the paper, what was dropped and why, what changed after verification.

## Results in the paper (details in `formulas.txt`)
| Question (who asked) | Result | Label |
|---|---|---|
| Fan, arXiv:2609.11186, Conjectures 5.9 and 5.6 (Riesz capacity of three points on a circle; odd regular polygons) | both true (equilibrium measure exists with the stated support and masses) | **PROVED** (relying on three results quoted in Fan's paper) |
| Xu–Zhao, arXiv:2609.11072, Conjecture 6.1 (sign thresholds Gr(ℓ) of higher-order Gregory coefficients) | false; Gr(3..10)=11,36,113,346,1030,2995,8580,24303; Gr(11..14) numerically | **PROVED (computer-assisted)** for ℓ ≤ 10; numerical beyond |
| Fasi–Higham Conjecture 3.2, diagonal case left open by Scardino (arXiv:2610.39051) | true for every odd 3 ≤ m ≤ 361 (positive Taylor coefficients of 1/q_{m,m}); first failure for fixed m at k*(m) ≈ 2m+12..14 | **PROVED (computer-assisted)** per m; law **VERIFIED (numerical)** |
| Chen–Nguyen, arXiv:2507.19502 (closed forms of Σ H_k…H_{k+q}/(k…(k+q))) | exact reduction to multiple zeta values for q ≤ 9; closed forms in zeta values for q ≤ 8 | **PROVED (computer-assisted)** reduction; closed forms **VERIFIED (numerical identification)** |
| Finch, arXiv:2506.07625 (delta conjectures for Abel's equation) | δ = −(a/τ)·ln(−τγ), a=(τ+1)/2−c₂/γ² | **PROVED** (elementary; log coefficient is classical) |
| Wiśniewska, arXiv:2512.07028, open problems 1, 2 (Gurland's ratio) | series converges for all x,y>0; problem 3: conjecture t > (x+y+√xy)/3 | **PROVED** (elementary) / conjecture (numerical) |
| Finch, arXiv:2503.13378 and 2509.24918 | C″(2)=0.37462642198301734111677…; T(4/3,½), T(5/4,½), T(6/5,½) | **VERIFIED (numerical)** |
| Krasniqi, arXiv:2610.33699 (exact real completely monotonic degrees) | d_CM(R₂)=2.8667042552, d_CM(−R₂′)=3.7984354776 (+ table) | **VERIFIED (numerical)** |

## Found but already known (not claimed)
* Habib–Hildebrand Conjecture 7.1 — proved by the same authors in arXiv:2606.24182 (our independent proof in `results/painleve_series` is correct but not new).
* Chavan–Kobayashi–Layja Conjecture 4.5 (t-values) — proved by Charlton, arXiv:2112.14613.
* Finch's A/B and I/J identities — explained in Finch's own corrigendum (arXiv:2503.00579).
* Samart's n₄(81) conjecture — refuted and explained in H. Zheng, arXiv:2608.02265.

## Repo map
`paper/` the preprint · `CLAUDE.md` briefs and progress logs · `CITATIONS.md`, `NOVELTY.md`, `VERIFICATION.md`, `PAPER_SUMMARY.md` · `formulas.txt` recorded results · `TARGETS.md` scouting list · `NOTES.md` dead ends and leads · `results/*/` code, logs, proof write-ups · `referee_reports/` independent referee and verification reports · `novelty_parts/` raw literature-search logs · `verify_all.py` re-runs the headline checks.
