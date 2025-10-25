import numpy as np
from datetime import datetime


class ThermalFaultDetector:
    def __init__(self, camera):
        self.camera = camera
        self.has_faults = False

    def detect_faults(self, threshold=40):
        # Detect if any thermal faults exceed the given threshold temperature (°C) returns True/False
        self.camera.capture_image([0]*768)
        latest_image = self.camera.get_latest_image()
        self.has_faults = np.any(latest_image > threshold)
        return self.has_faults

    def log(self, filename="fault_log.txt"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as f:
            f.write(f"{timestamp} - Fault detected: {self.has_faults} - Tempature Range: {self.get_average_temperature} - Tempature Average: {self.get_average_temperature()}\n")

    def get_average_temperature(self):
        lastest_image = self.camera.get_latest_image()
        return np.mean(lastest_image)

    def get_temperature_range(self):
        lastest_image = self.camera.get_latest_image()
        return f"Min: {np.min(lastest_image)} , Max: {np.max(lastest_image)}"