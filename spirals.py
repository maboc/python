from graphics import *
import numpy as np

def normal(n):
    return 1

def prime(n):
    d=0
    for x in range (1, n+1):
       if n%x == 0:
           d=d+1

    if d>2:
        rc=0
    else:
        rc=1
    return rc
    

ws=1000
m=40000
vf=ws/(2*m)
win=GraphWin('Spirals', ws, ws)
        
for n in range(1, m):
    if prime(n)==1:
        hoek=n%(2*np.pi)
        o=round(np.sin(hoek)*n*vf,0)
        a=round(np.cos(hoek)*n*vf,0)
        win.plot(a+ws/2, o+ws/2, "red")
