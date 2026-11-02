# Proof of Conjectures 5.9 and 5.6 in "Riesz capacity ratios with negative exponents" (Q. Fan, arXiv:2609.11186)

**Who asked.** Fan, Sec. 5: Conjecture 5.6 (equilibrium measure of the vertex set of a regular N-gon, N odd, for Riesz exponent r > 2, is supported on the triple {1, e^{i(pi-pi/N)}, e^{i(pi+pi/N)}}, with the stated energy) is reduced to Conjecture 5.9
(a monotonicity statement for the capacity of a 3-point set on the circle), and "if someone in future wants to work on this problem ...". Step 1 (Lemma 5.8) is proved in the paper, Step 2 (Conjecture 5.9) is not.

**Setting.** Energy of a 3-point set with side lengths a, b <= c (Clark-Laugesen, Thm 8 = Lemma 5.7 of the paper): U = c^r/2 if a^r + b^r <= c^r, and U = 2 (abc)^r / (4 (ab)^r - (a^r+b^r-c^r)^2) otherwise. Write x=a^r, y=b^r, z=c^r.
Conjecture 5.9: B, C = e^{+-i phi}, phi in (pi/2, 2pi/3]; A = e^{i psi}, psi in [0, 2pi-3phi] (so BC is the longest side); for r >= 2 the capacity of {A,B,C} is maximal at psi = 2pi - 3phi (AC = BC).

## Theorem 1 (PROVED). For r >= 2, U is nondecreasing in psi on [0, 2pi - 3phi] (constant on the 2-point branch, strictly increasing on the 3-point branch if r > 2); hence Conjecture 5.9.
Proof. Put alpha = (phi-psi)/2, beta = (phi+psi)/2 (alpha <= beta <= pi - phi < pi/2), a = 2 sin alpha, b = 2 sin beta, c = 2 sin phi, so x is decreasing and y increasing in psi, z is constant, and x,y <= z.
On the 3-point branch s := x+y-z > 0, D := 4xy - s^2 >= 4xy - min(x,y)^2 > 0 (s <= min(x,y) because z >= max(x,y)). A direct computation gives  d log U/dx = s (z+x-y)/(x D),  d log U/dy = s (z+y-x)/(y D), and with a'/a = -(1/2) cot alpha, b'/b = (1/2) cot beta:
  d log U / d psi = (s r / (2D)) [ (z+y-x) cot(beta) - (z+x-y) cot(alpha) ].
Since z+x-y > 0, the sign is that of  R_r := (z+y-x)/(z+x-y)  minus  cot(alpha)/cot(beta) = (sin phi + sin psi)/(sin phi - sin psi) = R_2  (use sin(alpha+beta)=sin phi, sin(beta-alpha) = sin psi).
With rho_A = a/c, rho_B = b/c, t_r := rho_B^r - rho_A^r we have R_r = (1+t_r)/(1-t_r), so R_r >= R_2 iff **t_r >= t_2**.   (At r = 2 equality: U is constant, as in the paper.)
**Lemma.** Let 0 < A < B < 1, A^2 + B^2 >= 1, r >= 2 and A^r + B^r > 1.  Then B^r - A^r >= B^2 - A^2.
 Proof. F(r) := B^r - A^r - (B^2 - A^2), F(2) = 0. F'(r) = B^r ln B - A^r ln A >= 0 iff (B/A)^r <= ln A/ln B, and (B/A)^r increases with r, so F increases then decreases: on [2, r_1], r_1 := the root of A^r + B^r = 1 (r_1 >= 2 since A^2+B^2 >= 1),
 F is minimal at an endpoint. So it suffices to show F(r_1) >= 0. Put w = B^{r_1} in (1/2,1), A^{r_1} = 1-w, s = 2/r_1 in (0,1]: F(r_1) = (2w-1) - phi(s) with phi(s) = w^s - (1-w)^s, phi(1) = 2w-1. phi'(s) = (1-w)^s|ln(1-w)| - w^s |ln w| >= 0 for s <= 1, because
 ((1-w)/w)^s >= (1-w)/w and then phi'(s) >= w^s (k(1-w)/k(w) - 1)|ln w|·... where k(u) = -u ln u and k(1-w) >= k(w) for w in [1/2,1) (the function D(u) = k(u)-k(1-u) is concave on (0,1/2] and vanishes at 0 and 1/2). Hence phi(s) <= phi(1), F(r_1) >= 0. []
Apply the lemma with A = rho_A, B = rho_B: A^2 + B^2 - 1 = -(8 sin alpha sin beta cos phi)/c^2·... >= 0 because phi >= pi/2. So d log U/d psi >= 0 on the 3-point branch. On {x+y<=z}, U = z/2, and U > z/2 on the 3-point branch (U - z/2 = (z/2) s^2/D),
so a 3-point stretch can never be followed by a 2-point stretch; U is constant then increasing, continuous, and maximal at psi = 2pi - 3phi. []

## Theorem 2 (PROVED, given Bjorck's theorem that for r > 2 an equilibrium measure is supported on <= 3 points, and Lemma 5.7 as quoted in the paper). Conjecture 5.6 holds for all odd N and r > 2.
Take any 3 vertices of P_N. (i) If the triangle is obtuse (no right triangles for odd N): a^2+b^2 < c^2 implies a^r+b^r < c^r for r >= 2, so U = c^r/2 <= c_max^r/2 where c_max = 2 sin theta_N is the longest chord of P_N; and the conjectured three-point energy is >= c_max^r/2 (U >= z/2 always).
(ii) If acute with longest side BC = 2 sin(k pi/N): rotate so B, C = e^{+-i phi}, phi = pi - (angle at A) in (pi/2, 2pi/3]; by Theorem 1 (A moved along the circle to AC = BC) its energy is <= the energy of the isosceles triangle with legs 2 sin(k pi/N) and apex angle parameter alpha = 2k pi/N in [2pi/3, pi - pi/N];
by Lemma 5.8 of the paper (energy increasing in alpha) this is <= the energy at alpha = pi - pi/N, which is the conjectured triple with energy 2^{r-1} sin^r theta_N / (1 - 2^{r-2} cos^r theta_N). []

## Checks (verify.py)
* the derivative identity for d log U/d psi against finite differences (2000 random points), the key Lemma on 5e5 random points (min slack ~5e-12 as r -> 2), Lemma K on a fine grid,
* Conjecture 5.6 by brute force over all pairs and triples of vertices for odd N in {5,...,31} and r in {2.01, 2.5, 3, 5, 12, 40} (matches the closed form to 1e-9 relative).
Label: PROVED (Theorem 1 unconditionally; Theorem 2 relying on the two cited results). Novelty: NOT FOUND (single reading of the paper; the paper itself says Step 2 is not proved).
