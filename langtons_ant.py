from graphics import *
import numpy as np


a_d=0
a_x=50
a_y=50
f_w=100
f_h=100
w_w=4*f_w
w_h=4*f_h
n=0

print ("Langton's Ant");

field = np.zeros(shape=(f_w,f_h))
#fill the field with zeros (white)
for w in range(0,f_w):
    for h in range(0, f_h):
        field[w][h]=0

win=GraphWin("Langton's Ant",w_w,w_h)

while(a_x>0 and a_x < f_w and a_y>0 and a_y<f_h):
#     print(n)
    
    cur_col=field[a_x][a_y]
    if cur_col==0:
        a_d=(a_d-90)%360
    else:
        a_d=(a_d+90)%360

    if(cur_col==0):
        new_col=1
        field[a_x][a_y]=1
    else:
        new_col=0
        field[a_x][a_y]=0

    rec=Rectangle(Point(a_x*4, a_y*4), Point(a_x*4+4, a_y*4+4))
    if(new_col==0):
        rec.setFill("White")
    else:
        rec.setFill("Black")
    rec.draw(win)

    if(a_d==0):
        a_y=a_y+1
    elif(a_d==90):
        a_x=a_x+1
    elif(a_d==180):
        a_y=a_y-1
    elif(a_d==270):
        a_x=a_x-1

    n=n+1


