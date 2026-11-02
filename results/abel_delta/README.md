# Finch's "delta conjectures" for Abel's equation: proof (arXiv:2506.07625, S. R. Finch, "Half-Iterates and Delta Conjectures")

**Who asked.** Finch compares two numerical solutions of Abel's equation g(theta(x)) = g(x) + 1 for theta(x) = x + c_1 x^{tau+1} + c_2 x^{2 tau+1} + ..., c_1 = gamma < 0:
the Ecalle-Jagy (EJ) one, g_EJ = A x^{-tau} + a ln x + (series in x^tau with NO constant term), and the Mavecha-Laohakosol (ML) "principal" one g~, defined directly from the orbit x_n = theta^n(x_0).
Their difference delta = g_EJ - g~ is a constant; the paper's aim is "filling this gap in our knowledge" with an exact expression, conjectures delta13 = -(3/4) ln 2, delta15, delta16 = -(2/3) ln 3, delta(k) = -((k+1)/(2k)) ln k,
delta(rho), delta17 = -(5/9) ln 6, and in Addenda II-III the general formula delta = [(tau+1)/(2 tau) + rho/(tau sigma^2)] ln(1/(tau sigma)) for theta = x(1 - sigma x^tau - rho x^{2 tau}), plus transcendental cases
(ln(1+x), x e^{-x}, x/(1+x^2), sin x, Fresnel cosine). "Formal proofs would be good to see someday."

## Theorem (PROVED).  Let kappa = -tau*gamma > 0 and a = (tau+1)/2 - c_2/gamma^2.
1. The EJ solution has A = 1/kappa and ln-coefficient a.
2. The ML limit  g~(x_0) = -tau * lim_{n->inf} n^{1+1/tau} [ kappa^{1/tau} x_n - n^{-1/tau} + (a/tau^2) ln(n) n^{-1-1/tau} ]  exists and  g~ = g_EJ + (a/tau) ln(kappa).
3. Hence **delta = g_EJ - g~ = -(a/tau) ln(kappa) = [ (tau+1)/(2 tau) - c_2/(tau gamma^2) ] ln(1/(tau |gamma|)).**
With theta = x(1 - sigma x^tau - rho x^{2 tau}) this is exactly Finch's Addendum III formula (c_2 = -rho, gamma = -sigma); delta depends only on tau, c_1, c_2, as he observed.
(The ML formula in item 2 is, for each of Finch's examples, the displayed formula of the paper: e.g. tau=2, kappa=2, a=3/2: g~13 = -2 lim n^{3/2}( sqrt2 x_n - n^{-1/2} + (3/8) ln n n^{-3/2} ).)

## Proof
*Item 1.* Put eps = x^tau, theta = x(1 + gamma eps + c eps^2 + ...). Then theta^{-tau} = eps^{-1}[1 - tau gamma eps + (tau(tau+1)/2 gamma^2 - tau c) eps^2 + ...] and ln(theta/x) = gamma eps + O(eps^2).
In g(theta) - g(x) = 1 with g = A x^{-tau} + a ln x + b_1 x^tau + ...: the eps^0 term gives -A tau gamma = 1; the eps^1 term gives A (tau(tau+1)/2 gamma^2 - tau c) + a gamma = 0, i.e. a = (tau+1)/2 - c/gamma^2 (the b_m terms enter only at eps^2 and higher). (verify.py re-derives this with sympy for 17 maps.)
*Item 2.* Let g be any solution with g(x) = A x^{-tau} + a ln x + beta + O(x^tau) (beta = 0 for EJ).  g(x_n) = g(x_0) + n gives  x_n^{-tau} = kappa[ n + g_0 - beta - a ln x_n ] + o(1) with ln x_n = -(1/tau) ln(kappa n) + o(1), so
x_n^{-tau} = kappa n + kappa(g_0 - beta) + (kappa a/tau) ln(kappa n) + o(1), and  kappa^{1/tau} x_n = n^{-1/tau}[1 - ( g_0 - beta + (a/tau) ln kappa + (a/tau) ln n )/(tau n) + O(ln^2 n / n^2)].
Hence the bracket in item 2 equals -(g_0 - beta + (a/tau) ln kappa) n^{-1-1/tau}/tau + o(n^{-1-1/tau}); multiplying by -tau n^{1+1/tau} gives g~ = g_0 - beta + (a/tau) ln kappa.  QED
(The existence of the expansion g = A x^{-tau} + a ln x + beta + O(x^tau) for an actual solution is the standard fixed-point/Fatou-coordinate theory used by EJ and ML: de Bruijn, Ecalle, Kuczma-Choczewski-Ger.)

## Checks (`verify.py`)
* The formula reproduces every delta in the paper: theta13, theta14 (0), theta15, theta16, theta17, delta(k) for x(1-x^k) and x(1-x)^k, delta(rho), ln(1+x) (-(1/3) ln 2), x e^{-x} (0), x/(1+x^2) (-(1/4) ln 2), sin x ((3/5) ln 3),
  Fresnel cosine ((55/108) ln(10/pi^2)), x(1-x)^3 and x(1-6x+16x^2) (the "shared delta" observations of Addendum II).
* Independent high-precision check: Finch's printed 50-digit values give g_EJ(1/2) - g~(1/2) = -0.519860385419958982062924091094... = -(3/4) ln 2 to 30 printed digits, and the same at x_0 = 1/sqrt(3).
* Direct orbit evaluation of the ML limit for theta16 at x_0 = 1/2 (N = 10^6) gives 1.11283 vs the printed 1.112930778... (limit converges like ln^2 N / N).
Novelty: NOT FOUND (a single reading; the argument is elementary asymptotics). Finch writes "[Formal proofs] would be good to see someday".
