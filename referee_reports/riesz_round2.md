# Referee report, round 2: sec_riesz.tex

## (1) Verdict
COMPLETE MODULO MINOR. I found no fatal or major gap. The proof is correct, given (I1)-(I3) as stated. Everything below is minor.

## (2) Issues
1. (minor) Lemma "elementary inequality", unimodality of G. The text says there is rho_0 in [2,infinity] with G'>=0 on [2,rho_0]. If G'(2)<0 (this can happen, e.g. q near 1), no such rho_0 exists, because the set where G'>=0 is empty. G is then strictly decreasing on [2,infinity). The conclusion G>=min{G(2),G(rho_1)} on [2,rho_1] still holds. Fix: say "G' changes sign at most once, from + to -", or treat the case G'(2)<0 in one line.
2. (minor) Lemma "elementary inequality", hypothesis p^2+q^2>=1. It is redundant. From p^r+q^r>1 and r>=2 with p,q<1, we get p^2+q^2>=p^r+q^r>1. It is only used to get rho_1>=2, which follows directly. Either drop it, or note that it is automatic. The proposition's verification of it via -8 sin(lambda) sin(mu) cos(phi) is unnecessary, though correct.
3. (minor) Notation clashes.
   - mu is the angle (phi+psi)/2 and also the measure mu and mu_N.
   - a,b,c are triangle sides, but the quoted Conjecture 5.6 uses a=2sin(pi/N) and b=2sin(theta_N). The text does flag "a=beta, b=ell" in one place.
   - A,B,C are points, but a,b,c are used for the lengths with a<=b<=c, whereas I1 labels a,b by "the two shorter sides". Fix: rename the angle mu to eta, or the measure to nu.
4. (minor) Branch argument in the monotonicity proposition. "Let psi_2>psi_1 be such that s>0 on [psi_1,psi_2)" is loose. It should say: let psi_2 be the first zero of s after psi_1, if one exists in (psi_1, 2pi-3phi]. Then s(psi_2)=0 and F(psi_2)=z/2<F(psi_1), contradicting F(psi_2)>=F(psi_1). Also say explicitly that the open set {s>0} is therefore an up-set (psi*,end] or [0,end], and that F=z/2 is constant on its complement. The argument is correct. Two points would help:
   - At psi=0, the derivative is only used on (0,psi_2), so no problem arises. Say so.
   - The endpoint psi=2pi-3phi (b=c) is handled by continuity of F, which is fine. For phi=2pi/3 the interval is the single point psi=0, so monotonicity is trivial. State this.
5. (minor) The pair and single-point cases. (I1) is stated for three points only. The text uses U_r(pair)=d^r/2 and U_r(single point)=0 without comment. Add: "maximise 2m(1-m)d^r". Also note that (I2) lets one restrict to subsets with at most 3 points.
6. (minor) Acute case, reduction to the normal form. The following is correct but terse and should be stated:
   - Acute is equivalent to all three arcs <pi.
   - Chord=2sin(arc/2) is increasing for arcs in [0,pi], so the longest side corresponds to the longest arc. This is why "BC longest" becomes 2pi-2phi>=phi+psi.
   - With ties, any longest side may be chosen as BC.
   - After reflection, psi>=0, and psi<phi because A is not equal to B.
   - Placing the arc BC (not containing A) centred at angle pi is the normalisation that gives B=e^{i phi}, C=e^{-i phi}.
7. (minor) The isosceles comparison triple. Add one sentence: an isosceles inscribed triangle is determined up to isometry by its leg length L, because the only two circle points at distance L from the apex are the apex rotated by +-alpha. This makes "congruent to {1,e^{i alpha},e^{-i alpha}}" airtight. Also note alpha=2pi-2phi equals 2(pi-phi) and lies in [2pi/3,pi) exactly because phi lies in (pi/2,2pi/3]. The final step 2*theta_N=pi-pi/N>=2pi/3 for N>=3 should be stated, so that (I3) applies on [alpha,2theta].
8. (minor, honesty/scope) (I1) is quoted for all r>0, and the authors say they did not open the original sources. This is acceptable, as it is declared. I independently confirmed (I1) numerically, comparing with a direct simplex quadratic-program maximisation on random circle triples with r in (2,5): agreement to about 1e-7 relative, which is the optimiser accuracy. I also confirmed the final theorem on the full N-point simplex QP for N=5,7,9 without using I1 or I2. This is evidence only, not proof of the inputs.
9. (cosmetic) The line "lambda>0 for psi<phi, which holds because 2pi-3phi<phi" is correct. In the sentence "0<=lambda<=mu" the lower bound could be written as 0<lambda. The Remark on non-uniqueness is appropriate. The remark about 3|N is correct (equilateral triangle: phi=2pi/3, psi=0).

## (3) What I verified and how
(a) Derivative lemma: re-derived with sympy by differentiating log U(x,y,z) with x=(2sin((phi-psi)/2))^r, y=(2sin((phi+psi)/2))^r, z=(2sin phi)^r directly. It matches the stated formula to about 1e-15 at 5 random (r,phi,psi). The hand derivation of d_x log U = s(z+x-y)/(xD) is also correct, since D - x(4y-2s) = s(2x-s). The identities D>0 and U-z/2 = z s^2/(2D) are correct.
(b) Elementary inequality, checked step by step:
   - G' sign criterion: correct.
   - rho_1 exists and r<rho_1: correct.
   - w=q^{rho_1} lies in (1/2,1).
   - sigma=2/rho_1 lies in (0,1].
   - G(rho_1)=chi(1)-chi(sigma): correct.
   - chi' bound: ((1-w)/w)^sigma >= (1-w)/w because the base is <1 and sigma<=1.
   - E''(u) = -1/u + 1/(1-u), E(0)=E(1/2)=0, so E is concave and E>=0: correct.
   Random test: 33,795 admissible (p,q,r) with r from 2 to about 60; minimum of q^r-p^r-(q^2-p^2) was 4.7e-13, with 0 violations.
(c) R_2 identity: verified by hand using sin^2 mu - sin^2 lambda = sin(psi) sin(phi) and the sum-to-product formulas. Also verified: a^2+b^2-c^2 = -8 sin(lambda) sin(mu) cos(phi). The sign analysis (factorisation with cot(mu)(z+x-y)>0, monotonicity of (1+t)/(1-t)) is correct. Numerical monotonicity of F in psi, for 200 random (r in [2,8], phi in (pi/2,2pi/3]) on 400-point grids: no decrease (min difference 0.0, i.e. flat on the two-point branch).
(d) Branch argument: logically correct (see issue 4); the endpoint psi=0 (a=b, lambda=phi/2>0) and psi=2pi-3phi are covered, and so is phi=2pi/3.
(e) Second conjecture:
   - T_N consists of vertices of P_N for odd N, and the side lengths ell, ell, beta are correct.
   - beta<=ell iff N>=3.
   - The closed form for U_r(T_N) was re-derived algebraically and equals Fan's formula.
   - The masses are positive and sum to 1.
   - The direct energy computation of mu_N is correct (by hand: 2l^{2r}(4l^r-beta^r)/(4l^r-beta^r)^2).
   - Case analysis: a^r+b^r>c^r with r>2 implies a^2+b^2>c^2, hence acute; arcs, ranges phi in (pi/2,2pi/3] and psi in [0,2pi-3phi] are correct; reflection is harmless.
   - alpha=2pi-2phi; L<=ell implies alpha<=pi-pi/N; the use of (I3) is correct.
   - The final sandwich is valid.
   Brute force (all vertex triples, formula I1), N in {5,7,9,11,13}, r in {2.01,2.5,3,5}: the maximum equals Fan's closed form to relative error <=4.4e-16 in all 20 cases. For N=5,7,9 the full simplex QP gave the same value (agreement ~1e-11 relative to 1e-9), so the claim holds without using I1 or I2.
