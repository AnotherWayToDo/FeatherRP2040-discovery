import board
import time
import digitalio
from microcontroller import Pin

flash = digitalio.DigitalInOut(board.D10)
flash.direction = digitalio.Direction.OUTPUT


while(True):
    print("Flash")
    flash.value = True
    time.sleep(0.25)
    flash.value = False    
    time.sleep(5)
