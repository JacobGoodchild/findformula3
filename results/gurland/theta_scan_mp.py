from mpmath import *
mp.dps=30
def t_of(x,y):
    m=(x+y)/2; d=(x-y)/2
    L=loggamma(1+x)+loggamma(1+y)-2*loggamma(1+m)
    target=L/d**2
    # psi'(1+t)=target, t in [sqrt(xy), m]; psi' decreasing
    return findroot(lambda t: psi(1,1+t)-target, (sqrt(x*y)+m)/2, tol=1e-25)
import itertools
best=(0,None); worst=(9,None)
for m in [0.01,0.1,0.5,1,2,5,20,100]:
    row=[]
    for r in [0.01,0.1,0.3,0.6,0.9,0.99,0.999]:
        d=r*m   # y=m-d>0 requires d<m ; (x=m+d)
        x,y=m+d,m-d
        t=t_of(mpf(x),mpf(y)); g=sqrt(x*y)
        th=(m-t)/(m-g)
        row.append(float(th))
        if th>best[0]: best=(th,(m,r))
        if th<worst[0]: worst=(th,(m,r))
    print(m,[round(v,4) for v in row])
print(best,worst)
