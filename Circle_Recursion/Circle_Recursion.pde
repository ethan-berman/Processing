import processing.sound.*;
SoundFile file;
FFT fft;
int bands = 512;
float[] spectrum = new float[bands];
int frames;
void setup() {
  size(640,360);
  frames = 0;
  fft = new FFT(this, bands);
  file = new SoundFile(this, "final3.wav");
  file.play();
  fft.input(file);
}
 
void draw() {
  background(0);
  fft.analyze();
  float factor = 0.0;
  frames += 1;
  for(int i = 0; i < bands; i++){
    factor += fft.spectrum[i];
  }
  factor /= bands;
  print(factor + " ");
  //map(factor, 0.0001, 0.01, 1000,10000)
  drawCircle(width/2,height/2,500 + frames);
}
 
void drawCircle(float x, float y, float radius) {
  stroke(0);
  fill(255);
  ellipse(x, y, radius, radius);
  if(radius > 2) {
    drawCircle(x + radius/2, y, radius/2);
    drawCircle(x - radius/2, y, radius/2);
    drawCircle(x, y + radius/2, radius/2);
    drawCircle(x, y - radius/2, radius/2);
 
  }
}
