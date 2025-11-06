import board
import busio
import adafruit_mlx90640
import matplotlib.pyplot as plt 
import numpy as np
from CameraInterface import CameraInterface

class Camera_MLX90640(CameraInterface):
    def __init__(self,buffer_size=16):
        # Initialize thermal camera
        self.initialize_I2C()
        self.mlx = adafruit_mlx90640.MLX90640(self.i2c)
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
        self.thermal_data = []
        self.buffer_size = buffer_size
        self.buffer = 0

    def initialize_I2C(self):
        # Initialize camera hardware and settings
        self.i2c = busio.I2C(board.SCL, board.SDA)


    def capture_image(self, frame):
        # Capture a new thermal image data
        self.mlx.getFrame(frame)
        reshaped_frame = np.reshape(frame, (24, 32))
        if len(self.thermal_data) < self.buffer_size:
        # Fill buffer initially
            self.thermal_data.append(reshaped_frame)
        else:
        # Overwrite oldest frame when buffer is full
            self.thermal_data[self.buffer % self.buffer_size] = reshaped_frame

        self.buffer += 1
        return self.get_latest_image()

    def save_image(self, filename="thermal_image.jpg", vmin=20, vmax=110):
        # Save the latest thermal image to a file
        plt.imshow(
            self.get_latest_image(),
            cmap='inferno',
            interpolation='none',
            vmin=vmin,
            vmax=vmax
        )
        plt.colorbar(label='Temperature (°C)')
        plt.title("MLX90640 Thermal Image")
        plt.savefig(filename, dpi=200)
        plt.close()

    def get_image_latest(self):
        # Get the most recent thermal image
        return self.thermal_data[(self.buffer - 1) % self.buffer_size]
    
    def get_image_history(self):
        # Get all stored thermal images in the buffer
        return self.thermal_data
        
