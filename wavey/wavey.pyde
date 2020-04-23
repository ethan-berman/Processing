num = []
xval = 0
frames = 0
current = 0
def setup():
    size(500,500)
    background(255)
    global current
    current = 0
    global frames
    frames = 200
    xval = 5000
    print(frames)
    for i in range(xval):
        num.append({i:sin(radians(i))})
    
    
def draw():
    global frames
    global current
    background(255)
    current = (current + 1) % frames
    print(current)
    for i in range(len(num)):
        ellipse(num[i].keys()[0] - (current - (frames/2)),200 + (num[i][i] * 100),15,15)
