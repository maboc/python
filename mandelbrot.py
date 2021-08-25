from graphics import *

def mb(r, i):
    n=0
    rc=0
    r0=r
    i0=i
    
    while ((n<100) and (r*r+i*i<4)):
        rn=r*r-i*i
        imn=2*r*i
        rn=rn+r0
        imn=imn+i0
        n=n+1
        r=rn
        i=imn

#    if(n>=99):
 #       rc=1
  #  else:
   #     rc=0
        
    return n

    
LB=Point(-2,1.5)
RB=Point(1.5,1.5)
LO=Point(-2,0)
RO=Point(1.5,0)
delta=0.005
Ws=600
Hs=600

Wr=RB.getX()-LB.getX()
Hr=LB.getY()-LO.getY()
ax=Ws/Wr
bx=-ax*LB.getX()
ay=-1*(Hs/Hr)
by=-1*ay*LB.getY()

print('ax : ' + str(ax) + '  bx : ' + str(bx))
print('ay : ' + str(ay) + '  by : ' + str(by))


x=LB.getX();

win=GraphWin('Mandelbrot', Ws, Hs)

while x<RB.getX():
    y=LO.getY();
    while y<LB.getY():
        y=y+delta

 #       if(mb(x,y)==1):
        xs=ax*x+bx
        ys=ay*y+by
        v=mb(x,y)
        win.plot(xs,ys, color_rgb(20*v,20*v,20*v))
    x=x+delta
    
