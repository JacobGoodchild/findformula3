# Hurwitz-stability probability p_4 (Gasull, arXiv:2012.02524, Problem 21 context)

p_n = probability that a degree-n polynomial with iid Gaussian coefficients is Hurwitz stable.
Known: p_1=1/2, p_2=1/4, p_3=1/16; p_4, p_5 only by Monte Carlo in the paper.

Result (PARTIAL, numerical, not a proof):
  p_4 = (1/16) * P_cond, with P_cond = P(a4a1/(a3a2) + a3a0/(a2a1) < 1), a_i iid half-normal,
  P_cond = 1 - (2/pi)^2 * Int_0^{pi/2} Int_0^{pi/2} g/sqrt(g^2+c^2 s^2) dphi dt
  (g = cos^2(phi) cos t + sin^2(phi) sin t, c = cos phi, s = sin phi)
  p_4 = 0.009283844724298118957149924  (25 digits; p4_exact.py). Independent check: grid cubature p4.py (0.0092838).
NEGATIVE: PSLQ of the integral against {pi^2, pi log2, pi log(1+sqrt2), pi log(golden), Catalan, pi, log^2 2, ...}
at 50 digits found nothing. The question asked (asymptotics of p_n) is NOT answered.
