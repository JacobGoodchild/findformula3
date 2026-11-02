# Finch's conjectured identities for Abel functions: proof (arXiv:2503.00579, S. R. Finch, "Abel's Functional Equation and Interrelations")

Finch studies the convex solutions of four Abel equations F(f(x)) = F(x) + 1:
 A: f(x) = x(1-x);   B: f(x) = x/(1+x+x^2);   I: f(x) = x/(1+x-x^2);   J: f(x) = x(1+x)/(1+2x),
normalised through the power-logarithmic asymptotics of the orbits (his constants C(x0)), and conjectures (numerically, 100 digits)
**A(x/(1+x)) = B(x) + 1** and **I(x/(1+x)) = J(x) + 1**, adding: "A formal proof of both identities would be good to see someday."

## Theorem (PROVED).  Both identities hold exactly, for all x in the common domain.
Let h(x) = x/(1+x).
1. *Conjugacy.*  f_A(h(x)) = x/(1+x)^2 = h(g_B(x))  and  f_I(h(x)) = x(1+x)/(1+3x+x^2) = h(f_J(x))  (rational-function identities, checked by sympy in verify.py).
   Hence h maps B-orbits to A-orbits and J-orbits to I-orbits: f_A^n(h(x)) = h(g_B^n(x)), f_I^n(h(x)) = h(f_J^n(x)).
   (This is the reason for the observation in Finch's Sections 2-3 that the numerators of the two orbit sequences coincide: h(p/q) = p/(p+q).)
2. *Normalisation.*  1/h(x) = 1/x + 1.  For the maps above, u_n = 1/x_n satisfies u_{n+1} = u_n + 1 + 1/u_n + O(u_n^{-2}) (A, B) resp. u_{n+1} = u_n + 1 - 1/u_n + O(u_n^{-2}) (I, J), so (de Bruijn; Bencherif-Robin; the
   power-logarithmic series Finch uses) the limits
   A(x) = lim_n [ 1/f_A^n(x) - n - ln n ],  B(x) = lim_n [ 1/g_B^n(x) - n - ln n ],  I(x) = lim_n [ 1/f_I^n(x) - n + ln n ],  J(x) = lim_n [ 1/f_J^n(x) - n + ln n ]
   exist, and they are exactly Finch's constants C(x0) (his expansion x_n ~ 1/n + (-+ ln n - C)/n^2 + ... is equivalent to 1/x_n = n -+ ... ln n + C + o(1); verify.py reproduces his printed A(1/2), B(1), I(1/2), J(1) to 4 digits with N = 4e5 iterations).
3. *The identity.*  1/f_A^n(h(x)) = 1/h(g_B^n(x)) = 1/g_B^n(x) + 1, so
   A(h(x)) = lim [1/g_B^n(x) + 1 - n - ln n] = B(x) + 1.  The same computation with I, J (and +ln n) gives I(h(x)) = J(x) + 1.   QED
Both Abel functions also satisfy the Abel equation, so this is consistent with uniqueness of convex solutions up to constants; the proof above fixes the constant (the "+1").

## Cross-check against Finch's printed digits
A(1/2) = 1.76799378613615... = B(1)+1 (B(1) = 0.76799378613615...);  A(2/3) = A(1/3) = 2.12911826567282... = B(2)+1;  A(4/5) = 3.50782830348353... = B(4)+1;
I(1/2) = 1.64018851423987... = J(1)+1; I(1/3) = 3.48300671252821... = J(1/2)+1; I(2/3) = 0.24236645469421... = J(2)+1; I(3/4) = -0.47037171508299... = J(3)+1. All agree with the identity (all printed digits).

## Remarks
* The statement generalises: if h conjugates two parabolic maps, the Abel (Fatou) coordinates differ by the constant lim [1/h(y) - 1/y] taken along orbits (here 1).
* Not claimed: closed forms for A, B, I, J (Finch notes they are hypertranscendental). Novelty: NOT FOUND elsewhere (the argument is elementary; Finch says the identities are "new" as far as known).
