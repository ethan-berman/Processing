width = 500
height = 500
def setup():
    size(500,500)

def draw():
    background(100)
    drawCircle()
    
def drawCircle():
    noStroke()
    fill(255)
    #ellipse(mouseX, mouseY, 50,50)
    #drawSquare(20)
    for i in range(width):
        ellipse(i, height-(sin(i)*500), 5,5) 

def drawSquare(size):
    noStroke()
    fill(155)
    rect(mouseX,mouseY,size, size)
