import processing.sound.*;

/**
 * Blade demo
 * modeling blades of grass in the wind
 * 2016-09-08
 * forum.processing.org/two/discussion/comment/74398/
 */
SoundFile file;
FFT fft;
int bands = 512;
float[] spectrum = new float[bands];
float detailLvl = 1;
ArrayList<Blade> bs = new ArrayList<Blade>();
 
void setup(){
  size(200,200);
  fft = new FFT(this, bands);
  file = new SoundFile(this, "angels.mp3");
  file.play();
  fft.input(file);
  //// create new blades of grass
  int bladeCount = 30;
  for(int i=0; i<bladeCount; i++){
    bs.add( new Blade(random(width),float(height),int(random(3,10)),1.0) );
  }
}
void draw(){
  background(0);
  float factor = 0.0;
  fft.analyze();
  for(int i = 0; i < bands; i++){
    factor += fft.spectrum[i];
  }
  factor /= bands;
  for(Blade b : bs){
    //// update each blade from a constant wind source
    
    b.update(-50, height/4, 1.5, 1.5);
    b.draw();
  }
}
 
/** Blade class code from pastebin.com/7YVSNczK */
 
class Blade {
  float anchorx;
  float anchory;
  float offset;
  color green;
  float stiffness;
  ArrayList<PVector> segments;
 
  Blade(float setAnchorx,float setAnchory, int setSegments, float preOffset) {
    anchorx = setAnchorx;
    anchory = setAnchory;
    segments = new ArrayList<PVector>();
    for (int x = 0; x < setSegments; x++) {
      segments.add(new PVector(anchorx, anchory+10*x));
    }
    offset = random(100)/100 + preOffset;
    green = color((int)random(0, 50), (int)random(100, 255), (int)random(0, 100));
    stiffness = random(1, 2);
    //grounding force
    segments.get(0).x = anchorx;
    segments.get(0).y = anchory;
  }
 
  void update(float blowx,float blowy,float forcex,float forcey) {
    //perlin noise wind, slightly offset from every other blade
    float wind = (noise(frameCount/100.0+offset)-0.5);
    //apply forces to each blade segment
    for (int x = 1; x < segments.size (); x++) {
      PVector segment = segments.get(x);
      segment.y -= (((segments.size ()-x)*1)/detailLvl)*stiffness;
      segment.x += x*wind*(4/detailLvl);
      //effect of mouse acceleration
      float secondWind = dist(blowx, blowy, segment.x, segment.y);
      if (secondWind < 100) {
        segment.x += forcex*(20/secondWind*(4/detailLvl));
        segment.y += forcey*(20/secondWind*(4/detailLvl));
      }
    }
    //pull joints together
    for (int x = 0; x < segments.size ()-1; x++) {
      float jointx = segments.get(x).x - segments.get(x+1).x;
      float jointy = segments.get(x).y - segments.get(x+1).y;
      float jointlength = sqrt(jointx*jointx + jointy*jointy);
      if (jointlength > 5*(4/detailLvl)) {
        float tempvar = 1.0/jointlength;
        jointx *= tempvar;
        jointy *= tempvar;
        jointx *= -5*(4/detailLvl);
        jointy *= -5*(4/detailLvl);
        segments.get(x+1).x = segments.get(x).x + jointx;
        segments.get(x+1).y = segments.get(x).y + jointy;
      }
    }
  }
 
  void draw() {
    fill(green);
    stroke(green);
    int h = segments.size()-2;
    beginShape(TRIANGLE_STRIP);
      for (int x = 0; x < segments.size ()-1; x++) {
        float segmentx = segments.get(x).x;
        float segmenty = segments.get(x).y;
        vertex(segmentx+1*(h-x), segmenty);
        vertex(segmentx-1*(h-x), segmenty);
      }
    endShape();
  }
}
