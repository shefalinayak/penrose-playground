# HELPFUL CONSTANTS
aToB = sin(PI/5) / sin(2*PI/5)


# DRAWING
def drawEdge(lxy):
    for i in range(0,len(lxy)-1):
        x1,y1 = lxy[i]
        x2,y2 = lxy[i+1]
        line(x1,y1,x2,y2)
    
def drawEditPoints(lxy,r):
    noStroke()
    for x,y in lxy[1:-1]:
        ellipse(x,y,r,r)
        
def drawEditPointsPlus(lxy,ptTypes,r):
    pass

# TRANSFORMATIONS
def rotatePoint(x,y,theta):
    return (x*cos(theta)-y*sin(theta),x*sin(theta)+y*cos(theta))

def rotateEdge(lxy,theta):
    return [rotatePoint(x,y,theta) for x,y in lxy]

def translateEdge(lxy,dx,dy):
    return [(x+dx,y+dy) for x,y in lxy]

# SHAPE CONSTRUCTION
def kitePoints(axy,bxy):
    e1 = rotateEdge(axy,-PI/5)
    e2 = list(reversed(translateEdge(rotateEdge(bxy,2*PI/5),100,0)))
    e3 = translateEdge(rotateEdge(bxy,-2*PI/5),100,0)
    e4 = list(reversed(rotateEdge(axy,PI/5)))
    return e1[:-1] + e2[:-1] + e3[:-1] + e4[:-1]

def dartPoints(axy,bxy):
    axy2 = list(reversed(translateEdge(axy,-100,0)))
    bxy2 = list(reversed(translateEdge(bxy,100*aToB,0)))
    e1 = rotateEdge(axy2,PI/5)
    e2 = list(reversed(translateEdge(rotateEdge(bxy2,-3*PI/5),-100*aToB,0)))
    e3 = translateEdge(rotateEdge(bxy2,3*PI/5),-100*aToB,0)
    e4 = list(reversed(rotateEdge(axy2,-PI/5)))
    return e1[:-1] + e2[:-1] + e3[:-1] + e4[:-1]
