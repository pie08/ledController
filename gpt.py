import time
from rpi_ws281x import Adafruit_NeoPixel, Color

# LED strip configuration
LED_COUNT = 30         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the LED data input.
LED_FREQ_HZ = 800000   # LED signal frequency in Hz.
LED_DMA = 10           # DMA channel to use for generating signal.
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest.
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift).

# Number of chaser sections
NUM_SECTIONS = 3

# Initialize the LED strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

# Initialize the library
strip.begin()

try:
    while True:
        # Clear the entire strip
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

        for section in range(NUM_SECTIONS):
            # Chaser pattern for this section
            for i in range(LED_COUNT // NUM_SECTIONS):
                index = section * (LED_COUNT // NUM_SECTIONS) + i
                strip.setPixelColor(index, Color(127, 0, section*75))  # Red color

        strip.show()
        time.sleep(0.1)  # Adjust the speed as needed

        # Clear the entire strip before the next iteration
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

except KeyboardInterrupt:
    # Clear the LED strip and exit
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()