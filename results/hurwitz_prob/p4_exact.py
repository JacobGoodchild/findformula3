"""Reduction of Gasull's p_4 to a 2-D integral of an algebraic function:
   P(Hurwitz | all a_i>0) = 1 - (2/pi)^2 int_0^{pi/2} int_0^{pi/2} g/sqrt(g^2 + c^2 s^2) dphi dt,   g = cos^2(phi) cos t + sin^2(phi) sin t, c=cos phi, s = sin phi
 (integrate a4,a0 in polar coordinates -> 1-exp(-.), then a2 by a Gaussian integral, then (a1,a3) in polar coordinates where the radius drops out).  p_4 = P/16."""
from mpmath import mp, mpf, quad, cos, sin, sqrt, pi
mp.dps = 25
def integrand(phi, t):
    c, s = cos(phi), sin(phi)
    g = c*c*cos(t) + s*s*sin(t)
    return g/sqrt(g*g + (c*s)**2)
I = quad(lambda t: quad(lambda phi: integrand(phi, t), [0, pi/4, pi/2]), [0, pi/4, pi/2])
P = 1 - (2/pi)**2*I
print("int =", I); print("P(Hurwitz | positive) =", P); print("p_4 =", P/16)
