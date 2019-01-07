yPos=0
angle = 0

def setup():
    size(450,500,P3D)
   
    
def draw():
    
    translate(50, 250, -300)
    global yPos
    global maxD
    global angle
  
    h = 0
    maxD = 11
    background(32)
    ortho(-width/2, width/2, -height/2, height/2);
    smooth()
    lights()
    noStroke()
    ambientLight(0, 0, 255);
    
    rotateX(-PI/6)
    rotateY(HALF_PI/2)  
    
    for i in range(maxD):        
        for j in range(maxD):
            d = dist(i,j,maxD/2,maxD/2)
            offset = map(d,0,maxD,-PI,PI)            
            yPos = angle + offset
            h= map(sin(yPos), -1, 1, 50, 200)
            box(24, h, 24)
            translate(0, 0, 25)            
        translate(25, 0, -maxD * 25) 
    
    angle -= 0.03
    
