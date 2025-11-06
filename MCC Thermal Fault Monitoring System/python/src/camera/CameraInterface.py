from abc import ABC, abstractmethod

class CameraInterface(ABC):
    @abstractmethod
    def __init__(self, buffer_size):
        pass
    
    @abstractmethod
    def capture_image(self):
        pass

    @abstractmethod
    def get_image_latest(self):
        pass
    
    @abstractmethod
    def save_image(self, filename):
        pass

    @abstractmethod
    def get_image_history(self):
        pass