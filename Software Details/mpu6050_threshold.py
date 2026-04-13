from machine import SoftI2C, Pin
from mpu6050 import MPU6050
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpu = MPU6050(i2c)

while True:
    gyro = mpu.get_gyro_data()
    print(gyro)
    time.sleep(2)
