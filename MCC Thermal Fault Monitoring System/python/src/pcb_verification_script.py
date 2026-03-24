import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt


TEMPATURE_GPIO = board.D38 #Physical pin 38, GPIO20, for temperature sensor

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)
# Check whats on the I2C bus
while not i2c.try_lock():
    pass
try:
    print("I2C addresses found:", [hex(device) for device in i2c.scan()])
finally:    i2c.unlock()

# Initialize the SPI
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# Check if SPI is working
while not spi.try_lock():
    pass
try:
    print("SPI devices found:", spi.scan())
finally:    spi.unlock()

# Initialize the GPIO for temperature sensor
import digitalio
temp_sensor_pin = digitalio.DigitalInOut(TEMPATURE_GPIO)
temp_sensor_pin.direction = digitalio.Direction.INPUT
# Check if GPIO is working
print(f"GPIO pin {TEMPATURE_GPIO} initialized for temperature sensor input.")






