////////// PEW! PEW! LIGHTS! //////////////////////
///////////// Choo-Choo Train Lights? /////////////
///////////////// I dunno... //////////////////////
// This project was done with an Arduino Nano v3, a
// WS2812B light strip, and the FastLED library.
// Arduino IDE version 1.8.13
// NUM_LEDS/(BLOCK_SIZE + GAP_SIZE) must divide evenly
// with no remainder for this code to work properly.
// BLOCK_SIZE and GAP_SIZE may be adjusted following this
// constraint. DELAY_TIME may be adjusted as well.
// Colors RED, GREEN, and BLUE may be adjusted along
// with RED_GAP, GREEN_GAP, and BLUE_GAP. 
// If NUM_LEDS is greater than 60, depending on how
// small the values for BLOCK_SIZE and GAP_SIZE are,
// More 'if' statements may need to be copy/pasted for
// the 'STARTUP STATE' of the code to work properly.
// YouTube.com/LifeMeetLightning
///////////////////////////////////////////////////
#include <FastLED.h>    //Need the FastLED library! 
#define NUM_LEDS 60     //How many lights are on your light strip.
#define DATA_PIN 2      //Which pin on your arduino is sending out light strip data.
#define COLOR_ORDER GRB //Green (G), Red (R), Blue (B).
#define CHIPSET WS2812B //What type of light strip you are using.
#define BRIGHTNESS 60   //How bright your light strip will display. 
#define VOLTS 5         //Working voltage of your light strip.
#define MAX_AMPS 500    //Limits how much current your light strip will draw.
                        //This setting overides the BRIGHTNESS setting.
                        
//////////Adjustable Section//////////
uint8_t BLOCK_SIZE = 5;    //How long the light blocks are.
uint8_t GAP_SIZE = 10;     //How long the gaps between light blocks are.
uint16_t DELAY_TIME = 50;   //How fast the blocks travel down the light strip.
uint8_t RED = 0;           //Mix and match these color values in the range of
uint8_t GREEN = 0;       //0 to 255 to customize the color of your 
uint8_t BLUE = 255;          //light blocks.
uint8_t RED_GAP = 0;       //I meant these to be 'Black' (values of 0) for
uint8_t GREEN_GAP = 0;     //the gaps between light blocks, but they can be
uint8_t BLUE_GAP = 0;      //colored as well! Woot! Options. 
//////////////////////////////////////
//Fun variables!
uint16_t inc = 0;           //Unsigned 16 bit integer used in 'startup' section.
uint16_t leap = 0;          //Ha ha. Cute. Leap frog!
uint16_t frog = 0;          //These are used as counters in the 'running' section. 
bool startup_flag = true;   //Toggles once to change between startup state and running state.
bool flip_flop = true;      //Toggles between two 'while' loops in running section.
                            //Necessary for 'frame' changes between blocks and gaps.
CRGB leds[NUM_LEDS];        //Array declaration in the CRGB type.

void setup() {
//FastLED setup nonsense. 
FastLED.addLeds<CHIPSET,DATA_PIN,COLOR_ORDER>(leds,NUM_LEDS);
FastLED.setMaxPowerInVoltsAndMilliamps(VOLTS,MAX_AMPS);
FastLED.setBrightness(BRIGHTNESS);
FastLED.clear();
FastLED.show();
}
void loop() { 
////////////STARTUP STATE//////////////
/*
 *Current startup state code below can handle block size
 *and gap size down to values of 2 on a 60 led strip,
 *4 on a 120 led strip, 8 on a 240 led strip, etc. 
 *If longer light strip is used and lower block/gap
 *sizes are desired, 'if' statements below will
 *need to be extended in the same pattern as shown.
 *
 *The startup section is just for aesthetic
 *purposes and can be by-passed by setting startup_flag
 *to false in the declarations section above.
 *This will negate the block size and gap size length
 *restrictions based on light strip length.
 *
 *Startup section writes out blocks and gaps from the
 *beginning of the light strip until the
 *light strip is filled and then moves into the 
 *'running' section.  
*/
  if (startup_flag == true) {
    
    leds[inc].setRGB(RED,GREEN,BLUE);
    if (inc>=BLOCK_SIZE) {
      leds[inc-BLOCK_SIZE].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=BLOCK_SIZE+GAP_SIZE) {
      leds[inc-(BLOCK_SIZE+GAP_SIZE)].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*2)+GAP_SIZE) {
      leds[inc-((BLOCK_SIZE*2)+GAP_SIZE)].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*2)+(GAP_SIZE*2)) {
      leds[inc-((BLOCK_SIZE*2)+(GAP_SIZE*2))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*3)+(GAP_SIZE*2)) {
      leds[inc-((BLOCK_SIZE*3)+(GAP_SIZE*2))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*3)+(GAP_SIZE*3)) {
      leds[inc-((BLOCK_SIZE*3)+(GAP_SIZE*3))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*4)+(GAP_SIZE*3)) {
      leds[inc-((BLOCK_SIZE*4)+(GAP_SIZE*3))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*4)+(GAP_SIZE*4)) {
      leds[inc-((BLOCK_SIZE*4)+(GAP_SIZE*4))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*5)+(GAP_SIZE*4)) {
      leds[inc-((BLOCK_SIZE*5)+(GAP_SIZE*4))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*5)+(GAP_SIZE*5)) {
      leds[inc-((BLOCK_SIZE*5)+(GAP_SIZE*5))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*6)+(GAP_SIZE*5)) {
      leds[inc-((BLOCK_SIZE*6)+(GAP_SIZE*5))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*6)+(GAP_SIZE*6)) {
      leds[inc-((BLOCK_SIZE*6)+(GAP_SIZE*6))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*7)+(GAP_SIZE*6)) {
      leds[inc-((BLOCK_SIZE*7)+(GAP_SIZE*6))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*7)+(GAP_SIZE*7)) {
      leds[inc-((BLOCK_SIZE*7)+(GAP_SIZE*7))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*8)+(GAP_SIZE*7)) {
      leds[inc-((BLOCK_SIZE*8)+(GAP_SIZE*7))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*8)+(GAP_SIZE*8)) {
      leds[inc-((BLOCK_SIZE*8)+(GAP_SIZE*8))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*9)+(GAP_SIZE*8)) {
      leds[inc-((BLOCK_SIZE*9)+(GAP_SIZE*8))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*9)+(GAP_SIZE*9)) {
      leds[inc-((BLOCK_SIZE*9)+(GAP_SIZE*9))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*10)+(GAP_SIZE*9)) {
      leds[inc-((BLOCK_SIZE*10)+(GAP_SIZE*9))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*10)+(GAP_SIZE*10)) {
      leds[inc-((BLOCK_SIZE*10)+(GAP_SIZE*10))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*11)+(GAP_SIZE*10)) {
      leds[inc-((BLOCK_SIZE*11)+(GAP_SIZE*10))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*11)+(GAP_SIZE*11)) {
      leds[inc-((BLOCK_SIZE*11)+(GAP_SIZE*11))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*12)+(GAP_SIZE*11)) {
      leds[inc-((BLOCK_SIZE*12)+(GAP_SIZE*11))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*12)+(GAP_SIZE*12)) {
      leds[inc-((BLOCK_SIZE*12)+(GAP_SIZE*12))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*13)+(GAP_SIZE*12)) {
      leds[inc-((BLOCK_SIZE*13)+(GAP_SIZE*12))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*13)+(GAP_SIZE*13)) {
      leds[inc-((BLOCK_SIZE*13)+(GAP_SIZE*13))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*14)+(GAP_SIZE*13)) {
      leds[inc-((BLOCK_SIZE*14)+(GAP_SIZE*13))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*14)+(GAP_SIZE*14)) {
      leds[inc-((BLOCK_SIZE*14)+(GAP_SIZE*14))].setRGB(RED,GREEN,BLUE);
    }
    if (inc>=(BLOCK_SIZE*15)+(GAP_SIZE*14)) {
      leds[inc-((BLOCK_SIZE*15)+(GAP_SIZE*14))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
    }
    if (inc>=(BLOCK_SIZE*15)+(GAP_SIZE*15)) {
      leds[inc-((BLOCK_SIZE*15)+(GAP_SIZE*15))].setRGB(RED,GREEN,BLUE);
    }
     
    FastLED.show();
    delay(DELAY_TIME);
    inc++;
       
    if (inc>=NUM_LEDS){
      startup_flag = false;
      inc=0;
    }
    
  }

////////////RUNNING STATE/////////////
/*  
 *The running state occurs once the entire light strip
 *has been filled with blocks and gaps. The running  
 *section looks at each 'frame' of one block and one
 *gap down the length of the light strip and flip flops
 *them. Once the block and gap in each frame has been
 *reversed, it flip flops them again giving the illusion
 *of the entire string of light blocks moving down the light strip.
 */
  if (startup_flag == false) {    //No longer in start up state. Move on to running state.
  
    while (true) {    //While(true) jumps us into a permanent while loop for our running state.
      while (flip_flop == true) {
        
        for (int i=0; i<(NUM_LEDS/(GAP_SIZE+BLOCK_SIZE)); i++) {                            
   
          //Writes black the trailing light in each block in each frame down the light strip.
          leds[(leap+(GAP_SIZE*(i+1))+(BLOCK_SIZE*i))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);   
          //Turns on the LED's in the beginning of each frame with each iteration continuing the lights from the frame before it.
          leds[(leap+((BLOCK_SIZE+GAP_SIZE)*i))].setRGB(RED,GREEN,BLUE); 
                               
        }
        
        FastLED.show();
        delay(DELAY_TIME);
        
        leap++;                 
         
        if (leap >= BLOCK_SIZE) {
          flip_flop=!flip_flop;
          leap = 0;
        }
        
      }
      
/*
*Leap_count keeps track of each cycle writing one LED on in each frame
*and one LED off. When the 'if' condition above is met, the frames
*will have been flip flopped so that now each frame ends with off
*LED's and begins with on LED's. At this point, we change the
*state of our flip_flop variable to false which will make us progress
*to the next 'while' loop. The leap variable is
*reset. 
*/
      while (flip_flop == false) {
/*
*This while loop progresses the block lights through the frames
*and turns off the trailing lights until we end up in the same state
*we started in at the beginning of the permanent 'running' state loop.
*Then it changes the state of our flip_flop variable and resets the frog
*variable to start the cycle over again. 
*/
        for (int i=0; i<(NUM_LEDS/(GAP_SIZE+BLOCK_SIZE)); i++) { 
                        
          // Turns on the next LED in each block in each frame until the LED's have progressed through the GAP_SIZE and back to original starting state.
          leds[(frog+(BLOCK_SIZE*(i+1))+(GAP_SIZE*i))].setRGB(RED,GREEN,BLUE);
            
          //Turns off the trailing LED in each block in each frame until GAP_SIZE has been met. 
          leds[(frog+((BLOCK_SIZE+GAP_SIZE)*i))].setRGB(RED_GAP,GREEN_GAP,BLUE_GAP);
            
        }
                                                                              
        FastLED.show();
        delay(DELAY_TIME);
        
        frog++;
        if (frog >= GAP_SIZE) {
          flip_flop=!flip_flop;
          frog = 0;       
        }
            
      }
    }
  }
}