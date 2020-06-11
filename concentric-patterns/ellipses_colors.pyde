
x = 2
y = 0


def setup():
  size(800, 800)
  background(100)


def draw():
  global x,y
  translate(width/2,height/2)
  rotate(x)
  fill(random(255),random(255),random(255))
  ellipse(x, y, 100,100)
  x = x + 1
  y = y + 1
