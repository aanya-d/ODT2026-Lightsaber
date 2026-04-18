#buzzer

from machine import Pin, PWM
import time 


buzzer = PWM(Pin(23), freq = 1000, duty = 0)

def whoosh():
    # Fade in (low → high frequency)
    for freq in range(200, 2000, 20):
        buzzer.freq(freq)
        buzzer.duty(512) 
        time.sleep(0.002)
    
    # Fade out (high → low frequency)
    for freq in range(2000, 200, -20):
        buzzer.freq(freq)
        buzzer.duty(512)
        time.sleep(0.002)
    
    buzzer.duty(0)  # turn off 

while True:
    whoosh()
    time.sleep(1)
