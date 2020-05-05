add_library('sound')
fft = None
bands = None
file = None
x = 0
y = 0
dir = None
pixel = 1
def setup():
    global fft, bands, file, x, y, dir, pixel
    pixel = 4
    x = 0
    y = 0
    size(500,500)
    background(255)
    frameRate(60)
    dir = 1
    bands = 512
    fft = FFT(this, bands)
    file = SoundFile(this, 'think.wav')
    file.play()
    fft.input(file)
def draw():
    global ave, x, y, dir, pixel
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
    #to the right
    design(ave, x, y, pixel)
    if x == width and dir == 1:
        y = y + 1*pixel
        dir = -1
    elif x == 0 and dir == -1:
        y = y + 1*pixel
        dir = 1
    x = x + dir * pixel
def design(ave, x, y, pixel):
    r = map(ave[0], 0, .001, 0, 255) % 255
    g = map(ave[1], 0, .001, 0, 255) % 255
    b = map(ave[2], 0, .001, 0, 255) % 255
    noStroke()
    fill(r, g, b)
    rect(x,y, pixel, pixel)
