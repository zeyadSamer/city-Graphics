
from time import sleep
from models.Point import Point
from models.Graphics import Graphics
from models.Shape import Shape
from OpenGL.GL import *




x=-260
trafficColor=(1,0,0,1)
graphics=Graphics()

def displaySky():
    higherRectanglePoints=[Point(0,0),Point(800,0),Point(800,150),Point(0,150)]
    Shape.displayRectangle(points=higherRectanglePoints,color=(4/255,228/255,226/255,1))


def displayGarden():
    gardenRectangularPoints=[Point(0,150),Point(800,150),Point(800,270),Point(0,270)]
    Shape.displayRectangle(points=gardenRectangularPoints,color=(0,229/255,3/255,1))

def displayDoors():
    blueBuildingDoorPoints=[Point(35,220),Point(65,220),Point(65,270),Point(35,270)]
    Shape.displayRectangle(points=blueBuildingDoorPoints,color=(0,0,0,0))

    brownBuildingDoorPoints=[Point(98+15+10,120+120),Point(168-15,120+120),Point(168-15,270),Point(98+15+10,270)]
    Shape.displayRectangle(points=brownBuildingDoorPoints,color=(0,0,0,0))

    
def displayBlueBuildingWindows():
    blueBuildingWindow1Points=[Point(15,188+5),Point(40,188+5),Point(40,208),Point(15,208)]
    blueBuildingWindow2Points=[Point((15+35+5),188+5),Point((40+35+5),188+5),Point((40+35+5),208),Point((15+35+5),208)]
    blueBuildingWindow3Points=[Point(15,158+5),Point(40,158+5),Point(40,178),Point(15,178)]
    blueBuildingWindow4Points=[Point((15+35+5),158+5),Point((40+35+5),158+5),Point((40+35+5),178),Point((15+35+5),178)]
    blueBuildingWindow5Points=[Point(15,128+5),Point(40,128+5),Point(40,148),Point(15,148)]
    blueBuildingWindow6Points=[Point((15+35+5),128+5),Point((40+35+5),128+5),Point((40+35+5),148),Point((15+35+5),148)]
    blueBuildingWindow7Points=[Point(15,98+5),Point(40,98+5),Point(40,118),Point(15,118)]
    blueBuildingWindow8Points=[Point((15+35+5),98+5),Point((40+35+5),98+5),Point((40+35+5),118),Point((15+35+5),118)]

    Shape.displayRectangle(points= blueBuildingWindow1Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow2Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow3Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow4Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow5Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow6Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow7Points, color=(0,0,0,0))
    Shape.displayRectangle(points= blueBuildingWindow8Points, color=(0,0,0,0))
    


def displayBuildings():

    blueBuildingPoints=[Point(10,100),Point(90,100),Point(90,270),Point(10,270)]
    Shape.displayRectangle(points=blueBuildingPoints,color=(14/255,53/255,97/255,1))
    depthPoints=[Point(90,100),Point(95,110),Point(95,260),Point(90,270)]
    Shape.displayRectangle(points=depthPoints,color=(14/255,53/255,97/255,1))
    
    brownBuildingPoints=[Point(98,120),Point(168,120),Point(168,270),Point(98,270)]
    Shape.displayRectangle(points=brownBuildingPoints,color=(129/255, 1/255, 65/255,1))


    depthPoints=[Point(168,120),Point(173,130),Point(173,260),Point(168,270)]
    Shape.displayRectangle(points=depthPoints,color=(129/255, 1/255, 65/255,1))


    redBuildingPoints=[Point(245,100),Point(330,100),Point(330,270),Point(245,270)]
    Shape.displayRectangle(points=redBuildingPoints,color=(252/255, 0/255, 1/255,1))
    depthPoints=[Point(330,100),Point(335,110),Point(335,260),Point(330,270)]
    Shape.displayRectangle(points=depthPoints,color=(252/255, 0/255, 1/255,1))


    towerPoints=[Point(340,100),Point(375,100),Point(375,270),Point(340,270)]
    Shape.displayRectangle(points=towerPoints,color=(124/255,1/255,0/255,255/255))


    towerHeadPoints=[Point(340,100),Point(355,80),Point(375,100)]
    Shape.displayTriangle(points=towerHeadPoints,color=(124/255,1/255,0/255,255/255))
    Shape.displayRectangle(points=[Point(355,80),Point(356,80),Point(356,60),Point(356,60)],color=(124/255,1/255,0/255,255/255))

    greenBuildingPoints=[Point(375,130),Point(520,130),Point(520,270),Point(375,270)]
    Shape.displayRectangle(points=greenBuildingPoints,color=(0,254/255,64/255,255/255) )

    lastBuildingPoints=[Point(520,100),Point(620,100),Point(620,270),Point(520,270)]
    Shape.displayRectangle(points=lastBuildingPoints,color=(1/255,65/255,64/255,255/255))
    
    depthPoints=[Point(620,100),Point(635,110),Point(635,260),Point(620,270)]
    Shape.displayRectangle(points=depthPoints,color=(1/255,65/255,64/255,255/255))

def displayCars():
    blueCarBodyPoints1=[Point(260,340),Point(500,340),Point(510,380),Point(260,380)]
    blueCarHeadPoints=[Point(290,340),Point(340,280),Point(440,280),Point(460,340)]
    windowPoints 
    
    Shape.displayRectangle(points = blueCarBodyPoints1, color=(0,0,1,1))
    Shape.displayRectangle(points = blueCarHeadPoints, color=(0,0,1,1))
    Shape.displayCircle(centerPoint = Point(340,380), radius = 15 , color=(0,0,0,0))
    Shape.displayCircle(centerPoint = Point(450,380) , radius = 15, color = (0,0,0,0))
    



def displayBlueCar():
    carBodyPoints1=[Point(260+x,340),Point(500+x,340),Point(510+x,380),Point(260+x,380)]
    carHeadPoints2=[Point(290+x,340),Point(340+x,280),Point(440+x,280),Point(460+x,340)]
    

    Shape.displayRectangle(points = carBodyPoints1, color=(0,0,1,1))
    Shape.displayRectangle(points = carHeadPoints2, color=(0,0,1,1))
    Shape.displayCircle(centerPoint = Point(340+x,380), radius = 15 , color=(0,0,0,0))
    Shape.displayCircle(centerPoint = Point(450+x,380) , radius = 15, color = (0,0,0,0))
    windowPoints=[Point(298+x,335),Point( 340+x,285),Point(380+x,285),Point(380+x,335)]


    Shape.displayRectangle(points=windowPoints,color=(0,0,0,0))
    windowPoints=[Point(383+x,285),Point( 435+x,285),Point(449+x,335),Point(383+x,335)]
    
    Shape.displayRectangle(points=windowPoints,color=(0,0,0,0))

def displayRedCar():
   
    carBodyPoints1=[Point(260,340),Point(430,340),Point(430,380),Point(260,380)]
    carHeadPoints2=[Point(260,340),Point(310,280),Point(410,280),Point(430,340)]
    edgePoints=[Point(430,340),Point(465,345),Point(465,380),Point(430,380)]
    Shape.displayRectangle(points=edgePoints,color=(226/255, 48/255, 14/255,1))
    

    Shape.displayRectangle(points = carBodyPoints1, color=(226/255, 48/255, 14/255,1))
    Shape.displayRectangle(points = carHeadPoints2, color=(226/255, 48/255, 14/255,1))
    Shape.displayCircle(centerPoint = Point(310,380), radius = 15 , color=(0,0,0,0))
    Shape.displayCircle(centerPoint = Point(410,380) , radius = 15, color = (0,0,0,0))
    windowPoints=[Point(268,335),Point( 310,285),Point(350,285),Point(350,335)]


    Shape.displayRectangle(points=windowPoints,color=(0,0,0,0))
    windowPoints=[Point(353,285),Point( 405,285),Point(419,335),Point(353,335)]
    
    Shape.displayRectangle(points=windowPoints,color=(0,0,0,0))



    
def displayTrafficLight():
    rectangularPoints=[Point(660,140),Point(670,140),Point(670,325),Point(660,325)] 
    Shape.displayRectangle(points=rectangularPoints,color=(230/255,49/255,1/255,255/255))

    #traffic head

    rectangularPoints=[Point(645,120),Point(685,120),Point(685,200),Point(645,200)] 
    Shape.displayRectangle(points=rectangularPoints,color=(174/255,179/255,172/255,255/255))
    
    
    #light circles

    Shape.displayCircle(centerPoint=Point(665,135),radius=11,color=(0,0,0,0))
    Shape.displayCircle(centerPoint=Point(665,160),radius=11,color=(253/255,253/255,4/255,255/255))
    Shape.displayCircle(centerPoint=Point(665,185),radius=11,color=(0/255,178/255,0/255,255/255))

def displayStreetLight():
    rectangularPoints=[Point(180,230),Point(190,230),Point(190,325),Point(180,325)] 
    Shape.displayRectangle(points=rectangularPoints,color=(0,0,0,0))
    headPoints=[Point(180,230),Point(195,220),Point(210,230)]
    Shape.displayTriangle(points=headPoints,color=(0,0,0,0))
    lightPoints=[Point(195,230),Point(205,230),Point(205,250),Point(195,250)] 
    Shape.displayRectangle(points=lightPoints,color=(1,1,1,1))


def displayTree():
    rectangularPoints=[Point(215,190),Point(220,190),Point(220,230),Point(215,230)] 
    Shape.displayRectangle(points=rectangularPoints,color=(230/255,49/255,1/255,255/255))
    Shape.displayCircle(centerPoint=Point(210,190),radius=15,color=(2/255,128/255,1/255,255/255))
    Shape.displayCircle(centerPoint=Point(225,190),radius=15,color=(2/255,128/255,1/255,255/255))
    Shape.displayCircle(centerPoint=Point(217,170),radius=15,color=(2/255,128/255,1/255,255/255))
    Shape.displayCircle(centerPoint=Point(217,152),radius=10,color=(2/255,128/255,1/255,255/255))
    

def displayRoad():
    lighterRectangularPoints=[Point(0,270),Point(800,270),Point(800,330),Point(0,330)]
    darkerRectangularPoints=[Point(0,330),Point(800,330),Point(800,400),Point(0,400)]
    Shape.displayRectangle(points=lighterRectangularPoints,color=(126/255,127/255,126/255,1))   
    
    Shape.displayRectangle(points=darkerRectangularPoints,color=(50/255,52/255,50/255,1))


def displaySun():
    Shape.displayCircle(centerPoint=Point(40,40),radius=20,color=(1,1,0,1))


def displayClouds():
    Shape.displayCircle(centerPoint=Point(200,40),radius=10,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(220,40),radius=17,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(240,40),radius=17,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(260,40),radius=17,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(280,40),radius=10,color=(255,255,255,1))


    Shape.displayCircle(centerPoint=Point(100,40),radius=10,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(120,40),radius=17,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(140,40),radius=17,color=(255,255,255,1))
    Shape.displayCircle(centerPoint=Point(160,40),radius=10,color=(255,255,255,1))


def totalDisplay():
    displaySky()
    displayGarden()
    displayRoad()
    displaySun()
    displayClouds()
    displayBuildings()
    displayTree()
    displayTrafficLight()
    displayStreetLight()
  
    
    displayBlueCar()
    displayRedCar()
    displayDoors()
    displayBlueBuildingWindows()

    
    

graphics.initializeWindow(totalDisplay)