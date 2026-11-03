#!/usr/bin/env python3
"""Re-run the headline checks for every recorded result. Prints OK/FAIL lines; exit code 1 if any FAIL.
Results kept in the paper: harmonic_products, gregory, abel_delta, tetration_half, pade_positivity, stirling_cm, finch_c2, riesz_triangle, gurland.
Results found but already known (not claimed): painleve_series, abel_finch, t_values."""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
checks = [("results/harmonic_products", "verify.py"), ("results/gregory", "verify.py"), ("results/painleve_series", "verify.py"), ("results/abel_finch", "verify.py"), ("results/abel_delta", "verify.py"), ("results/tetration_half", "verify.py"), ("results/pade_positivity", "verify.py"), ("results/stirling_cm", "verify.py"), ("results/finch_c2", "verify.py"), ("results/riesz_triangle", "verify.py"), ("results/t_values", "verify.py"), ("results/gurland", "verify.py")]
extra = os.path.join(here, "results")
fail = False
for d, script in checks:
    r = subprocess.run([sys.executable, script], cwd=os.path.join(here, d), capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        fail = True; sys.stdout.write(r.stderr[-2000:])
print("ALL OK" if not fail else "SOME FAILED")
sys.exit(1 if fail else 0)
