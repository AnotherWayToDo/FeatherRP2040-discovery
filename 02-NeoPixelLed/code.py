import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.25)

RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
    pixels.fill(RED)
    time.sleep(.25)
    pixels.fill(BLUE)
    time.sleep(.25)
