"""Independent check of d_CM(R_2) ~ 2.8667042552: test (-1)^j d^j/dx^j [x^rho f(x)] >= 0 directly using polygamma (Leibniz), at 120-digit precision.
f = R_2(x) = (+1) * [ log Gamma(x) - (x-1/2)log x + x - log(2pi)/2 - B2/(2x) - B4/(12 x^3) ]  (sign (-1)^2 = +).  CM, positive."""
import sys
from mpmath import mp, mpf, psi, bernoulli, factorial, binomial, log, pi, rf
mp.dps = 130
def fder(i, x, n=2):
    """i-th derivative of R_n(x) (sign (-1)^n)"""
    if i == 0:
        v = mp.loggamma(x) - (x - mpf(1)/2)*log(x) + x - log(2*pi)/2
        for k in range(1, n+1):
            v -= bernoulli(2*k)/(2*k*(2*k-1)*x**(2*k-1))
        return (-1)**n * v
    if i == 1:
        v = psi(0, x) - log(x) + 1/(2*x) - 0
        for k in range(1, n+1):
            v += bernoulli(2*k)/(2*k*x**(2*k)) * 1      # d/dx of -B/(2k(2k-1)) x^{-(2k-1)} = + B/(2k) x^{-2k}
        # careful: derivative of -(x-1/2)log x + x -> -log x + 1/(2x) ; of loggamma -> psi
        return (-1)**n * (v)
    v = psi(i-1, x) - ((-1)**(i-2))*factorial(i-2)/x**(i-1) * 1 + ((-1)**(i-1))*factorial(i-1)/(2*x**i) * 0
    # d^i[(x-1/2) log x] = (-1)^(i-2) (i-2)! x^{-(i-1)} * 1 ... compute generally below
    return None
def Rn_deriv(i, x, n):
    """i-th derivative of the (unsigned) remainder via explicit formulas"""
    if i == 0:
        v = mp.loggamma(x) - (x - mpf(1)/2)*log(x) + x - log(2*pi)/2
        for k in range(1, n+1): v -= bernoulli(2*k)/(2*k*(2*k-1)*x**(2*k-1))
        return v
    # d^i loggamma = psi^{(i-1)}
    v = psi(i-1, x)
    # d^i [-(x-1/2) log x] : first derivative -log x - 1 + 1/(2x); then standard
    if i == 1:
        v += -log(x) - 1 + 1/(2*x) + 1
    else:
        # d^i of -(x-1/2)log x = -[ x log x ]^{(i)} + (1/2)[log x]^{(i)}
        # [x log x]^{(1)} = log x + 1 ; [x log x]^{(i)} = (-1)^i (i-2)! x^{1-i} for i>=2 ; [log x]^{(i)} = (-1)^{i-1}(i-1)! x^{-i}
        v += -((-1)**i)*factorial(i-2)*x**(1-i) + mpf(1)/2*((-1)**(i-1))*factorial(i-1)*x**(-i)
    for k in range(1, n+1):
        e = 2*k - 1
        v -= bernoulli(2*k)/(2*k*(2*k-1)) * ((-1)**i) * rf(e, i) * x**(-e-i)
    return v
def deriv_x_rho_f(j, x, rho, n):
    s = mpf(0)
    for i in range(j+1):
        # d^{j-i}[x^rho] = rho(rho-1)...(rho-(j-i)+1) x^{rho-(j-i)}
        c = mpf(1)
        for r in range(j-i): c *= (rho - r)
        s += binomial(j, i) * c * x**(rho - (j-i)) * (-1)**n * Rn_deriv(i, x, n)
    return s
if __name__ == "__main__":
    rho0 = mpf(sys.argv[1]); n = int(sys.argv[2])
    for delta in (mpf(-3)/1000, mpf(3)/1000):
        rho = rho0 + delta
        worst = None
        for j in (8, 12, 16, 20, 24, 30):
            for tstar in (6, 9, 11.5, 14, 18):
                x = mpf(j)/tstar
                v = (-1)**j * deriv_x_rho_f(j, x, rho, n)
                # normalise by magnitude of a typical term to compare sign robustly
                if worst is None or v < worst[0]: worst = (v, j, x)
        print("rho = %s : most negative (-1)^j d^j[x^rho f] = %s at j=%d x=%s" % (mp.nstr(rho, 10), mp.nstr(worst[0], 5), worst[1], mp.nstr(worst[2], 5)))
