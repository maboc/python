from graphics import *

def mb(r, i, cr, ci):
    n=0
    rc=0
    r0=r
    i0=i
    
    while ((n<50) and (r*r+i*i<4)):
        rn=r*r-i*i
        imn=2*r*i
        rn=rn+cr
        imn=imn+ci
        n=n+1
        r=rn
        i=imn
        
    return n

Xrl=-2
Yrl=-2
Xrr=2
Yrr=2

Xsl=0
Ysl=0
Xsr=400
Ysr=400
    
ax=(Xrl-Xrr)/(-1*Xsr)
bx=Xrl

ay=(Yrl-Yrr)/(-1*Ysr)
by=Yrl

print('ax : ' + str(ax) + '  bx : ' + str(bx))
print('ay : ' + str(ay) + '  by : ' + str(by))

win=GraphWin('Julia Sets', Xsr, Ysr)
MP1=None
MP2=None

rc=0
ic=0.75
xs=0
while xs<Xsr:
    ys=0
    while ys<Ysr:
        xr=ax*xs+bx
        yr=ay*ys+by

        v=mb(xr,yr,rc,ic)
            
        win.plot(xs,ys, color_rgb(v*5,255-v*5,v*5))
        ys=ys+1
    xs=xs+1
    MP=win.checkMouse()
    if (MP is not None):
        if MP1 is None:
            MP1=MP
        else:
            MP2=MP

            print(str(MP1.getX()) + ' : ' +str(MP1.getY()))
            print(str(MP2.getX()) + ' : ' +str(MP2.getY()))

            Xrl=ax*MP1.getX()+bx
            Yrl=ay*MP1.getY()+by
            Xrr=ax*MP2.getX()+bx
            Yrr=ay*MP2.getY()+by
            
            ax=(Xrl-Xrr)/(-1*Xsr)
            bx=Xrl

            ay=(Yrl-Yrr)/(-1*Ysr)
            by=Yrl

            print('ax : ' + str(ax) + '  bx : ' + str(bx))
            print('ay : ' + str(ay) + '  by : ' + str(by))
            print('Xrl : '+str(Xrl) + '     Xrr : '+ str(Xrr))
            print('Yrl : '+str(Yrl) + '     Yrr : '+ str(Yrr))

            MP1=None
            MP2=None
            xs=0
            ys=0
