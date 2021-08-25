from graphics import *


def next_gen(old_gen, l):
    return l*old_gen*(1-old_gen)

win_w=1000
win_h=600
l_s=3.4
l_e=4

win=GraphWin('Bifurcation', win_w, win_h)
win.setCoords(l_s, 0,l_e,1)

l=l_s
while l<l_e:

    old_gen=0.1
    for n in range(1, 1000):
        old_gen=next_gen(old_gen, l)
        if n>900:
            #print(str(l) + ' : ' + str(n) + ' : ' +str(old_gen))
            win.plot(l, old_gen)

    l=l+0.001
