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
