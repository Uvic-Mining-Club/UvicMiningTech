from abc import ABC, abstractmethod

class FaultDetectorInterface(ABC):
    @abstractmethod
    def __init__(self, sensor):
        pass
    
    @abstractmethod
    def detect_fault(self, threshold):
        pass

    @abstractmethod
    def log_status(self, logfile):
        pass
    
    @abstractmethod
    def get_status(self):
        pass