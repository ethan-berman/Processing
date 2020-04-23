def setup():
    size(400,400)
    
s = 20
def draw():
    clear()
    wave = sin(radians(frameCount))
    rect(5,5,s*wave*10,s*wave)
    
    #fill(0);
    #rect(mouseX,mouseY,s,s)
    #background(420)
    #line(40, 80, mouseX, mouseY );

    
