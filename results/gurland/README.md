# Gurland's ratio: the open problems in arXiv:2512.07028 (H. Wisniewska), Section 2

G*(x,y) = Gamma(1+x)Gamma(1+y)/Gamma(1+(x+y)/2)^2.  Put m=(x+y)/2, delta=(x-y)/2, g=sqrt(xy).
Paper's Corollary 3: ln G* = delta^2 * zeta(2,1+t) = delta^2 psi'(1+t) for some t=t(x,y) in [g, m].

## Open problems 1 and 2 (convergence of the series S_inf): ANSWER YES for all x,y>0.   Label: PROVED
Let f(z) = ln Gamma(1+m+z). For |z| < 1+m the point 1+m+z has positive real part, so f is analytic in the disc |z|<1+m (its nearest singularity is z=-(1+m)).
Hence its Taylor series at 0 converges to f on that disc. Since |delta| = |x-y|/2 < (x+y)/2 + 1 = 1+m for all x,y>0, we get
ln G*(x,y) = f(delta)+f(-delta)-2f(0) = 2 sum_{k>=1} f^{(2k)}(0) delta^{2k}/(2k)! = sum_k (1/k) delta^{2k} zeta(2k,1+m)
(using f^{(2k)}(0) = psi^{(2k-1)}(1+m) = (2k-1)! zeta(2k,1+m)). So R_{nm}(x,y) -> 0 and ln G* = S_inf for EVERY x,y>0; the radius of convergence in delta is exactly 1+m.
The paper's sufficient condition Q(x,y)=|x-y|/(2(1+sqrt(xy)))<1 is therefore far from necessary.
Numerical sanity check (x=0.01, y=100, i.e. delta/(1+m)=0.98): 3000 terms give agreement to 1e-10 (convergence is geometric with ratio 0.96).

## Open problem 3 (where is t(x,y) in [sqrt(xy), (x+y)/2]?)   Label: PARTIAL
* PROVED local expansion: t = m + (delta^2/12) psi'''(1+m)/psi''(1+m) + O(delta^4)  (from phi(t)=E phi(m+V delta), E V^2=1/6, phi=psi'(1+.)),
  and m-g = delta^2/(2m)+O(delta^4). Hence theta := (m-t)/(m-g) -> (m/6) psi'''(1+m)/(-psi''(1+m)) as delta->0, which tends to 1/3 as m->infinity
  (psi''' ~ 2/z^3, -psi'' ~ 1/z^2). So t cannot be placed closer to g than 1/3 of the way from m: any bound t >= m - c(m-g) needs c >= 1/3 (sharp).
* CONJECTURE (not proved): theta < 1/3 always, i.e. t(x,y) > (x+y+sqrt(xy))/3. Evidence: 20000 random points x,y in [1e-3, 10^3.5], top 200 re-checked with 40-digit mpmath: max theta = 0.33327 < 1/3
  (sup approached as m->infinity, delta->0). A pointwise (in the Laplace variable) comparison fails, so a proof needs more than termwise comparison.
