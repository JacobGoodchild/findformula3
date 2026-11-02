"""Independent numerical check of n_4(81) = 4 m(x^4+y^4+z^4+1+3xyz) by Jensen's formula and a 2-D periodic grid (no analytic continuation involved):
 m(P) = (1/(2 pi)^2) int int sum_{roots z_i of z^4 + 3xy z + (x^4+y^4+1)} log^+ |z_i|  d theta_x d theta_y."""
import numpy as np, sys
def n4_direct(k, N):
    th = (np.arange(N) + 0.5)*2*np.pi/N
    X, Y = np.meshgrid(np.exp(1j*th), np.exp(1j*th), indexing='ij')
    c1 = k*X*Y; c0 = X**4 + Y**4 + 1
    # roots of z^4 + c1 z + c0 = 0 via companion matrices (vectorised)
    shape = c1.shape
    A = np.zeros(shape + (4, 4), dtype=complex)
    A[..., 0, 3] = -c0; A[..., 1, 0] = 1; A[..., 1, 3] = -c1; A[..., 2, 1] = 1; A[..., 3, 2] = 1
    # companion for z^4 + 0 z^3 + 0 z^2 + c1 z + c0 : last column -[c0, c1, 0, 0]
    A = np.zeros(shape + (4, 4), dtype=complex)
    A[..., 1, 0] = 1; A[..., 2, 1] = 1; A[..., 3, 2] = 1
    A[..., 0, 3] = -c0; A[..., 1, 3] = -c1
    ev = np.linalg.eigvals(A)
    val = np.log(np.maximum(np.abs(ev), 1.0)).sum(axis=-1).mean()
    return 4*val
if __name__ == "__main__":
    for k, name in ((3.0, "s=81"), (4.0, "s=256"), (5.0, "s=625")):
        for N in (400, 800, 1600):
            print("n_4 direct, %s (k=%g), grid %d: %.8f" % (name, k, N, n4_direct(k, N)), flush=True)
