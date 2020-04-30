add_library('minim')
add_library('sound')
song = None
minim = None
test = None
fft = None
bands = None
spectrum = []
earth = None
sky = None
sun = None
def setup():
    size(500, 500)
    background(255)
    global song
    global minim
    global test
    global fft
    global bands
    global spectrum
    global earth, sky, sun
    sky = Sky()
    sun = Sun(0)
    earth = Earth(0)
    
    minim = Minim(this)
    bands = 512
    fft = FFT(this, bands)
    test = SoundFile(this, 'angels.wav')
    spectrum = [0.0] * bands
    test.play()
    fft.input(test)
    #draw components
    sky.draw()
    sun.draw(0)
    earth.draw(4, 0)
    frameRate(30)
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
    def __init__(self, ave):
        self.x = 100
        self.y = 100
        self.color = (245, 255, 0)
        self.corona = (230, 250, 0)
        self.ave = ave
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

    def draw(self, ave):
        self.ave = ave
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
            stroke(0)
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
        #print opener
        #opener = song.getBand(20)
        ellipse(self.x, self.y + 5, 40, 20 + self.ave * 200)  # mouth

class Earth:
    def __init__(self, ave):
        self.x = 0
        self.y = 200
        self.width = 500
        self.height = 300
        self.ave = ave
        self.color = (0, 153, 12)
        self.grass = [[0 for x in range(self.width)] for y in range(self.height)]
        #[0] * (self.width * self.height)
        for i in range(len(self.grass)):
            for j in range(len(self.grass[i])):

                self.grass[i][j] = int(map(noise(i*self.width+j),0,1,120,180))
        #for i in range(len(self.grass)):
            #self.grass[i] = int(map(noise(i), 0, 1, 120, 180))
        print(self.width * self.height)
    def grassNoise(self, pixel):
        counter = 0
        for i in range(self.width/pixel):
            for j in range(self.height/pixel):
                g = self.grass[i][j] * self.ave
                fill(self.color[0], g, self.color[2])
                noStroke()
                rect(self.x + i * pixel, self.y + j * pixel, pixel, pixel)
                counter = counter + 1
        fill(0)
    def draw(self, pixel, ave):
        self.ave = ave
        self.grassNoise(pixel)
def draw():
    fft.analyze()
    ave = 0
    for i in range(bands):
        ave = ave + fft.spectrum[i]
    ave = (ave / bands) * 200
    #Order is essential
    sky.draw()
    sun.draw(ave)
    earth.draw(4, ave)
    #ellipse(mouseX,mouseY, 25, 25)


def ground():
    fill(0, 255, 0)
