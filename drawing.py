#12th Week Lab Assignment
#Ahmed El-Hussein Ahmed 19106798
#Zeyad Ahmed Samer 20106344

from models.Transformation import Transformation
from models.Point import Point
from models.Graphics import Graphics
from models.Shape import Shape
from models.Color import Color
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

texture = None

x=-260
r=5
x_pos=0
planeXPosition=0
planeYPosition=0
trafficColor=[Color.red,Color.black,Color.black]

circleColor=Color.sunColor
gardenColor=Color.green
skyColor=Color.sunnySkyColor

def displaySpeedLimitSignTexture():

    glEnable(GL_TEXTURE_2D)
    
    glBegin(GL_QUADS)
    
    glColor4f(1, 1, 1, 1)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(640.0, 210.0, 0.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(690, 210.0, 0.0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(690.0, 280.0, 0.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(640.0, 280.0, 0.0)

    
    glEnd()
    glFlush()
    
    glDisable(GL_TEXTURE_2D)


def keyboardFunction(key,x,y):

    global trafficColor,circleColor,gardenColor,skyColor,r
    if key == b'r':
        trafficColor[0] = Color.red  # red
        trafficColor[2]=Color.black
    elif key == b'g':
        
        trafficColor[2] = Color.green  # red
        trafficColor[0]=Color.black

    elif key==b'd':
        circleColor=Color.moonColor
        gardenColor=Color.darkGreen
        skyColor=Color.black

    elif key==b'w':
        circleColor=Color.sunColor
        gardenColor=Color.green
        skyColor=Color.sunnySkyColor
    
    elif key==b'b':
        r=-20

    elif key==b'f':
        r=20    
     
    
    Graphics.redisplay()
            

def displayPlane():
    offset=20


    planeBodyPoints=[Point(400,90-offset),Point(450,70-offset),Point(580,75-offset),Point(580,100-offset)]
    Shape.displayRectangle(points=planeBodyPoints,color=Color.red)            
    planeTailPoints=[Point(550,80-offset),Point(580,50-offset),Point(600,50-offset),Point(580,100-offset)]
    Shape.displayRectangle(points=planeTailPoints,color=Color.red) 
    tailLinePoints=[Point(600,50-offset),Point(610,50-offset)]
    Shape.displayLine(*tailLinePoints,color=Color.red)



def displaySky():
    higherRectanglePoints=[Point(0,0),Point(800,0),Point(800,150),Point(0,150)]
    Shape.displayRectangle(points=higherRectanglePoints,color=skyColor)


def displayGarden():
    gardenRectangularPoints=[Point(0,150),Point(800,150),Point(800,270),Point(0,270)]
    Shape.displayRectangle(points=gardenRectangularPoints,color=gardenColor)

def displayDoors():
    blueBuildingDoorPoints=[Point(35,220),Point(65,220),Point(65,270),Point(35,270)]
    Shape.displayRectangle(points=blueBuildingDoorPoints,color=Color.black)

    brownBuildingDoorPoints=[Point(98+15+10,120+120),Point(168-15,120+120),Point(168-15,270),Point(98+15+10,270)]
    Shape.displayRectangle(points=brownBuildingDoorPoints,color=Color.black)

    redBuildingDoorPoints=[Point((245+15+10),220),Point((245+15+40),220),Point((245+15+40),270),Point((245+15+10),270)]
    Shape.displayRectangle(points=redBuildingDoorPoints,color=Color.black)

    towerDoorPoints=[Point((340+7), 200),Point((340+27),200),Point((340+27),270),Point((340+7),270)]
    Shape.displayRectangle(points=towerDoorPoints,color=Color.black)

    greenBuildingDoorPoints=[Point(410,240),Point(480,240),Point(480,270),Point(410,270)]
    Shape.displayRectangle(points=greenBuildingDoorPoints, color=Color.black)

    lastBuildingDoorPoints=[Point(410+130+5,240),Point(480+130-5,240),Point(480+130-5,270),Point(410+130+5,270)]
    Shape.displayRectangle(points=lastBuildingDoorPoints, color=Color.black)
    
def displayBlueBuildingWindows():
    blueBuildingWindow1Points=[Point(15,188+5),Point(40,188+5),Point(40,208),Point(15,208)]
    blueBuildingWindow2Points=[Point((15+35+5),188+5),Point((40+35+5),188+5),Point((40+35+5),208),Point((15+35+5),208)]

    blueBuildingWindow3Points=[Point(15,158+5),Point(40,158+5),Point(40,178),Point(15,178)]
    blueBuildingWindow4Points=[Point((15+35+5),158+5),Point((40+35+5),158+5),Point((40+35+5),178),Point((15+35+5),178)]

    blueBuildingWindow5Points=[Point(15,128+5),Point(40,128+5),Point(40,148),Point(15,148)]
    blueBuildingWindow6Points=[Point((15+35+5),128+5),Point((40+35+5),128+5),Point((40+35+5),148),Point((15+35+5),148)]
    
    blueBuildingWindow7Points=[Point(15,98+5),Point(40,98+5),Point(40,118),Point(15,118)]
    blueBuildingWindow8Points=[Point((15+35+5),98+5),Point((40+35+5),98+5),Point((40+35+5),118),Point((15+35+5),118)]

    Shape.displayRectangle(points= blueBuildingWindow1Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow2Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow3Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow4Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow5Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow6Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow7Points, color=Color.black)
    Shape.displayRectangle(points= blueBuildingWindow8Points, color=Color.black)

def displayLastBuildingWindows():
    lastBuildingWindow1Points=[Point(525,188+5),Point(550,188+5),Point(550,208),Point(525,208)]
    lastBuildingWindow2Points=[Point(520+40,188+5),Point(545+40,188+5),Point(545+40,208),Point(520+40,208)]
    lastBuildingWindow3Points=[Point(515+80,188+5),Point(540+80,188+5),Point(540+80,208),Point(515+80,208)]
    
    lastBuildingWindow4Points=[Point(525,158+5),Point(550,158+5),Point(550,178),Point(525,178)]
    lastBuildingWindow5Points=[Point(520+40,158+5),Point(545+40,158+5),Point(545+40,178),Point(520+40,178)]
    lastBuildingWindow6Points=[Point(515+80,158+5),Point(540+80,158+5),Point(540+80,178),Point(515+80,178)]


    lastBuildingWindow7Points=[Point(525,128+5),Point(550,128+5),Point(550,148),Point(525,148)]
    lastBuildingWindow8Points=[Point(520+40,128+5),Point(545+40,128+5),Point(545+40,148),Point(520+40,148)]
    lastBuildingWindow9Points=[Point(515+80,128+5),Point(540+80,128+5),Point(540+80,148),Point(515+80,148)]



    lastBuildingWindow10Points=[Point(525,98+5),Point(550,98+5),Point(550,118),Point(525,118)]
    lastBuildingWindow11Points=[Point(520+40,98+5),Point(545+40,98+5),Point(545+40,118),Point(520+40,118)]
    lastBuildingWindow12Points=[Point(515+80,98+5),Point(540+80,98+5),Point(540+80,118),Point(515+80,118)]

    

    Shape.displayRectangle(points=lastBuildingWindow1Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow2Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow3Points, color=Color.black)

    Shape.displayRectangle(points=lastBuildingWindow4Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow5Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow6Points, color=Color.black)

    Shape.displayRectangle(points=lastBuildingWindow7Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow8Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow9Points, color=Color.black)
    
    Shape.displayRectangle(points=lastBuildingWindow10Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow11Points, color=Color.black)
    Shape.displayRectangle(points=lastBuildingWindow12Points, color=Color.black)


def displayBrownBuildingWindows():
    brownBuildingWindow1Points=[Point(103,200),Point(128,200),Point(128,215),Point(103,215)]
    brownBuildingWindow2Points=[Point((103+35+5),200),Point((128+35+5),200),Point((128+35+5),215),Point((103+35+5),215)]

    brownBuildingWindow3Points=[Point(103,170),Point(128,170),Point(128,185),Point(103,185)]
    brownBuildingWindow4Points=[Point((103+35+5),170),Point((128+35+5),170),Point((128+35+5),185),Point((103+35+5),185)]

    brownBuildingWindow5Points=[Point(103,140),Point(128,140),Point(128,155),Point(103,155)]
    brownBuildingWindow6Points=[Point((103+35+5),140),Point((128+35+5),140),Point((128+35+5),155),Point((103+35+5),155)]
    Shape.displayRectangle(points=brownBuildingWindow1Points,color=Color.black)
    Shape.displayRectangle(points=brownBuildingWindow2Points,color=Color.black)

    Shape.displayRectangle(points=brownBuildingWindow3Points,color=Color.black)
    Shape.displayRectangle(points=brownBuildingWindow4Points,color=Color.black)

    Shape.displayRectangle(points=brownBuildingWindow5Points,color=Color.black)
    Shape.displayRectangle(points=brownBuildingWindow6Points,color=Color.black)
    
def displayRedBuildingWindows():
    redBuildingWindow1Points=[Point(255,188+5),Point(280,188+5),Point(280,208),Point(255,208)]
    redBuildingWindow2Points=[Point((250+40+5),188+5),Point((275+40+5),188+5),Point((275+40+5),208),Point((250+40+5),208)]

    redBuildingWindow3Points=[Point(255,158+5),Point(280,158+5),Point(280,178),Point(255,178)]
    redBuildingWindow4Points=[Point((250+40+5),158+5),Point((275+40+5),158+5),Point((275+40+5),178),Point((250+40+5),178)]

    redBuildingWindow5Points=[Point(255,128+5),Point(280,128+5),Point(280,148),Point(255,148)]
    redBuildingWindow6Points=[Point((250+40+5),128+5),Point((275+40+5),128+5),Point((275+40+5),148),Point((250+40+5),148)]

    redBuildingWindow7Points=[Point(255,98+5),Point(280,98+5),Point(280,118),Point(255,118)]
    redBuildingWindow8Points=[Point((250+40+5),98+5),Point((275+40+5),98+5),Point((275+40+5),118),Point((250+40+5),118)]

    Shape.displayRectangle(points=redBuildingWindow1Points,color=Color.black)
    Shape.displayRectangle(points=redBuildingWindow2Points,color=Color.black)
    
    Shape.displayRectangle(points=redBuildingWindow3Points,color=Color.black)
    Shape.displayRectangle(points=redBuildingWindow4Points,color=Color.black)

    Shape.displayRectangle(points=redBuildingWindow5Points,color=Color.black)
    Shape.displayRectangle(points=redBuildingWindow6Points,color=Color.black)

    Shape.displayRectangle(points=redBuildingWindow7Points,color=Color.black)
    Shape.displayRectangle(points=redBuildingWindow8Points,color=Color.black)

def displayTowerWindows():
    towerWindow1Points=[Point((340+5),98+5),Point((340+30),98+5),Point((340+30),150),Point((340+5),150)]

    Shape.displayRectangle(points=towerWindow1Points, color=Color.black)

def displayGreenBuildingWindows():
    greenBuildingWindow1Points=[Point(380,150),Point(405,150),Point(405,180),Point(380,180)]
    greenBuildingWindow2Points=[Point(415,150),Point(440,150),Point(440,180),Point(415,180)]

    greenBuildingWindow3Points=[Point(450,150),Point(475,150),Point(475,180),Point(450,180)]
    greenBuildingWindow4Points=[Point(485,150),Point(510,150),Point(510,180),Point(485,180)]

    greenBuildingWindow5Points=[Point(380,190),Point(405,190),Point(405,220),Point(380,220)]
    greenBuildingWindow6Points=[Point(415,190),Point(440,190),Point(440,220),Point(415,220)]

    greenBuildingWindow7Points=[Point(450,190),Point(475,190),Point(475,220),Point(450,220)]
    greenBuildingWindow8Points=[Point(485,190),Point(510,190),Point(510,220),Point(485,220)]

    Shape.displayRectangle(points=greenBuildingWindow1Points, color=Color.black)
    Shape.displayRectangle(points=greenBuildingWindow2Points, color=Color.black)

    Shape.displayRectangle(points=greenBuildingWindow3Points, color=Color.black)
    Shape.displayRectangle(points=greenBuildingWindow4Points, color=Color.black)

    Shape.displayRectangle(points=greenBuildingWindow5Points, color=Color.black)
    Shape.displayRectangle(points=greenBuildingWindow6Points, color=Color.black)

    Shape.displayRectangle(points=greenBuildingWindow7Points, color=Color.black)
    Shape.displayRectangle(points=greenBuildingWindow8Points, color=Color.black)




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


def displayBlueCar():
   
    carBodyPoints1=[Point(260+x,340),Point(500+x,340),Point(510+x,380),Point(260+x,380)]
    carHeadPoints2=[Point(290+x,340),Point(340+x,280),Point(440+x,280),Point(460+x,340)]
    

    Shape.displayRectangle(points = carBodyPoints1, color=(0,0,1,1))
    Shape.displayRectangle(points = carHeadPoints2, color=(0,0,1,1))
    Shape.displayCircle(centerPoint = Point(340+x,380), radius = 15 , color=Color.black)
    Shape.displayCircle(centerPoint = Point(450+x,380) , radius = 15, color = Color.black)
    windowPoints=[Point(298+x,335),Point( 340+x,285),Point(380+x,285),Point(380+x,335)]


    Shape.displayRectangle(points=windowPoints,color=Color.black)
    windowPoints=[Point(383+x,285),Point( 435+x,285),Point(449+x,335),Point(383+x,335)]
    
    Shape.displayRectangle(points=windowPoints,color=Color.black)
   
def displayRedCar():
    
    carBodyPoints1=[Point(260,340),Point(430,340),Point(430,380),Point(260,380)]
    carHeadPoints2=[Point(260,340),Point(310,280),Point(410,280),Point(430,340)]
    edgePoints=[Point(430,340),Point(465,345),Point(465,380),Point(430,380)]
    Shape.displayRectangle(points=edgePoints,color=(226/255, 48/255, 14/255,1))
    
    Shape.displayRectangle(points = carBodyPoints1, color=(226/255, 48/255, 14/255,1))
    Shape.displayRectangle(points = carHeadPoints2, color=(226/255, 48/255, 14/255,1))
    Shape.displayCircle(centerPoint = Point(310,380), radius = 15 , color=Color.black)
    Shape.displayCircle(centerPoint = Point(410,380) , radius = 15, color = Color.black)
    windowPoints=[Point(268,335),Point( 310,285),Point(350,285),Point(350,335)]

    Shape.displayRectangle(points=windowPoints,color=Color.black)
    windowPoints=[Point(353,285),Point( 405,285),Point(419,335),Point(353,335)]
    
    Shape.displayRectangle(points=windowPoints,color=Color.black)


def displayBus():
    busBodyPoints = [Point(500,320),Point(680,320),Point(680,380),Point(500,380)]
    busHeadPoints = [Point(500,270),Point(670,270),Point(680,320),Point(500,320)]

    window1Points = [Point(510,280),Point(550,280),Point(550,310),Point(510,310)]
    window2Points = [Point(555,280),Point(595,280),Point(595,310),Point(555,310)]
    window3Points = [Point(600,280),Point(640,280),Point(640,310),Point(600,310)]
    window4Points = [Point(645,280),Point(665,280),Point(670,310),Point(645,310)]
    

    Shape.displayRectangle(points=busBodyPoints,color=(1,1,0,1))
    Shape.displayRectangle(points=busHeadPoints,color=(1,1,0,1))

    Shape.displayRectangle(points=window1Points,color=(0,0,0,1))
    Shape.displayRectangle(points=window2Points,color=(0,0,0,1))
    Shape.displayRectangle(points=window3Points,color=(0,0,0,1))
    Shape.displayRectangle(points=window4Points,color=(0,0,0,1))

    Shape.displayCircle(centerPoint = Point(540,380), radius = 15, color = Color.black)
    Shape.displayCircle(centerPoint = Point(640,380), radius = 15, color = Color.black)
    

    
def displayTrafficLight():
    rectangularPoints=[Point(660,140),Point(670,140),Point(670,325),Point(660,325)] 
    Shape.displayRectangle(points=rectangularPoints,color=(230/255,49/255,1/255,255/255))

    #traffic head
    rectangularPoints=[Point(645,120),Point(685,120),Point(685,200),Point(645,200)] 
    Shape.displayRectangle(points=rectangularPoints,color=(174/255,179/255,172/255,255/255))
    
    
    #light circles
    Shape.displayCircle(centerPoint=Point(665,135),radius=11,color=trafficColor[0])
    Shape.displayCircle(centerPoint=Point(665,160),radius=11,color=trafficColor[1])#(253/255,253/255,4/255,255/255)
    Shape.displayCircle(centerPoint=Point(665,185),radius=11,color=trafficColor[2])#(0/255,178/255,0/255,255/255)
   

def displayStreetLight():
    rectangularPoints=[Point(180,230),Point(190,230),Point(190,325),Point(180,325)] 
    Shape.displayRectangle(points=rectangularPoints,color=Color.black)
    headPoints=[Point(180,230),Point(195,220),Point(210,230)]
    Shape.displayTriangle(points=headPoints,color=Color.black)
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
    global x_pos
    Shape.displayCircle(centerPoint=Point(40,40),radius=20,color=circleColor)
  
  

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
        

    if(circleColor==Color.sunColor):
       displayClouds()

    displayBuildings()
    displayTree()
    displayTrafficLight()
    displayStreetLight()
  
    displaySun()
    
   
    displayDoors()
    displayBlueBuildingWindows()
    displayBrownBuildingWindows()
    displayRedBuildingWindows()
    displayTowerWindows()
    displayGreenBuildingWindows()
    displayLastBuildingWindows()
   
    displaySpeedLimitSignTexture()

    Transformation.translate(displayBlueCar,x_pos,0)
    Transformation.translate(displayRedCar,x_pos,0)
    Transformation.translate(displayBus,x_pos,0)
    Transformation.translate(objectDisplay=displayPlane,x_trans=planeXPosition,y_trans=planeYPosition)
    
   
    Graphics.swapBuffer()
  
    
graphics=Graphics()  



def updateCars():
 
    global x_pos

    if(trafficColor[0]!=Color.red):
       x_pos+=r
       if(x_pos>700):
           x_pos=0
   
    Graphics.redisplay()
        
   
def updatePlane():
    global planeXPosition , planeYPosition

    planeXPosition-=4
    
    planeYPosition-=0.5
 

#7asak meday2 ya zeyaaddd


    Graphics.redisplay()      
   
def idleFunction():
    updatePlane()
    updateCars()   



graphics.initializeWindow(display=totalDisplay,idleFunction=idleFunction,keyboardFunction=keyboardFunction)

