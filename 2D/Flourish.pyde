def setup():
    size(550,550)

r= 0

def draw():
    global r
    background(40);
    ortho(-width/2, width/2, -height/2, height/2);
    smooth()
    a = map(millis()%10000,0,10000,0,TWO_PI);
    translate(width/2, height/2)
    noStroke()
    bolas = 200
    for i in range (bolas):       
        x = i* cos(i)
        y = i* sin(i)
        distancia = dist(x,y,0,0)
        d = map(distancia,0,500,0,TWO_PI)
        e = sin(a-d)
        f = map(dist(x,y,0,0),0,500,0,TWO_PI)
        
        distancia=map(distancia,-50,500,0,2.5)
        
        anchura = map(e*16,0,16,0,16*(distancia))
         
        ellipse(x+e, y+e, anchura, anchura);
    saveFrame("/frames/####")
