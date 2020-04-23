add_library('minim')
add_library('sound')
song = None
minim = None
test = None
fft = None
bands = None
spectrum = []
def setup():
    global song
    global minim
    global test
    global fft
    global bands
    global spectrum
    minim = Minim(this)
    bands = 512
    fft = FFT(this, bands)
    song = minim.loadSample('final3.wav', 512)
    test = SoundFile(this, 'final3.wav')
    spectrum = [0.0] * bands
    test.play()
    fft.input(test)
    size(500, 500)
    frameRate(30)
    # song.trigger()
class Sky:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = (0, 100, 255)
        self.width = 500
        self.height = 200
        self.clouds = []

    def draw(self):
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.width, self.height)
class Sun:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.color = (245, 255, 0)
        self.corona = (230, 250, 0)
        self.radius = 50
        self.time = 0
        self.timelimit = 360 * 8  # change this factor for rate of rotation

    def rise(self):
        self.time = self.time + 1 % self.timelimit
        mx = 250
        my = 250
        r = 160
        self.x = mx + cos(radians(self.time % 360 - 90)) * r
        self.y = my + sin(radians(self.time % 360 - 90)) * r

    def draw(self):
        self.rise()
        for i in range(12):
            # 12 triangles means 30 degrees per rotation
            # left corner (x1,y1) = cos(theta-90)*leg
            # peak of triangle (x2,y2) = cos(theta)*amp,sin(theta)*amp
            # right corner (x3, y3) = cos(theta+90)*leg,sin(theta+90)*leg
            leg = 15
            peak = 35
            x1 = self.x + cos(radians((i * 30) - 90)) * leg
            y1 = self.y + sin(radians((i * 30) - 90)) * leg
            x2 = self.x + cos(radians(i * 30)) * peak
            y2 = self.y + sin(radians(i * 30)) * peak
            x3 = self.x + cos(radians((i * 30) + 90)) * leg
            y3 = self.y + sin(radians((i * 30) + 90)) * leg
            fill(self.corona[0], self.corona[1], self.corona[2] - 20)
            triangle(x1, y1, x2, y2, x3, y3)
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(self.x, self.y, self.radius, self.radius)
        # draw face
        fill(0)
        ellipse(self.x - 15, self.y - 12, 5, 5)  # left eye
        ellipse(self.x + 15, self.y - 12, 5, 5)  # right eye
        opener = randomGaussian() * 10
        fft.analyze()
        opener = 0
        for i in range(bands):
            opener = opener + fft.spectrum[i]
        opener = (opener / bands) * 200
        print opener
        #opener = song.getBand(20)
        ellipse(self.x, self.y + 5, 40, 20 + opener * 5)  # mouth

class Earth:
    def __init__(self):
        self.x = 0
        self.y = 200
        self.width = 500
        self.height = 300
        self.color = (0, 153, 12)
        self.grass = []
    def draw(self):
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.width, self.height)

sky = Sky()
sun = Sun()
earth = Earth()
def draw():
    background(0)
    sky.draw()

    earth.draw()
    sun.draw()
    #ellipse(mouseX,mouseY, 25, 25)


def ground():
    fill(0, 255, 0)
