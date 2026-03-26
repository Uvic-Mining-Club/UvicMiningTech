import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt


TEMPATURE_GPIO = board.D27 #Physical pin 38, GPIO20, for temperature sensor

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

#Polling Buttons that are Active high

BUTTON_1_GPIO = board.D28
BUTTON_2_GPIO = board.D29
button_1 = digitalio.DigitalInOut(BUTTON_1_GPIO)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.UP
button_2 = digitalio.DigitalInOut(BUTTON_2_GPIO)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.UP
print(f"GPIO pins {BUTTON_1_GPIO} and {BUTTON_2_GPIO} initialized for button inputs.")
print("Polling buttons for 10 seconds. Press Button 1 or Button 2 to test.")
start_time = time.time()
while time.time() - start_time < 10:
    if not button_1.value:
        print("Button 1 Pressed!")
    if not button_2.value:
        print("Button 2 Pressed!")
    time.sleep(0.1)
    





