def setup():
    size(1000,1000)
    background(0)

    
def draw():
    stroke(random(200,250))
    strokeWeight(random(1,5))
    point(random(0,width),random(0,height))
    #saveFrame("####.png")
