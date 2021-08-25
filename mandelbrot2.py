from graphics import *

def mb(r, i):
    n=0
    rc=0
    r0=r
    i0=i
    
    while ((n<767) and (r*r+i*i<4)):
        rn=r*r-i*i
        imn=2*r*i
        rn=rn+r0
        imn=imn+i0
        n=n+1
        r=rn
        i=imn
        
    return n

Xrl=-1
Yrl=-1
Xrr=0
Yrr=1

Xsl=0
Ysl=0
Xsr=600
Ysr=600
    
ax=(Xrl-Xrr)/(-1*Xsr)
bx=Xrl

ay=(Yrl-Yrr)/(-1*Ysr)
by=Yrl

print('ax : ' + str(ax) + '  bx : ' + str(bx))
print('ay : ' + str(ay) + '  by : ' + str(by))

win=GraphWin('Mandelbrot 2', Xsr, Ysr)
MP1=None
MP2=None

xs=0
while xs<Xsr:
    ys=0
    while ys<Ysr:
        xr=ax*xs+bx
        yr=ay*ys+by

        v=mb(xr,yr)
        if (v<=200):
            k1=v
            k2=0
            k3=0
        elif (v<400):
            k1=200
            k2=v-200
            k3=0
        elif (v<600):
            k1=200
            k2=200
            k3=v-400
        else:
            k1=255
            k2=255
            k3=255
            
        win.plot(xs,ys, color_rgb(k1,k2,k3))
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
