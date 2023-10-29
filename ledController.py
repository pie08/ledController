#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import random
import math

# LED strip configuration:
LED_COUNT = 150      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, delay=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(delay/1000.0)


def theaterChase(strip, color, delay=50, iterations=1):
    """Movie theater light style chaser animation."""
    # for iteration in range(iterations):
    for q in range(3):
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i+q, color)
        strip.show()
        time.sleep(delay/1000.0)
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i+q, 0)


def police(strip, delay=200):
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(i+1, 0)
        strip.setPixelColor(i, Color(127, 0, 0))
    strip.show()
    time.sleep(delay/1000)
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(i, 0)
        strip.setPixelColor(i+1, Color(0, 0, 127))
    strip.show()
    time.sleep(delay/1000)


def policeFull(strip, delay=200):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
        strip.setPixelColor(i, Color(127, 0, 0))
    strip.show()
    time.sleep(delay/1000)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
        strip.setPixelColor(i, Color(0, 0, 127))
    strip.show()
    time.sleep(delay/1000)


def policeFade(strip, delay=20):
    color = (127, 0, 0)
    for n in range(128):
        if (n < 64):
            color = (127 - n * 2, 0, n * 2)
        else:
            n -= 64
            color = (n * 2, 0, 127 - n * 2)

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(*color))

        strip.show()
        time.sleep(delay/1000)


def twinkle(strip, color, count=3, delay=20):
    strip[0:-1] = 0

    for i in range(count):
        index = random.randrange(0, strip.numPixels())
        strip.setPixelColor(index, color)
        strip.show()

    time.sleep(delay/1000)


def twinkleRandom(strip, count=3, delay=20):
    strip[0:-1] = 0

    for i in range(count):
        index = random.randrange(0, strip.numPixels())
        strip.setPixelColor(index, Color(random.randrange(
            0, 256), random.randrange(0, 256), random.randrange(0, 256)))
        strip.show()

    time.sleep(delay/1000)


def snowSparkle(strip, color, delay=150, speed=100):
    pixel = random.randrange(0, strip.numPixels())
    strip[pixel] = Color(127, 127, 127)
    strip.show()
    time.sleep(delay/1000)
    strip[pixel] = color
    strip.show()
    time.sleep(speed/1000)
    strip[pixel] = 0


def horizontalBounce(strip, color, delayReturn=0, delay=20, length=10):
    for i in range(strip.numPixels() - length):
        strip[0:-1] = 0
        strip[i: i+length] = color
        strip.show()
        time.sleep(delay/1000)

    time.sleep(delayReturn/1000)

    for i in range(strip.numPixels() - length, 0, -1):
        strip[0:-1] = 0
        strip[i: i+length] = color
        strip.show()
        time.sleep(delay/1000)

    time.sleep(delayReturn/1000)


def colorCycle(strip, colors, delay=20):
    for color in colors:
        for i in range(strip.numPixels()):
            strip[i] = color
            strip.show()
            time.sleep(delay/1000)
        time.sleep(delay/1000)


def usaRandom(strip, step=1, fill=False, delay=100):
    colors = [Color(127, 0, 0), Color(127, 127, 127), Color(0, 0, 127)]

    for i in range(0, strip.numPixels(), step):
        randomColor = colors[random.randrange(0, 3)]
        if fill:
            strip[i:i+step] = randomColor
        else:
            strip[i] = randomColor

    strip.show()
    time.sleep(delay/1000)


def breathing(strip, colors, delayExit=0, delay=20):
    for color in colors:
        strip[0:-1] = color

        for i in range(0, 50):
            strip.setBrightness(i)
            strip.show()
            time.sleep(delay/1000)

        time.sleep(delayExit/1000)

        for i in range(50, 0, -1):
            strip.setBrightness(i)
            strip.show()
            time.sleep(delay/1000)

    # reset brightness so effects after this one appear normal
    strip.setBrightness(50)


def breathingRandom(strip, delayExit=0, delay=20):
    strip[0:-1] = Color(random.randrange(0, 127),
                        random.randrange(0, 127), random.randrange(0, 127))

    for i in range(0, 50):
        strip.setBrightness(i)
        strip.show()
        time.sleep(delay/1000)

    time.sleep(delayExit/1000)

    for i in range(50, 0, -1):
        strip.setBrightness(i)
        strip.show()
        time.sleep(delay/1000)

    # reset brightness so effects after this one appear normal
    strip.setBrightness(50)


def backAndForth(strip, color1, color2, delayReturn=0, delay=25):
    for i in range(strip.numPixels()):
        strip[0:i] = color1
        strip[i:-1] = color2
        strip.show()
        time.sleep(delay/1000)
    time.sleep(delayReturn/1000)
    for i in range(strip.numPixels(), 0, -1):
        strip[0:i] = color1
        strip[i:-1] = color2
        strip.show()
        time.sleep(delay/1000)
    time.sleep(delayReturn/1000)


def runningLights(strip, color, precision=2, delay=50):
    # nested for loop because j will actually cause the effect to move
    for j in range(strip.numPixels()):
        # set colors
        for i in range(strip.numPixels()):
            strip[i] = Color(int(((math.sin((i+j)/precision) * 127 + 128)/255) * color.r),
                             int(((math.sin((i+j)/precision) * 127 + 128)/255) * color.g),
                             int(((math.sin((i+j)/precision) * 127 + 128)/255) * color.b))
        strip.show()
        time.sleep(delay/1000)


def meteor(strip, color, decay=150, size=3, delay=30):
    strip[0:-1] = 0

    for i in range(strip.numPixels()):
        # fade all pixels one step
        for j in range(strip.numPixels()):
            # random chance to not decrease this pixels brightness
            if random.randrange(0, 10) >= 5:
                continue
            r = RGBW(strip.getPixelColor(j)).r
            g = RGBW(strip.getPixelColor(j)).g
            b = RGBW(strip.getPixelColor(j)).b

            # decreasing the brightness
            r = 0 if r <= 10 else (r * decay) // 255
            g = 0 if g <= 10 else (g * decay) // 255
            b = 0 if b <= 10 else (b * decay) // 255

            strip.setPixelColor(j, Color(r, g, b))

        # draw meteor
        for j in range(size):
            if i - j >= 0 and i - j <= strip.numPixels():
                strip[i-j] = color

        strip.show()
        time.sleep(delay/1000)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        # fade from red to blue
        return Color(255 - pos * 3, 0, pos * 3)
    elif pos < 170:
        # fade from blue to green
        pos -= 85
        return Color(0, pos * 3, 255 - pos * 3)
    else:
        # fade from green to red
        pos -= 170
        return Color(pos * 3, 255 - pos * 3, 0)


def rainbow(strip, delay=20):
    """Draw rainbow that fades across all pixels at once."""
    # loop 256 times because to return to original color you need to loop 255 times
    for j in range(256):
        for i in range(strip.numPixels()):
            strip[i] = wheel((i+j) % 255)
        strip.show()
        time.sleep(delay/1000.0)


def rainbowCycle(strip, delay=20):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(j))
        strip.show()
        time.sleep(delay/1000)


def theaterChaseRainbow(strip, delay=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(delay/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def colorFromArray(arr):
    return Color(arr[0], arr[1], arr[2])


if __name__ == 'ledController':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip, 0)