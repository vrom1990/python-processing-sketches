angle = 0
sz = 0
def setup():
    size(1080,1080)
    rectMode(CENTER)
    noFill()

def draw():
    global angle, sz
    translate(width/2,height/2)
    rotate(angle)
    square(0,0,sz)
    angle+=1
    sz+=1
