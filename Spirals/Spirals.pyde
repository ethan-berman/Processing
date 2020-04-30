add_library('sound')
sun = None
fft = None
bands = None
file = None
def setup():
    global sun, fft, bands, file
    size(500,500)
    background(255)
    sun = Sun(1)
    bands = 512
    fft = FFT(this, bands)
    file = SoundFile(this, 'think.wav')
    file.play()
    fft.input(file)
def draw():
    fft.analyze()
    ave = [0,0,0]
    for i in range(len(fft.spectrum) / 3):
        ave[0] = ave[0] + fft.spectrum[i]
        ave[1] = ave[1] + fft.spectrum[i + (len(fft.spectrum))/3 ]
        ave[2] = ave[2] + fft.spectrum[i + (len(fft.spectrum))/3 * 2]
    ave[0] = ave[0]/(len(fft.spectrum) / 3)
    ave[1] = ave[1]/(len(fft.spectrum) / 3)
    ave[2] = ave[2]/(len(fft.spectrum) / 3)
    print(ave)
    sun.draw(ave)
    

class Sun:
    def __init__(self, ave):
        self.x = 100
        self.y = 100
        self.color = (245, 255, 0)
        self.corona = (230, 250, 0)
        self.mx = 250
        self.my = 250
        self.r = 160
        self.ave = ave
        self.radius = 50
        self.time = 0
        self.timelimit = 360 # change this factor for rate of rotation

    def rise(self):
        self.r = self.r - 0.1
        if self.r < -350:
            self.r = 350
        if self.time == self.timelimit - 1:
            print('i hit big')
            
            #self.mx = self.mx - 1
            #self.my = self.my - 1
        #print(self.time+1) % self.timelimit
        self.time = (self.time + 1) % self.timelimit
        self.x = self.mx + cos(radians(self.time % self.timelimit - 90)) * self.r
        self.y = self.my + sin(radians(self.time % self.timelimit - 90)) * self.r

    def draw(self, ave):
        self.ave = ave
        r = map(ave[0], 0, .001, 0, 255) % 255
        g = map(ave[1], 0, .001, 0, 255) % 255
        b = map(ave[2], 0, .001, 0, 255) % 255
        print(r, g, b)
        self.rise()
        for i in range(12):
            # 12 triangles means 30 degrees per rotation
            # left corner (x1,y1) = cos(theta-90)*leg
            # peak of triangle (x2,y2) = cos(theta)*amp,sin(theta)*amp
            # right corner (x3, y3) = cos(theta+90)*leg,sin(theta+90)*leg
            leg = 15
            peak = 35
            angle1 = 30
            angle2 = 90
            x1 = self.x + cos(radians((i * angle1) - angle2)) * leg
            y1 = self.y + sin(radians((i * angle1) - angle2)) * leg
            x2 = self.x + cos(radians(i * angle1)) * peak
            y2 = self.y + sin(radians(i * angle1)) * peak
            x3 = self.x + cos(radians((i * angle1) + angle2)) * leg
            y3 = self.y + sin(radians((i * angle1) + angle2)) * leg
            noStroke()
            fill(r, g, b)
            triangle(x1, y1, x2, y2, x3, y3)
        noStroke()
        fill(r, g, b)
        ellipse(self.x, self.y, self.radius, self.radius)
        # draw face
        fill(0)
        #ellipse(self.x - 15, self.y - 12, 5, 5)  # left eye
        #ellipse(self.x + 15, self.y - 12, 5, 5)  # right eye
        '''
        opener = randomGaussian() * 10
        fft.analyze()
        opener = 0
        for i in range(bands):
            opener = opener + fft.spectrum[i]
        opener = (opener / bands) * 200
        '''
        #print opener
        #opener = song.getBand(20)
        #ellipse(self.x, self.y + 5, 40, 20)  # mouth
