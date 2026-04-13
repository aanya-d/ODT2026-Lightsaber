from machine import Pin
import neopixel
import time

# Initialization
np = neopixel.NeoPixel(Pin(4), 16)
pb = Pin(21, Pin.IN, Pin.PULL_UP)
ldr = Pin(15, Pin.IN)
colour = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 0, 255)]
# 0 = green, 1 = blue, 2 = red, 3 = purple

counter = 0
ldr_triggered = False  # Flag to track if LDR has fired

while True:
    ldr_val = ldr.value()

    if ldr_val == 1 and not ldr_triggered:
        # First time darkness detected — set white
        for i in range(0, 16):
            np[i] = (255, 255, 255)
        np.write()
        ldr_triggered = True  # Lock this in, won't run again

    if ldr_triggered:
        # LDR has fired, push button now takes over
        pb_val = pb.value()
        if pb_val == 0:
            print(counter)
            for i in range(0, 16):
                np[i] = colour[counter]
            np.write()
            time.sleep(0.2)  # Debounce
            counter = counter + 1
            if counter == 4:
                print("reset")
                counter = 0
