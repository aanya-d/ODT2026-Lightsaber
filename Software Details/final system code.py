#code for LDR on -> push button + neopixel -> LDR off
from machine import Pin
import neopixel
import time

# Initialization
np = neopixel.NeoPixel(Pin(5), 61)
pb = Pin(4, Pin.IN, Pin.PULL_UP)
ldr = Pin(18, Pin.IN)
colour = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 0, 255)]
# 0 = green, 1 = blue, 2 = red, 3 = purple

counter = 0
ldr_sensed = False  # defining the flag to see if ldr has sensed darkness (this  means it's light out- no darkness)
system_on = False #system here means the neopixel turning on when LDR == 1 and switching off otherwise

while True:
    ldr_val = ldr.value()

    if ldr_val == 1 and not system_on:
        print ("darkness detected, system_on")
        # LDR detects darkness and the light system starts
        for i in range(0, 61):
            np[i] = (100, 100, 100)
            np.write()
            time.sleep(0.04)
        ldr_sensed = True #flagged
        system_on = True
#lightsaber switches on with default colour (white)
    
    elif ldr_val == 0 and system_on:
        print ("LDR not detected, system off")
        for i in range(0, 61):
            np[i] = np[i] = (0, 0, 0)
        np.write()
        ldr_sensed = False
        system_on = False
    #if the LDR is uncovered, detects light, the light system switches off

    if ldr_sensed and system_on: 
        # LDR has detected darkness, push button now takes over for different colours
        pb_val = pb.value()
        if pb_val == 0:
            print(counter)
            for i in range(0, 61):
                np[i] = colour[counter]
                np.write()
                time.sleep(0.03) 
            counter = counter + 1
            if counter == 4:
                print("reset")
                counter = 0
