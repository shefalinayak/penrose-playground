from geometry import aToB

# rotationally symmetric tiling with kites in the center
def drawPattern(kite,dart):
    for i in range(0,5):
        shape(kite)
        rotate(2*PI/5)
    
    for i in range(0,5):
        rotate(PI/5)
        translate(100*(1+aToB),0)
        shape(dart)
        translate(-100*(1+aToB),0)
        rotate(PI/5)
        
    tx,ty = 100,0
    for i in range(0,5):
        translate(tx,ty)
        rotate(PI/5)
        shape(kite)
        rotate(-2*PI/5)
        shape(kite)
        rotate(PI/5)
        translate(-tx,-ty)
        rotate(2*PI/5)
    
    tx,ty = 100*(2+aToB),0
    for i in range(0,5):
        translate(tx,ty)
        for j in range(0,5):
            shape(dart)
            rotate(2*PI/5)
        translate(-tx,-ty)
        rotate(2*PI/5)
        
    rotate(-PI/5)
    tx,ty = 100*(2+aToB),0
    for i in range(0,5):
        translate(tx,ty)
        for j in range(0,5):
            shape(kite)
            rotate(2*PI/5)
        translate(-tx,-ty)
        rotate(2*PI/5)
