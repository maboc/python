from graphics import *
import random

def process_poi(win, poi):
    P1=Point(0,600)
    P2=Point(300,00)
    P3=Point(600,600)

    random.seed()
    direction = random.randrange(1,4)
    #print(direction)
    
    win.plot(poi.getX(),poi.getY())

    if (direction==1):
        pnx=(poi.getX()+P1.getX())/2
        pny=(poi.getY()+P1.getY())/2
        poi=Point(pnx,pny)
    elif(direction==2):
        pnx=(P2.getX()+poi.getX())/2
        pny=(poi.getY()+P2.getY())/2
        poi=Point(pnx,pny)
    elif(direction==3):
        pnx=(poi.getX()+P3.getX())/2
        pny=(P3.getY()+poi.getY())/2
        poi=Point(pnx,pny)
    return poi

win=GraphWin('Spielerei',600,600)

poi=Point(100,100)

for t in range(1,10000):
    poi=process_poi(win, poi)
