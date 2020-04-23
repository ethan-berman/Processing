def split(h):
    h = h + 1
    if(h<20):
        pushMatrix()
        rotate(radians(15))
        translate(0,25)
        ellipse(0,0,25,25)
        split(h)
        popMatrix()
        #other side
        pushMatrix()
        rotate(radians(-15))
        translate(0,25)
        ellipse(0,0,25,25)
        split(h)
        popMatrix()
    else:
        pushMatrix()
        rotate(radians(15))
        translate(0,25)
        ellipse(0,0,25,25)
        popMatrix()
        #other side
        pushMatrix()
        rotate(radians(-15))
        translate(0,25)
        ellipse(0,0,25,25)
        popMatrix()
        
def setup():
    size(640,360)
    background(255)
    stroke(255)
    fill(255)
    translate(width/2,height)
    pushMatrix()
    ellipse(0,0, 25, 25)
    split(0)
'''
def split(h):
    h = h + 1
    if(h<20):
        pushMatrix()
        rotate(radians(15))
        translate(0,25)
        ellipse(0,0,25,25)
        split(h)
        popMatrix()
        #other side
        pushMatrix()
        rotate(radians(-15))
        translate(0,25)
        ellipse(0,0,25,25)
        split(h)
        popMatrix()
    else:
        pushMatrix()
        rotate(radians(15))
        translate(0,25)
        ellipse(0,0,25,25)
        popMatrix()
        #other side
        pushMatrix()
        rotate(radians(-15))
        translate(0,25)
        ellipse(0,0,25,25)
        popMatrix()
        

    def draw():
    background(255)
    ellipse(10,10,20,20)
    stroke(255)
    fill(255)
    translate(width/2,height)
    pushMatrix()
    ellipse(0,0, 25, 25)
    split(0)
'''

        

        
    
