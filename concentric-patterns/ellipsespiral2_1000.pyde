angle = 0
sizeAll = 20
yellow = 0
def setup():
 size(1000,1000)
 stroke(1, 87, 155)
 strokeWeight(0.6)
 frameRate(60)
 
def draw():
 global angle,sizeAll,yellow
 translate(width/2,height/2)
 scale(3)
 scale(sizeAll)
 rotate(angle)
 yellow = random(200,255)
 fill(yellow,yellow,0)
 ellipse(5,0,20,20)
 if (sizeAll>0):
  sizeAll = sizeAll - 0.05
 else:
  saveFrame("vangog.png");
  exit();
 angle = angle + 1
