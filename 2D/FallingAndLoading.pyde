def setup():
    size(550,550)

def draw():
    background(40);
    a = map(4*millis()%10000,0,10000,0,TWO_PI);
    
    translate(width/2, height/2-50)
    noStroke()
    e=20
    
    fill(170)  
    for i in range(0,24):
        x= cos(map(i ,0 ,24,0,-TWO_PI))
        y= sin(map(i ,0 ,24,0 ,-TWO_PI))
                    
        b= (TWO_PI/24)*i+a
        c= (b+( 1 * PI )) % TWO_PI
        
        if (0 <= c) and (c < PI/2):
            d = map(c,0,PI/2,e,2*e)
        elif (PI/2 <= c) and (c< PI):
            d= map(c,PI/2,PI,2*e,3*e)
        elif (PI <= c) and(c < 1.50*PI):
            d= map(c,PI,1.5*PI,3*e, 4*e)
        else:
            d = map(c,1.5*PI,TWO_PI,0,e)
        
        ellipse(x*200, y*200+d, 15-15*sin(b), 15-15*sin(b))
          
    
