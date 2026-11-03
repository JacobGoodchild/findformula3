> **SUPERSEDED (3 Nov 2026).** This is the first-night summary, kept for the record. A second session checked everything: several items below turned out to be **already known** (items 1/Painlevé 7.1, 3/Finch A-B, and the t-values conjecture and Samart explanation) or were **downgraded** (see `PAPER_SUMMARY.md`, `VERIFICATION.md`, `NOVELTY.md`). The draft e-mails that used to be here were removed. For the current state read `PAPER_SUMMARY.md` and `paper/main.pdf`.

# Morning summary (final, written 06:20 UK, 3 November 2026)

Good morning. This is the plain-English version. Everything below was done by Claude, on the session's own machine, and **nothing has been sent, posted or submitted** — the e-mails at the bottom are drafts for you to look at.

## What I did differently
Instead of picking curiosities, I looked for **specific questions that a researcher has written down in a recent paper** ("this is open", "we conjecture", "it would be good to see ..."), opened the paper to make sure the question is really there, and then answered it.
Every result carries an honest label: **proved** (a full argument, checked by computer), **verified** (matches high-precision numbers and an independent check, but no proof), or **partial**.

## What was found (best first)
1. **A conjecture about a Painlevé-type differential equation is true — proved.** (Habib & Hildebrand, June 2026, Conjecture 7.1.) For the equation u″u − u′² = e^{−x}P(u) − 1 they conjectured that a certain series solution always has polynomial coefficients. I proved it: the only possible obstruction at each step is a single number, and a short local calculation at the point where u = 0 shows it always vanishes. I also reduced their second conjecture (the coefficients are all non-negative) to one clean statement that I checked in hundreds of cases but could not prove. *Label: proved (first conjecture), partial (second).*
2. **Steven Finch's "delta conjectures" — proved with one formula.** Finch compared two ways of solving a functional equation (Abel's equation) and noticed a mysterious constant that differs between them; he guessed its exact value in about 17 cases and asked for proofs. One short asymptotic calculation gives the value in all of them (including sin x, ln(1+x), the Fresnel cosine). *Proved.*
3. **Finch's two "surprising identities" between four Abel functions — proved.** They follow from the fact that the map x ↦ x/(1+x) transforms one iteration into the other. *Proved.*
4. **Two more questions of Finch's answered numerically:** the missing half-step values T(4/3,½), T(5/4,½), T(6/5,½) of "tower" functions (40 digits), and an independent confirmation of C″(2)=0.3746264219830… for the recurrence x ↦ x+1+1/x² (and an explanation of why his first guess 0.3909 was wrong: one factor was missing). *Verified.*
5. **A published conjecture about higher-order Gregory coefficients is false.** (Xu & Zhao, Sept. 2026, Conjecture 6.1.) It said a certain threshold grows like 3^ℓ; their own table already breaks it, and I computed the true thresholds for ℓ=8…14 (2995, 8580, 24303, 68283, 190698, 530152, 1468691). The growth is governed by exp(π·cot(π/ℓ)) ≈ e^ℓ, not 3^ℓ. *Proved for ℓ≤10, verified beyond.*
6. **Harmonic-number series.** For the series Σ H_k H_{k+1}…H_{k+q}/(k(k+1)…(k+q)) (Furdui–Sîntămărian; Chen–Nguyen asked for general q) I wrote an exact algorithm that reduces it to multiple zeta values for any q, got explicit answers for q up to 8, and found a clean law for the "leading part": (ζ(q+2)+ζ(q+1,1))/q!. *Proved for q ≤ 5, verified for q = 6–8, law verified for q ≤ 9.*
7. **A positivity conjecture for matrix-exponential approximations (Fasi–Higham).** A 2026 paper disproved it in general but left the practically relevant diagonal case open. I proved the diagonal case for every odd size from 3 up to 361 (rigorous computer-assisted proofs) and found exactly where it really fails: the first failure is at k = 2m + 12…14, so the diagonal is nowhere near the danger zone. *Proved for each m tested; the failure law is verified.*
8. **Capacity of three points on a circle (Fan, 2026).** A conjecture that was only half proved in the paper (which polygon vertices maximise a certain energy) — I proved the missing step with a short calculus lemma, which completes the proof for all odd polygons. *Proved.*
9. **How "completely monotone" the Stirling remainders are (Krasniqi, 2026).** The paper only gave bounds, e.g. 8/3 < d < 3; I computed the actual numbers: 2.8667042552 and 3.7984354776 (tables checked to n = 22; extra values up to n = 27 sit in the logs but were not folded into the limit estimate), with two independent checks, and found numerically that the paper's open 'limit' question has the answer 2π²/Cin(2π) = 8.0976… (the paper's own upper bound is sharp; I match it to about 4 digits). *Verified (limit: numerical evidence).*
10. **Gurland's gamma-function ratio (Wiśniewska, Dec. 2025).** Two of the three open problems have a one-line answer (a Taylor series that converges for all inputs); for the third I found the sharp constant (1/3) and a numerically supported inequality I could not prove. *Proved / partial.*

11. **A conjecture on t-values (Chavan, Kobayashi, Layja et al., arXiv:2111.07097, Conjecture 4.5) — proved.** The value t({2}^N,1) equals I(2N)/(2N)! for every N; the proof goes through a Gamma-function product, a Beta-integral and the series for x/√(1−x²). *Proved* (checked numerically for N=1..4).
12. **Why a Mahler-measure guess failed (Samart's n_4(81), arXiv:2608.02265).** The guess 40·L-value is actually the real part of the analytic continuation (agrees to 25+ digits) but the true Mahler measure is 4.16553(5), about 0.0587 bigger. I could not find a closed form for the true value. *Verified* (the explanation), no closed form.
13. **Chance that a random degree-4 polynomial is stable (Gasull, arXiv:2012.02524 context).** p_4 = 0.0092838447242981189571, from a two-dimensional integral I derived; no closed form found, and Gasull's actual question (behaviour for large degree) is NOT answered. *Partial, numerical only.*

## What did not work / was dropped
* The sharp-constant problems of Gorbachev's survey (Hörmander–Bernhardsson constant) — famous, heavily attacked; dropped.
* The AI-generated Bessel-moment conjecture (arXiv:2609.22318) — numerical agreement proves nothing; dropped.
* The Schwarzian-norm conjecture for α-convex functions (arXiv:2606.21574): I proved the easy half (the boundary limit gives exactly the conjectured value) but not the "nothing larger anywhere in the disc" half.
* The positivity of the extra coefficients in the Painlevé series (Conjecture 7.2) and the Gurland inequality resisted proof tonight.

## Best leads for next time
(see NOTES.md) 1. Finish the positivity proof for the Painlevé series (Conjecture 7.2); the proof structure is half there. 2. Prove k*(m)=2m+O(1) for the Padé problem, which would settle the diagonal case for all m. 3. Prove the Gurland inequality t(x,y) > (x+y+√xy)/3.


---
**Note on the night:** the computer was restarted about every 40 minutes after midnight, which killed long jobs; I restarted them and the logs show it. Nothing was lost, but the Padé proofs stopped at m=361 and the n=28..30 Stirling values were never finished.
