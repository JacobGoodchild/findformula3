# Paper brief (current)

# findformula3: verify everything, then write the paper

You are working in the GitHub repo **JacobGoodchild/findformula3**. Last night's session left 13 results there (see `formulas.txt`, `MORNING_SUMMARY.md`, `results/`, `TARGETS.md`, `NOTES.md`). Your job now is to **check every result and every citation properly, cut anything that doesn't survive, and write one Zenodo-ready preprint.**

This is a **wrap-up job, not more research**: no new problems, no extending results. Work only as long as it takes to check and write things up properly, then stop. **Tell me first**: your very first message should be a short plan in plain English, with an estimate of how many hours you expect each phase to take. Then start straight away without waiting for a reply (I may be away). Put the same plan at the top of the progress log.

**First thing:** add this brief to the top of `CLAUDE.md`, above the old brief, under a heading `# Paper brief (current)`, with a new `## Paper progress log` section. Keep the old brief below it, marked as finished. CLAUDE.md is your memory if you get restarted.

---

## 0. Usage limits: keep a wake-up alarm set (set this up FIRST)

A usage limit can stop you partway through, and you can't make a tool call once it hits. So keep a "dead man's switch" running:

1. **Right at the start**, use your scheduling tool (`send_later`, or `ScheduleWakeup`; search your tools for "schedule" if neither shows) to schedule a message back into **this same session** about **45 minutes** from now, saying:
   `WAKE-UP CHECK: if you were stopped by a usage limit, re-read CLAUDE.md (paper brief + paper progress log), check git status and git log, and carry on from where you left off. If you are already mid-task, ignore this, but make sure a new wake-up is scheduled. If the job is finished, do nothing.`
2. **After every commit**, schedule a fresh wake-up about 45 minutes ahead, and cancel the older one if your tool allows it.
3. **Backup chain:** at the start, also schedule wake-ups every 90 minutes for the next 8 hours. Extra ones that arrive while you're busy are harmless.
4. **After any restart**, first re-read CLAUDE.md and `git log`. Never redo committed work. Background jobs are probably dead (last night the machine restarted about every 40 minutes), so check them and relaunch if needed. Design long jobs to **save progress to disk and resume**, not start over.
5. **When the whole job is finished**, cancel every remaining wake-up.
6. **If no scheduling tool exists in this session**, write that as the first line of the progress log.

Commit and push after every small step, with a short progress-log entry each time.

---

## 1. Phase A: check every citation (do this before anything else)

Last night's session moved fast and its novelty checks were often "one web search". Assume nothing.

For **every paper cited anywhere** in `formulas.txt`, `results/*/README.md` and `MORNING_SUMMARY.md`:
1. Open the actual arXiv page or DOI and the PDF.
2. Confirm the **exact title, all authors (spelled correctly), year, and arXiv ID/DOI**.
3. Confirm the **exact statement** we claim to answer: the conjecture/question number, the section, and the precise wording. Copy the original statement word for word into `CITATIONS.md` next to our claim, and check they really match. Watch especially for:
   - **Gregory coefficients (Xu & Zhao, arXiv:2609.11072, "Conjecture 6.1")**: we claim their own table breaks their conjecture. That is unusual; make sure we haven't misread the statement (range of ℓ, the exact constants, how Gr(ℓ) is defined).
   - **t-values (Chavan, Kobayashi, Layja, arXiv:2111.07097, "Conjecture 4.5")**: this paper is from 2021. Search hard (arXiv, citing papers, Google Scholar-style searches, the authors' later papers) for anyone who has proved it since. Check the author list too.
   - **Anything cited from memory** (e.g. Hoffman proving N = 1, 2, 3; Björck; Clark–Laugesen; Kitaev 2025): find the real source or remove the claim.
4. If a paper can't be opened, say so in `CITATIONS.md` and don't rely on it.
5. Record anything wrong (titles, names, IDs, misquoted conjectures) and fix it everywhere.

**Never invent or "repair" a citation from memory.** If you can't confirm it, it doesn't go in the paper.

## 2. Phase B: novelty check for every result

For each of the 13 results, do a **proper** literature search: at least 5 different search queries, the citing papers of the source paper, the authors' later work, standard references (DLMF, Gradshteyn & Ryzhik, OEIS for any integer sequences such as the Gr(ℓ) values), and searches for special cases. Record queries and findings in `NOVELTY.md`. Label each result **"not found" / "probably known" / "known"**, with links. Anything "known" is dropped from the paper (or kept only as a credited remark).

## 3. Phase C: independent verification of every result

The same AI that found a result is a poor judge of it. So:

1. **For every result marked PROVED**, use a **separate agent that has not seen last night's work** (spawn a fresh subagent with the Agent tool, giving it only the statement and the written proof, not our code or our conclusions). Ask it to check the proof line by line as a sceptical referee: find gaps, unjustified steps, hidden assumptions, and cases not covered. Fix every gap it finds, or downgrade the label. Repeat until a fresh referee finds no gaps.
2. **Every algebraic step** should be checked by computer algebra (sympy etc.), and **every numerical step used in a proof** must have rigorous error bounds (interval/ball arithmetic: mpmath `iv`, or python-flint/arb). Floating-point checks don't count as proof.
3. **For every VERIFIED (numerical) result**, recompute the key numbers **from scratch with fresh code written by a fresh agent** that hasn't seen our code, using a different method where possible. The digits must agree.
4. **Computer-assisted proofs** (Padé m ≤ 361, Gregory ℓ ≤ 10): check that the existing logs cover every case with no gaps, and re-run a sample of cases (including the largest) from clean scripts to confirm they reproduce. Don't re-run the whole overnight computation.
5. Keep a table in `VERIFICATION.md`: result, what was checked, by which method, outcome, final label.

Labels must be honest: **PROVED** only if the proof survives a fresh referee and all computations are rigorous; otherwise **VERIFIED (numerical)** or **PARTIAL**. Downgrading is fine. Being wrong in public is not.

## 4. No new research

**Don't start any new research or try to extend the results.** This is a wrap-up job: check what exists, cut what fails, and write it up. Open problems (e.g. Habib–Hildebrand Conjecture 7.2, a proof of the Gregory growth law, the all-m Padé diagonal case, the Gurland inequality) go in the paper's "open problems" section as they stand. Don't relaunch the long Padé or Stirling runs to push them further either; use the results already in the logs. Finish as soon as the job is done properly.

## 5. Phase D: write the paper

Write one LaTeX preprint in `paper/` (source + compiled PDF). Working title along the lines of *"Solutions to some recent conjectures and questions in classical analysis"*; choose a better one if the content suggests it.

- **Only include results that passed Phases A–C.** Group them by topic (differential equations, special functions and series, asymptotics, inequalities, functional equations and iteration), with the strongest results first.
- For each result: the original question, quoted and properly cited (who asked, where); our statement as a numbered theorem/proposition; the full proof (or, for numerical results, the method, precision and error bounds); and what remains open.
- Clearly separate **proved theorems**, **computer-assisted proofs** (say exactly what was computed) and **numerical results** (never present these as theorems).
- Credit prior work honestly, including special cases that were already known.
- An abstract, an introduction explaining what the paper does, and a short "open problems" section at the end.
- References: only papers you actually opened in Phase A, with correct details. Run a final check that every `\cite` resolves and every bibliography entry matches what you recorded in `CITATIONS.md`.
- Code availability: link this repo.
- Write it in normal mathematical style (no AI-flavoured filler, no hype words like "remarkable", "elegant", "groundbreaking").

**AI disclosure statement** (put it in the abstract footnote or a clearly labelled section, and in the README):
> This work was carried out with extensive use of an AI system, Claude (Anthropic), via the Claude Code software, under the direction of Jacob Goodchild. The AI system chose the problems from the recent literature, carried out the derivations, proofs and computations, searched and checked the literature, and wrote the manuscript. Proofs were checked by independent AI referee passes and by computer algebra and interval arithmetic, but have not been checked by a human expert or peer reviewed. Novelty assessments are based on literature searches and may be incomplete. Jacob Goodchild directed the work and is responsible for its publication.

Remove the draft e-mails from the repo's summary documents; they are not needed.

## 6. Phase E: final review

1. Spawn **one more fresh agent** to read the finished PDF as a referee: correctness, clarity, whether every claim is supported, whether every citation is right, and whether any result looks trivial or already known. Fix what it finds.
2. Run `verify_all.py` (updated to cover everything in the paper); all must be OK.
3. Prepare `paper/ZENODO.md` with suggested metadata (title, description, keywords, licence CC BY 4.0, related link to this repo), using the same style as my earlier Zenodo records. **Do not upload anything.**
4. Write `PAPER_SUMMARY.md` for me in **plain English, no jargon**: what's in the paper, what was dropped and why, what changed after verification (any downgrades or errors found), and an honest one-paragraph assessment of how significant the paper is.
5. Commit, push, cancel all remaining wake-ups.

---

## Rules (non-negotiable)

1. **Verify everything.** If a check fails, the result is wrong until shown otherwise.
2. **Never invent citations, numbers, quotes or authors.** Only cite what you opened.
3. **Honest labels.** Never call something proved when it was only matched numerically, or new when you haven't searched.
4. **Computing:** only on this session's own machine. **Never use GitHub Actions** or any other cloud service. Don't hammer websites with automated requests.
5. **Never post, upload, email, comment or submit anything anywhere** (no Zenodo, arXiv, emails). I'll publish it myself.
6. Run long jobs in the background with logs and resumable progress; don't leave orphaned processes; never use `pkill -f`/`pgrep -f` with a pattern that matches your own shell.

## Paper progress log

- REVISED PLAN (user: finish by ~16:40 UTC, 3 Nov; must not take 17 h): A citations 1h (to ~09:30), B novelty 1h (~10:30), C verification 2.5h (~13:00), D paper 2h (~15:00), E final review 1h (~16:00-16:40). Run referee/search agents in parallel to save time.
- (superseded) PLAN (written at start, ~06:30 UTC 3 Nov 2026). Estimated hours: setup 0.25; Phase A citations 2-3; Phase B novelty 2-3; Phase C verification 3-5; Phase D paper 3-4; Phase E final review 1.5-2. Total about 12-17 h. Results that fail a check are downgraded or cut.

---

# OLD BRIEF (overnight calculus night: FINISHED, kept for reference)

# findformula3: overnight research brief

You are working in the GitHub repo **JacobGoodchild/findformula3** (currently empty). **Tonight's topic is calculus** (see section 2). Work **all night without stopping until 07:00 UK time (07:00 UTC, the clocks are on GMT)**. Don't ask me questions; I'm asleep. Make the most reasonable choice, write down why in the log, and keep going. Never stop early because "enough has been done": if a target is finished or stuck, pick the next one.

**First thing, before anything else:** copy this whole brief into `CLAUDE.md` at the top of the repo, with an empty `## Progress log` section underneath. That file is your memory if you get restarted.

---

## 0. Usage limits: keep a wake-up alarm set (set this up FIRST)

A usage limit can stop you partway through the night, and you can't make a tool call once it hits. So keep a "dead man's switch" running:

1. **Right at the start**, use your scheduling tool (`send_later`, or `ScheduleWakeup`; search your tools for "schedule" if neither shows) to schedule a message back into **this same session** about **45 minutes** from now, saying:
   `WAKE-UP CHECK: if you were stopped by a usage limit, re-read CLAUDE.md (brief + progress log), check git status and git log, and carry on from where you left off until 07:00 UK. If you are already mid-task, ignore this, but make sure a new wake-up is scheduled.`
2. **After every commit**, schedule a fresh wake-up about 45 minutes ahead, and cancel the older one if your tool allows it.
3. **Backup chain:** at the start, also schedule wake-ups at **23:00, 00:30, 02:00, 03:30, 05:00 and 06:15 UK**. Extra ones that arrive while you're busy are harmless; just make sure a next one exists and keep going.
4. **After any restart**, first re-read CLAUDE.md and `git log`. Never redo work that's already committed. Any background computation that was running is probably dead, so check and restart it if needed.
5. **At about 06:45 UK**, cancel any wake-ups scheduled after 07:00, so nothing restarts the session in the morning.
6. **If no scheduling tool exists in this session**, write that as the very first line of the progress log, so I know to restart you by hand.

Commit and push after every small step (a working script, a checked number, a finished section), with a short progress-log entry each time, so nothing is lost if you're cut off.

---

## 1. Background: read the two earlier repos first (about 20 minutes, not more)

Clone and skim **JacobGoodchild/findformula** and **JacobGoodchild/findformula2** (both public), especially `README.md`, `NOTES.md` and the index at the top of `formulas.txt`. They show the method that has worked:
- findformula: exact results for lattice models via Kirchhoff transfer currents/lattice Green functions (Grover-walk trapping, sandpile height-one probabilities, spanning-tree entropies, resistances). Two Zenodo preprints.
- findformula2: exact formulas for Kerr black holes (shadow areas, capture cross-sections, escape probabilities). One preprint. It also has two short failed attempts at famous problems (Hadwiger–Nelson, cap sets).

Reuse their code and their **pitfalls** (in the NOTES files), e.g. importing a module that resets `mp.dps`; `pkill -f`/`pgrep -f` killing your own shell; double-precision cancellation; "special case" values turning out to be already known, so search harder for those.

---

## 2. What I want tonight (read carefully, this is the important part)

I'm **bored of obscure closed forms that nobody asked for**. I also know that aiming at famous problems (P vs BPP, Hadwiger–Nelson, cap sets, brute-force counterexample hunts) has produced nothing. Aim in between: **medium-impact results**.

**The rule for choosing targets: someone already wants the answer.** A good target is a specific question that a real researcher has written down in a recent paper (roughly 2022–2026), for example:
- "the exact value of X is not known" / "we could only compute X numerically" / "it would be interesting to find a closed form for X";
- a stated **conjecture** that is checkable and provable with computation plus algebra;
- an "open problem" or "future work" item at the end of a paper;
- a result that was proved only in special cases, where the general case looks within reach;
- a quantity people currently use **fits or tables** for, where an exact formula or a proof would replace them.

**Tonight's topic is CALCULUS. Every target must be a calculus question.** That means things like:
- **definite integrals** whose exact value is asked for or conjectured (including multiple integrals, and integrals that turn up in physics, probability or number theory);
- **infinite series and sums** (closed forms, convergence, rates of convergence, Euler-type sums);
- **inequalities** proved with calculus (sharp constants, best possible bounds, conjectured inequalities);
- **asymptotics** (expansions as n → ∞ or x → 0, leading constants, error terms);
- **differential equations** (exact solutions, conjectured properties of solutions, special-function identities they lead to);
- **limits, products and special functions** (Gamma, zeta, polylogarithms, elliptic integrals, hypergeometric functions) where a stated identity or value is open.

The question can come from any field (physics, probability, number theory, combinatorics) as long as the actual problem is a calculus problem. Good sources: open problems and conjectures in recent arXiv papers (math.CA "Classical Analysis and ODEs", math.NT, math-ph), problem sections and "open problem" lists in analysis journals, and conjectures from papers on integrals and series. The tests below still apply.

**Do NOT spend the night on:**
- anything that isn't calculus;
- more entries in my existing lattice tables, or more Kerr variants of results already in findformula2, unless a paper explicitly asks for that specific one;
- textbook integrals and series that are already in standard tables (Gradshteyn & Ryzhik, DLMF); check there before claiming anything;
- the snub-square/Cairo results (another mathematician, Erik Ersson, is writing proofs of those; leave them to him);
- famous problems that big groups and huge computers have already attacked;
- PSLQ hunts on constants that nobody has asked about.

### Target tests (all must pass before you commit time to a target)
Write each candidate into `TARGETS.md` with:
1. **Who asked:** the paper (title, authors, arXiv ID or DOI) and the exact place the question appears. **Open the paper and confirm the question is really there.** Never invent or guess a citation.
2. **Still open?** Search (arXiv, Google Scholar-style web searches, citing papers) for anyone who answered it since. If it has been answered, drop it.
3. **Why it matters:** one or two sentences in plain English.
4. **Doable in a few hours** with computation plus algebra, and **checkable**: there must be an independent way to confirm the answer.
5. **Impact score** 1–5 (5 = the question appears in several papers or blocks other work; 1 = a passing remark) and **chance of success** 1–5. Work on the best product first.

### Time plan
- **21:30–23:00 at most: scouting.** Collect at least 8 candidate calculus targets in `TARGETS.md`, ranked. Then start working. Don't scout forever.
- **Then work targets in order**, timeboxed to about **2.5 hours each**. If a target is stuck at the timebox, write what you learned in NOTES.md and move to the next. If a target is going well, you may extend it, but say so in the log.
- If you run out of targets, scout more (about 30 minutes), then continue.
- **06:15–07:00: wrap-up** (section 5). Start it on time.

---

## 3. What counts as a result

Label every result with one of these, honestly:
- **PROVED**: a complete proof, written out step by step in `results/`, with every algebraic step checked by computer algebra (sympy etc.) and any numerical step backed by rigorous error bounds (interval arithmetic, e.g. mpmath `iv` or python-flint/arb if you can install it). This is the best kind. Prefer proofs over new closed forms.
- **VERIFIED (not proved)**: identified numerically (PSLQ at 50+ digits, predicted digits confirmed at even higher precision) AND confirmed by an independent method (a different formula, exact finite-size computations, simulation). Only worth recording if the quantity was explicitly asked for in a paper.
- **PARTIAL**: e.g. a proof of a special case, a rigorous bound, extra terms of a series, or a counterexample to a published conjecture (counterexamples must be checked exactly, not in floating point).
- **NEGATIVE**: honest "no closed form found in basis X at N digits" or "this approach fails because…". These go in NOTES.md, not formulas.txt.

Every recorded result needs a **novelty check**: search properly, including for special cases, and label it "not found" / "probably known" / "known", with real links. "Not found" only means you couldn't find it, so say that.

---

## 4. Rules (non-negotiable)

1. **Verify everything.** No result goes in `formulas.txt` without an independent check. If a check fails, the result is wrong until shown otherwise.
2. **Never invent citations, numbers, quotes or authors.** Only cite papers you actually opened. If you can't access a paper, say so.
3. **Honest labels.** Never call something proved when it was only matched numerically. Never call something new when you haven't searched.
4. **AI disclosure:** the README must say plainly that the research was carried out by Claude (Anthropic), via Claude Code, under my direction, the same way the findformula and findformula2 READMEs do.
5. **Computing:** run everything inside this session's own machine only. **Never use GitHub Actions** or any other cloud service to run computations; that risks my account. Don't hammer any website with automated requests; normal searching and reading is fine.
6. **Never post, email, comment or submit anything anywhere** (no arXiv, Zenodo, MathOverflow, OEIS, emails). I decide what gets shared. You may draft things in the repo.
7. Keep long computations sensible: run them in the background with logs, check on them, and don't leave orphaned processes.
8. Keep everything in plain files in the repo: Python (mpmath, sympy, numpy, scipy; install anything else you need with pip).

### Repo layout
- `CLAUDE.md`: this brief + progress log (timestamped, one entry per commit).
- `TARGETS.md`: ranked candidate targets with the tests above, and the status of each (todo / working / done / dropped + why).
- `formulas.txt`: recorded results only, with an index at the top: statement, label (PROVED / VERIFIED / PARTIAL), who asked (citation), how it was checked, novelty status with links.
- `results/<short-name>/`: the code, logs, proof write-up and verification script for each result.
- `NOTES.md`: research log, including dead ends and leads for a future night.
- `verify_all.py`: re-runs the headline checks for every recorded result and prints OK/FAIL.

---

## 5. Wrap-up (start at 06:15 UK)

1. Run `verify_all.py`; fix or downgrade anything that fails.
2. Write `MORNING_SUMMARY.md` for me in **plain English, no jargon**:
   - a short list of what was found, best first, each with its label (proved / verified / partial), who asked for it, and one sentence on why it matters;
   - what was tried and didn't work;
   - the 3 best leads for next time;
   - for each strong result, a short **draft** email (NOT sent) to the author who asked the question, disclosing that the work was done by an AI system under my direction.
3. Update the README (what this repo is, the AI disclosure, a results table).
4. Commit and push, then cancel any leftover wake-ups after 07:00.

Go. Set up the wake-up alarms, write CLAUDE.md, then start.


---

## Progress log

- 21:25 UTC: started. Scheduling tool available (send_later). Wake-ups set: +45min and 23:00, 00:30, 02:00, 03:30, 05:00, 06:15 UK.
- 21:45 UTC: TARGETS.md written (9 candidates; T1 = Furdui-Sintamarian harmonic-product series, best). T1 working: numerics.py (EM tail, 60+ digits), exact_reduce.py (exact reduction to MZVs, matches numerics to 1e-62 for q<=4), reduce_mzv.py (MZV -> zeta products). q=4 closed form found (new?). NOTE: do not use `pkill -f` (killed own shell once).
- 21:55 UTC: T1 DONE (formulas.txt [1], results/harmonic_products): S_q closed forms q<=8, exact algorithm, verified 45-60 digits. Next: T2 (Gurland: open problems 1,2 answered by Taylor series, problem 3 numerics suggest t > (x+y+sqrt(xy))/3), then T3.
- 22:00 UTC: T2 done (gurland: problems 1,2 proved by Taylor series; problem 3 partial). T3 gregory: exact Gr(ell) ell=8..12 computed (new), Conjecture 6.1 refuted (ell=5,8,9,10 rigorous w/ paper's tail bound; Gr ~ 1.5*exp(pi*cot(pi/ell)) ~ e^ell not 3^ell). T10 painleve_series: Conjecture 7.1 (Habib-Hildebrand 2606.21145) PROVED (residue/local zero argument); 7.2 verified exactly to k=40, not proved. Waiting on Gr(13) run (results/gregory/gr_table_11_13.log).
- 22:45 UTC: T1 (harmonic products + top-weight law), T2 (Gurland), T3 (Gregory Gr(l), Conj 6.1 false), T10 (Painleve: Conj 7.1 PROVED, 7.2 reduced), T13 (Finch Abel identities PROVED) recorded. In progress: T11 pade positivity (rigorous diagonal proofs running, k*(m)=2m+12..14 law), T12 Stirling CM degrees (table2.log). Backups: results/*/README.md. 
- 23:47 UTC: hurwitz_prob p_4=0.0092838447242981189571 (partial; no closed form). Background: rigorous_diag at m=331, kstar 1209/1509 and stirling n=23..30 still running.
- 00:32 UTC: container restarted, background jobs died; restarted stirling 25..30 (n=23,24 done), rigorous_diag 337..401 (<=335 proved), kstar 1509 (1209: k*=2432=2m+14).
- 01:19 UTC: jobs died again (restart); proved odd m<=341; stirling n=25 done (d_CM=48.1458475899). Relaunched with setsid: rigorous_diag 343..401, kstar 1509, stirling 26..30.
- 02:00 UTC: jobs died at restart again; proved odd m<=345; stirling n=26 d_CM=50.1407770082. Relaunched: rigorous_diag 347..401, kstar 1509, stirling 27..30.
- 02:41 UTC: jobs died again; proved odd m<=347; stirling 27 not finished. Dropped kstar 1509 (1209 suffices). Relaunched rigorous_diag 349..401, stirling 27..30.
- 03:30 UTC: README table + TARGETS statuses updated; jobs relaunched (rigorous_diag 351..401, stirling 27..30).
- 03:31 UTC: jobs died again; proved odd m<=351; stirling n=27 d_CM=52.1360471128. Relaunched rigorous_diag 353..401, stirling 28..30.
- 04:05 UTC: jobs died again; proved odd m<=353. Relaunched rigorous_diag 355..401, stirling 28..30.
- 04:51 UTC: jobs died again; proved odd m<=355. Relaunched rigorous_diag 357..401, stirling 28..30.
- 05:01 UTC: proved odd m<=357; relaunched rigorous_diag 359..401; stirling n=28 never completes between restarts -> final table uses n<=27. verify_all.py running in background (scratchpad log).
- 05:40 UTC: verify_all.py ALL OK; Pade claim extended to odd 3<=m<=359 (179 values, no gaps/failures across logs) in formulas.txt, pade README, main README. rigorous_diag 361..401 still running.
- 06:20 UTC: wrap-up: MORNING_SUMMARY.md finalised (13 items, 9 draft emails, restart note), README/formulas/pade README updated to odd m<=361. Final verify_all run next.
- 06:20 UTC: final verify_all.py ALL OK (0 FAIL). No wake-ups pending after 07:00. Background jobs stopped. Done.
- 08:20 UTC: Phase A done (CITATIONS.md). Findings: (1) 2608.02265 is by Zheng not Samart and ALREADY contains our Samart result -> KNOWN; (2) Finch 2503.00579 corrigendum already explains A/B, I/J identities -> KNOWN; (3) 'Hoffman proved N=1,2,3' was from memory, corrected; (4) Fan's Bjorck/Clark-Laugesen only as quoted; (5) Gasull p_4 does not answer Problem 21. Next: Phase B novelty.
- 08:25 UTC: Phase B agents (4) and Phase C referee agents (7) launched; Phase B part_2 done (novelty: harmonic closed forms and Gr values not found; algorithm standard).
