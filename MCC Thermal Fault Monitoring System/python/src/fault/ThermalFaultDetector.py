import numpy as np
from datetime import datetime
from FaultDetectorInterface import FaultDetectorInterface

class ThermalFaultDetector(FaultDetectorInterface):
    def __init__(self, sensor):
        self.camera = sensor
        self.has_faults = False

    def detect_fault(self, threshold=40):
        # Detect if any thermal faults exceed the given threshold temperature (°C) returns True/False
        self.camera.capture_image([0]*768)
        latest_image = self.camera.get_image_latest()
        self.has_faults = np.any(latest_image > threshold)
        return self.has_faults

    def log_status(self, filename="fault_log.txt"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as f:
            f.write(f"{timestamp} - Fault detected: {self.has_faults} - Tempature Range: {self.get_temperature_range()} - Tempature Average: {self.get_average_temperature()}\n")

    def get_status(self):
        return {"has_faults": self.has_faults,
                "average_temperature": self.get_average_temperature(),
                "temperature_range": self.get_temperature_range()}

    def get_average_temperature(self):
        lastest_image = self.camera.get_image_latest()
        return f"{np.mean(lastest_image):.4f}"

    def get_temperature_range(self):
        lastest_image = self.camera.get_image_latest()
        return f"Min: {np.min(lastest_image):.4f} , Max: {np.max(lastest_image):.4f}"
