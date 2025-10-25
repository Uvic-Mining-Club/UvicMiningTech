from camera import Camera_MLX90640
from fault.ThermalFaultDetector import ThermalFaultDetector

def main():
    # Initialize camera
    camera = Camera_MLX90640(buffer_size=16)

    # Initialize fault detector
    fault_detector = ThermalFaultDetector(camera)

    while(True):
        fault_detector.detect_faults(threshold=40)
        fault_detector.log()
        if fault_detector.has_faults:
            print("Fault detected!")
            fault_detector.camera.save_image(filename="fault_thermal_image.jpg")
            break
        else:
            print("No faults detected.")
        