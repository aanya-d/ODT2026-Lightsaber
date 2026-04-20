from machine import Pin
import neopixel
import random
import time

#initialization
np = neopixel.NeoPixel(Pin(4), 16)
pb = Pin(21, Pin.IN, Pin.PULL_UP) 

colour = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 0, 255)]
# 0 = green, 1 = blue, 2 = red, 3 = purple
#print(colour)

counter = 0
#initial counter value (unpressed)

while True:
    pb_val = pb.value()
    if pb_val == 0:
        print(counter)
        for i in range(0, 16):
            np[i] = colour[counter]
            np.write()
            time.sleep(0.2)
        counter = counter + 1
    if counter == 4:
        print("reset")
        counter = 0
