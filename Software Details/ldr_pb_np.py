from machine import Pin
import neopixel
import time

# Initialization
np = neopixel.NeoPixel(Pin(4), 60)
pb = Pin(21, Pin.IN, Pin.PULL_UP)
ldr = Pin(15, Pin.IN)
colour = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 0, 255)]
# 0 = green, 1 = blue, 2 = red, 3 = purple

counter = 0
ldr_sensed = False  # defining the flag to see if ldr has sensed darkness (this  means it's light out- no darkness)

while True:
    ldr_val = ldr.value()

    if ldr_val == 1 and not ldr_sensed:
        # Darkness detected -> lightsaber on -> set default colour to white
        for i in range(0, 61):
            np[i] = (255, 255, 255)
        np.write()
        ldr_sensed = True  # now flagged

    if ldr_sensed:
        # LDR has fired, push button now takes over
        pb_val = pb.value()
        if pb_val == 0:
            print(counter)
            for i in range(0, 61):
                np[i] = colour[counter]
            np.write()
            time.sleep(0.02) 
            counter = counter + 1
            if counter == 4:
                print("reset")
                counter = 0
