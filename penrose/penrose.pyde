from geometry import *
from tilings import *

NUM_SEGMENTS_A = 10
NUM_SEGMENTS_B = 7


BACKGROUND_COLOR = color(250)
KITE_COLOR = color(0,78,100,200)
DART_COLOR = color(56,134,151,200)
LINEA_COLOR = color(96,140,82)
LINEB_COLOR = color(140,175,105)
DOT_COLOR = color(0,0,0,100)

exportedFileCount = 0;

def exportSVG():
    fileName = str(exportedFileCount)
    while len(fileName) < 4:
        fileName = '0' + fileName
    fileName = 'penrose' + fileName + '.svg'
    polyStyle = 'style="fill:black"'
    
    output = createWriter(fileName)
    output.print('<svg height="300" width="300">\n')
    output.print('<polygon ' + polyStyle + ' class="kite" points="')
    for x,y in kitePoints(axy,bxy):
        output.print(str(x)+','+str(y)+' ')
    output.print('"/>\n')
    output.print('<polygon ' + polyStyle + ' class="dart" points="')
    for x,y in dartPoints(axy,bxy):
        output.print(str(x)+','+str(y)+' ')
    output.print('"/>\n')
    output.print('</svg>')
    output.flush()
    output.close()
    
    print('exported shapes as SVG')
    
def keyPressed():
    if key == 's':
        global exportedFileCount
        exportedFileCount += 1
        exportSVG()

# initializes segments to straight lines
def basicShapes():
    global axy
    axy = [(0,0)]
    segmentLength = 100 / NUM_SEGMENTS_A
    for i in range(0,NUM_SEGMENTS_A-1):
        axy.append((segmentLength*(i+1),0))
    axy.append((100,0))
    global bxy
    bxy = [(0,0)]
    segmentLength = -(100 * aToB) / NUM_SEGMENTS_B
    for i in range(0,NUM_SEGMENTS_B-1):
        bxy.append((segmentLength*(i+1),0))
    bxy.append((-100*aToB,0))

# initializes segments to have small spiky things
def spikyShapes():
    global axy
    axy = [(0,0),(22,0),(26,8),(30,-5),(34,3),(38,0),(100,0)]
    global bxy
    bxy = [(0,0),(-10,0),(-13,5),(-17,5),(-20,0),(-100*aToB,0)]

def updateTiles():
    # reconstruct kite primitive
    global kite
    kite = createShape()
    kite.beginShape()
    kite.fill(KITE_COLOR)
    kite.stroke(BACKGROUND_COLOR)
    kite.strokeWeight(1)
    for x,y in kitePoints(axy,bxy):
        kite.vertex(x,y)
    kite.endShape(CLOSE)

    # reconstruct dart primitive
    global dart
    dart = createShape()
    dart.beginShape()
    dart.fill(DART_COLOR)
    dart.stroke(BACKGROUND_COLOR)
    dart.strokeWeight(1)
    for x,y in dartPoints(axy,bxy):
        dart.vertex(x,y)
    dart.endShape(CLOSE)
    
dotIndex = -1
dotOnA = False

DOT_RADIUS = 5
LINE_SCALE = 2
LINE_OFFSET_X = 100
LINE_OFFSET_Y = 60

# returns True if point (x,y) is within dot at (cx,cy) 
def onDot(cx,cy,x,y):
    distX = (cx - x)*(cx - x)
    distY = (cy - y)*(cy - y)
    return distX+distY <= DOT_RADIUS*DOT_RADIUS

# transforms mouse coordinates to match transformation on edges
def mouseToEdgeSpace(mouseX,mouseY):
    trueX = mouseX/LINE_SCALE - LINE_OFFSET_X
    trueY = mouseY/LINE_SCALE - LINE_OFFSET_Y
    return (trueX,trueY)

# figures out if an editable dot was clicked
def mousePressed():
    # mouse coordinates transformed
    trueX,trueY = mouseToEdgeSpace(mouseX,mouseY)
    # figure out which dot was clicked (if any)
    for i,(ax,ay) in enumerate(axy[1:-1]):
        if onDot(ax,ay,trueX,trueY):
            global dotIndex,dotOnA
            dotIndex = i+1
            dotOnA = True
            break
    if dotIndex < 0:
        for i,(bx,by) in enumerate(bxy[1:-1]):
            if onDot(bx,by,trueX,trueY):
                global dotIndex,dotOnA
                dotIndex = i+1
                dotOnA = False
                break

def mouseReleased():
    global dotIndex
    dotIndex = -1
    
# if editable dot was clicked, updates geometry
def mouseDragged():
    # mouse coordinates transformed
    trueX,trueY = mouseToEdgeSpace(mouseX,mouseY)
    if dotIndex >= 0:
        if dotOnA:
            global axy
            x,y = axy[dotIndex]
            axy[dotIndex] = (trueX,trueY)
        else:
            global bxy
            x,y = axy[dotIndex]
            bxy[dotIndex] = (trueX,trueY)
        updateTiles()

def setup():
    size(800,800)
    background(200)
    pixelDensity(displayDensity())
    smooth()
    # initialize kite and dart
    basicShapes()
    updateTiles()
    
def draw():
    background(BACKGROUND_COLOR)
    
    # editable lines
    scale(LINE_SCALE)
    translate(LINE_OFFSET_X,LINE_OFFSET_Y)
    strokeWeight(2)
    stroke(LINEA_COLOR)
    drawEdge(axy)
    stroke(LINEB_COLOR)
    drawEdge(bxy)
    fill(DOT_COLOR)
    drawEditPoints(axy,DOT_RADIUS)
    drawEditPoints(bxy,DOT_RADIUS)
    
    # kite and dart
    translate(200,0)
    scale(0.75)
    shape(kite)
    shape(dart)
    
    # tiling pattern
    scale(0.5)
    translate(-250,500)
    drawPattern(kite,dart)
