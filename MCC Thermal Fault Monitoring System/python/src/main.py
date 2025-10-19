import time
import numpy as np
import matplotlib.pyplot as plt
from smbus2 import SMBus

# Constants
I2C_BUS = 1
DEVICE_ADDR = 0x33  # MLX90640 default I²C address
FRAME_SIZE = 768
ROWS, COLS = 24, 32  # MLX90640 resolution

# Initialize I2C bus
bus = SMBus(I2C_BUS)

def write_register16(addr, value):
    """Write a 16-bit value to a 16-bit register address."""
    addr_high = (addr >> 8) & 0xFF
    addr_low = addr & 0xFF
    data_high = (value >> 8) & 0xFF
    data_low = value & 0xFF
    bus.write_i2c_block_data(DEVICE_ADDR, addr_high, [addr_low, data_high, data_low])

def read_register16(addr):
    """Read a 16-bit value from a 16-bit register address."""
    addr_high = (addr >> 8) & 0xFF
    addr_low = addr & 0xFF
    bus.write_i2c_block_data(DEVICE_ADDR, addr_high, [addr_low])
    data = bus.read_i2c_block_data(DEVICE_ADDR, 0, 2)
    return (data[0] << 8) | data[1]

def read_frame():
    """Read the entire frame of temperature data from the MLX90640."""
    frame = np.zeros(FRAME_SIZE, dtype=np.uint16)
    for i in range(0, FRAME_SIZE, 2):
        frame[i] = read_register16(0x0400 + i)
        frame[i + 1] = read_register16(0x0400 + i + 1)
    return frame

def process_frame(frame):
    """Convert raw frame data to temperature values in Celsius."""
    # Apply calibration constants and other processing steps here
    # For simplicity, we'll assume the raw values are directly usable
    return frame.reshape((ROWS, COLS))

def save_image(thermal_data, filename="thermal_image.jpg"):
    plt.imshow(thermal_data, cmap='inferno', interpolation='none',
               vmin=np.min(thermal_data), vmax=np.max(thermal_data))  # scale to data
    plt.colorbar(label='Temperature (°C)')
    plt.title("MLX90640 Thermal Image")
    plt.savefig(filename, dpi=200)
    plt.close()
    print(thermal_data)
    print(f"Saved thermal image as {filename}")


if __name__ == "__main__":
    try:
        while True:
            print("Reading frame...")
            raw_frame = read_frame()
            thermal_data = process_frame(raw_frame)
            save_image(thermal_data)
            time.sleep(1)  # Adjust the delay as needed
    except KeyboardInterrupt:
        print("Terminating the program.")
    finally:
        bus.close()
