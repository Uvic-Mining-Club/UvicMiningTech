from abc import ABC, abstractmethod

class DisplayInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def update(self):
        pass
