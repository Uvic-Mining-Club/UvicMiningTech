import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768  # 32*24 pixels

while True:
    try:
        mlx.getFrame(frame)
        thermal_data = np.reshape(frame, (24, 32))  # Rows x Cols

        # Plot and save image
        plt.imshow(thermal_data, cmap='inferno', interpolation='none')
        plt.colorbar(label='Temperature (°C)')
        plt.title("MLX90640 Thermal Image")
        plt.savefig("thermal_image.jpg", dpi=200)
        plt.close()
        print("Saved thermal_image.jpg")

        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting.")
        break

