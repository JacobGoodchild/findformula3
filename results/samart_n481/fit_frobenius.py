"""Fit the true Mahler measure n_4(s), 0<s<256, to n_4(s) = n0 + sum_j c_j x^{a_j} sum_n t_{j,n} x^n/(a_j+n), x = s/256, a_j = 1/4,1/2,3/4,
where t_{j,n} are the coefficients of 3F2(a_j,a_j,a_j; ...; x).  Data: direct 2-D Jensen integrals (json)."""
import json, numpy as np
from scipy.optimize import lstsq if False else None
