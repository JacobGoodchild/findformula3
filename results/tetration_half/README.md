# Half-iterates of b^x for b = 4/3, 5/4, 6/5   (S. Finch, arXiv:2509.24918, "Exercises in Iterational Asymptotics IV", Section 1.5)
Finch writes: "It would be good to see the values of T(4/3, 1/2), T(5/4, 1/2) and T(6/5, 1/2) someday." (T(b,x) = tetration; T(b,1/2) = f^{[1/2]}(1) for f(x) = b^x, since T(b,0)=1.)

For 1 < b < e^{1/e} the function f has an attracting fixed point L = L(b) (the smaller root of b^L = L) with multiplier lambda = L ln b in (0,1), and the standard (regular / Koenigs-Szekeres) tetration is
T(b,x) = psi^{-1}(lambda^x psi(1)), psi(y) = lim_n (f^n(y) - L)/lambda^n.  [This is the unique analytic extension with T(b,x) -> L; it joins continuously to Finch's T(e^{1/e},1/2) = 1.2571... as b -> e^{1/e}, see below.]

## Values (verified to 40 digits)
* T(4/3, 1/2) = 1.205837434043095594941839306507112566901...   (L = 1.57167727089..., lambda = 0.452143374516...)
* T(5/4, 1/2) = 1.163595361965008849025943273358436312884...   (L = 1.35220351364..., lambda = 0.301735494133...)
* T(6/5, 1/2) = 1.136262486727128084185300918647426025589...   (L = 1.25773454138..., lambda = 0.229312119617...)

## Checks
* psi(y) = sqrt(lambda) psi(1) holds to 1e-69 (so the half-iterate applied twice gives f(1) = b); recomputing with n -> 1.6 n iterations changes T(4/3,1/2) by 5e-41 (so ~40 digits are certified; the last digits above are beyond that).
* Continuity: T(1.40,1/2) = 1.23718267..., T(1.44,1/2) = 1.25510180..., T(1.4446,1/2) = 1.2571233..., T(1.44466,1/2) = 1.2571496... -> Finch's quoted T(e^{1/e},1/2) = 1.2571...
* Not claimed: closed forms.  Label: VERIFIED (numerical, explicitly requested; no theorem).  Novelty: NOT FOUND (single reading of Finch's note).
