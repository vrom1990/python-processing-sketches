x = 0
y = 0
def setup():
    global x,y
    x = random(-100,100)
    y = random(-100,100)
    fullScreen()
    background(random(360),100,90)
    frameRate(30)
    colorMode(HSB,360,100,100)
    
def draw():
    global x,y
    translate(width/2,height/2)
    strokeWeight(random(10,100))
    stroke(random(360),100,90)
    point(x,y)
    x = x + random(-50,50)
    y = y + random(-50,50)
    if x >width/2:
        x = width/2
    if y > height/2:
        y = height/2
    if x < - width/2:
        x = -width/2
    if y < -height/2:
        y = -height/2
        
