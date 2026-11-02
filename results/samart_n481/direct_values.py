import numpy as np, json
from direct_check import n4_direct
out = {}
for k in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9):
    vals = [n4_direct(k, N) for N in (1200, 2400)]
    out[str(k)] = vals
    print(k, vals, flush=True)
json.dump(out, open('direct_values.json', 'w'))
