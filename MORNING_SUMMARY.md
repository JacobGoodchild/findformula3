# Morning summary (draft written at ~23:00 UK; final version at the end of the night)

Good morning. This is the plain-English version. Everything below was done by Claude, on the session's own machine, and **nothing has been sent, posted or submitted** — the e-mails at the bottom are drafts for you to look at.

## What I did differently
Instead of picking curiosities, I looked for **specific questions that a researcher has written down in a recent paper** ("this is open", "we conjecture", "it would be good to see ..."), opened the paper to make sure the question is really there, and then answered it.
Every result carries an honest label: **proved** (a full argument, checked by computer), **verified** (matches high-precision numbers and an independent check, but no proof), or **partial**.

## What was found (best first)
1. **A conjecture about a Painlevé-type differential equation is true — proved.** (Habib & Hildebrand, June 2026, Conjecture 7.1.) For the equation u″u − u′² = e^{−x}P(u) − 1 they conjectured that a certain series solution always has polynomial coefficients. I proved it: the only possible obstruction at each step is a single number, and a short local calculation at the point where u = 0 shows it always vanishes. I also reduced their second conjecture (the coefficients are all non-negative) to one clean statement that I checked in hundreds of cases but could not prove. *Label: proved (first conjecture), partial (second).*
2. **Steven Finch's "delta conjectures" — proved with one formula.** Finch compared two ways of solving a functional equation (Abel's equation) and noticed a mysterious constant that differs between them; he guessed its exact value in about 17 cases and asked for proofs. One short asymptotic calculation gives the value in all of them (including sin x, ln(1+x), the Fresnel cosine). *Proved.*
3. **Finch's two "surprising identities" between four Abel functions — proved.** They follow from the fact that the map x ↦ x/(1+x) transforms one iteration into the other. *Proved.*
4. **Two more questions of Finch's answered numerically:** the missing half-step values T(4/3,½), T(5/4,½), T(6/5,½) of "tower" functions (40 digits), and an independent confirmation of C″(2)=0.3746264219830… for the recurrence x ↦ x+1+1/x² (and an explanation of why his first guess 0.3909 was wrong: one factor was missing). *Verified.*
5. **A published conjecture about higher-order Gregory coefficients is false.** (Xu & Zhao, Sept. 2026, Conjecture 6.1.) It said a certain threshold grows like 3^ℓ; their own table already breaks it, and I computed the true thresholds for ℓ=8…13 (2995, 8580, 24303, 68283, 190698, 530152). The growth is governed by exp(π·cot(π/ℓ)) ≈ e^ℓ, not 3^ℓ. *Proved for ℓ≤10, verified beyond.*
6. **Harmonic-number series.** For the series Σ H_k H_{k+1}…H_{k+q}/(k(k+1)…(k+q)) (Furdui–Sîntămărian; Chen–Nguyen asked for general q) I wrote an exact algorithm that reduces it to multiple zeta values for any q, got explicit answers for q up to 8, and found a clean law for the "leading part": (ζ(q+2)+ζ(q+1,1))/q!. *Proved for q ≤ 5, verified for q = 6–8, law verified for q ≤ 9.*
7. **A positivity conjecture for matrix-exponential approximations (Fasi–Higham).** A 2026 paper disproved it in general but left the practically relevant diagonal case open. I proved the diagonal case for every odd size up to a few hundred (rigorous computer-assisted proofs) and found exactly where it really fails: the first failure is at k = 2m + 12…14, so the diagonal is nowhere near the danger zone. *Proved for each m tested; the failure law is verified.*
8. **Capacity of three points on a circle (Fan, 2026).** A conjecture that was only half proved in the paper (which polygon vertices maximise a certain energy) — I proved the missing step with a short calculus lemma, which completes the proof for all odd polygons. *Proved.*
9. **How "completely monotone" the Stirling remainders are (Krasniqi, 2026).** The paper only gave bounds, e.g. 8/3 < d < 3; I computed the actual numbers: 2.8667042552 and 3.7984354776 (and a table up to n = 9), with two independent checks. *Verified.*
10. **Gurland's gamma-function ratio (Wiśniewska, Dec. 2025).** Two of the three open problems have a one-line answer (a Taylor series that converges for all inputs); for the third I found the sharp constant (1/3) and a numerically supported inequality I could not prove. *Proved / partial.*

## What did not work / was dropped
* The sharp-constant problems of Gorbachev's survey (Hörmander–Bernhardsson constant) — famous, heavily attacked; dropped.
* The AI-generated Bessel-moment conjecture (arXiv:2609.22318) — numerical agreement proves nothing; dropped.
* The Schwarzian-norm conjecture for α-convex functions (arXiv:2606.21574): I proved the easy half (the boundary limit gives exactly the conjectured value) but not the "nothing larger anywhere in the disc" half.
* The positivity of the extra coefficients in the Painlevé series (Conjecture 7.2) and the Gurland inequality resisted proof tonight.

## Best leads for next time
(see NOTES.md) 1. Finish the positivity proof for the Painlevé series (Conjecture 7.2); the proof structure is half there. 2. Prove k*(m)=2m+O(1) for the Padé problem, which would settle the diagonal case for all m. 3. Prove the Gurland inequality t(x,y) > (x+y+√xy)/3.

## Draft e-mails (NOT sent) — see the end of this file, added at the end of the night.

---
## Draft e-mails (NOT sent — you decide). Each discloses that the work was done by an AI system under your direction.

**1. To Rahaf Habib and Roland Hildebrand (arXiv:2606.21145, Conjecture 7.1)**
Subject: A proof of Conjecture 7.1 in "Necessary conditions for the existence of exponential-polynomial expansions ..."
Dear Dr Habib, dear Prof. Hildebrand — I am writing on behalf of myself and an AI system (Claude, Anthropic), which did the mathematical work under my direction. Your Conjecture 7.1 (polynomials p_k exist when π0=0, π1=π2) follows from a short argument: the obstruction at order s is the coefficient [x²] of e^{−sx}ρ_s (a residue), and expanding the truncated series around its zero shows this coefficient is a combination of lower-order residuals times O(ε), hence vanishes. For Conjecture 7.2 we could only reduce it to coefficientwise positivity of the right-hand sides ρ_s (checked exactly for s ≤ 12, hundreds of polynomials P). The write-up and code are at <repo>/results/painleve_series. We have not posted this anywhere; please tell us if you would like a cleaner note. — Jacob Goodchild

**2. To Steven Finch**
Subject: Proofs of the delta conjectures and of the A,B,I,J identities; three numerical items
Dear Dr Finch — an AI system (Claude, Anthropic), working under my direction, found (i) a one-line asymptotic derivation of all your delta conjectures: δ = −(a/τ)ln(−τγ) with a = (τ+1)/2 − c2/γ² (it reproduces ≈17 of your cases, including sin x, ln(1+x), the Fresnel cosine, and your Addendum II/III formulas); (ii) a proof of A(x/(1+x)) = B(x)+1 and I(x/(1+x)) = J(x)+1 (the map x/(1+x) conjugates the iterations and shifts 1/x by 1); (iii) 40-digit values T(4/3,½), T(5/4,½), T(6/5,½); (iv) the exact series C″(x0) = C′(x0)Σ f″(xj)Dj/f′(xj), giving C″(2) = 0.374626421983017341116…, and an explanation of the missing factor Dj in the 0.3909 series. Details: results/abel_delta, abel_finch, tetration_half, finch_c2. — Jacob Goodchild

**3. To Wilson Chen and Vincent Nguyen (arXiv:2507.19502)**
Subject: Closed forms for Σ H_k…H_{k+q}/(k…(k+q)), q ≤ 8
Dear Dr Chen, dear Dr Nguyen — an AI system (Claude, Anthropic), working under my direction, wrote an exact algorithm reducing S_q to multiple zeta values for every q; it reproduces your q=3 formula and gives explicit closed forms for q=4,…,8 (e.g. S_4 = ζ(2)/432 − 45ζ(3)/64 + 1799ζ(2)²/8640 − 11ζ(2)ζ(3)/72 + 13ζ(5)/18 + ζ(2)³/60 − ζ(3)²/48), checked to 60 digits, plus the observation that the top-weight part is (ζ(q+2)+ζ(q+1,1))/q!, which shows the Furdui–Sîntămărian conjecture fails unless products like ζ(a)ζ(b) (a+b=q+2) collapse. Files: results/harmonic_products. — Jacob Goodchild

**4. To Ce Xu and Jianqiang Zhao (arXiv:2609.11072)**
Subject: Conjecture 6.1 (Gr(ℓ)) appears to be false; new values of Gr(ℓ)
Dear Dr Xu, dear Prof. Zhao — an AI system (Claude, Anthropic), working under my direction, recomputed Gr(ℓ) with interval arithmetic: Gr(3..7) agree with your table; Gr(8)=2995, Gr(9)=8580, Gr(10)=24303 (rigorous using your tail bound), Gr(11..13)=68283, 190698, 530152. Gr(5)=113 < 0.47·3⁵ already violates Conjecture 6.1, and Gr(ℓ)/3^ℓ keeps decreasing: Gr(ℓ)/exp(π cot(π/ℓ)) stays near 1.5–1.55 (the largest zero of H_ℓ is exactly exp(π cot(π/ℓ)); r(9) in your table seems to be a misprint of 5605.2). Files: results/gregory. — Jacob Goodchild

**5. To Francesco Scardino (arXiv:2610.39051)**
Subject: Diagonal case of the Fasi–Higham conjecture
Dear Dr Scardino — an AI system (Claude, Anthropic), working under my direction, proved by rigorous ball arithmetic (certified roots, residues, interval check of the initial coefficients) that for every odd m up to a few hundred all Taylor coefficients of 1/q_{m,m} are positive, and found numerically that the smallest k with a negative coefficient is k*(m)=2m+12…14 (m up to 1009), with the failing set exactly {k ≥ k*(m)}. So the diagonal sits far inside the region of validity; the general diagonal statement remains open. Files: results/pade_positivity. — Jacob Goodchild

**6. To Qiuling Fan (arXiv:2609.11186)**
Subject: A proof of Conjectures 5.9 and 5.6
Dear Dr Fan — an AI system (Claude, Anthropic), working under my direction, found a proof of Conjecture 5.9: d log U/dψ has the sign of (1+t_r)/(1−t_r) − (1+t_2)/(1−t_2) with t_r = ρ_B^r − ρ_A^r, and t_r ≥ t_2 follows from a short lemma (unimodality in r plus an entropy comparison). Together with your Lemma 5.8 this completes Conjecture 5.6 for all odd N and r>2 (given the Björck and Clark–Laugesen results you quote). Brute-force checks for odd N ≤ 31 agree. Files: results/riesz_triangle. — Jacob Goodchild

**7. To Valmir Krasniqi (arXiv:2610.33699)**
Subject: Numerical values of d_CM(R_2), d_CM(−R_2′) and (2n−1)δ_n
Dear Dr Krasniqi — an AI system (Claude, Anthropic), working under my direction, computed the real completely monotonic degrees via the fractional-derivative criterion: d_CM(R_2) = 2.8667042552, d_CM(−R_2′) = 3.7984354776, and a table for n ≤ 15+ (two independent evaluations of the criterion). (2n−1)δ_n increases slowly (2.60 at n=2 to ≈6.6 at n=15). Files: results/stirling_cm. — Jacob Goodchild

**8. To Halina Wiśniewska (arXiv:2512.07028)**
Subject: Open problems 1–2 on Gurland's ratio
Dear Dr Wiśniewska — an AI system (Claude, Anthropic), working under my direction, notes that ln Γ(1+m+z) is analytic on |z|<1+m, so the series S_∞ converges to ln G* for all x,y>0 (answering open problems 1 and 2 affirmatively), and that for problem 3 the constant 1/3 is sharp (t(x,y) lies at most 1/3 of the way from the midpoint toward √(xy) asymptotically); a conjectured inequality t > (x+y+√xy)/3 is supported by numerics but unproved. Files: results/gurland. — Jacob Goodchild
