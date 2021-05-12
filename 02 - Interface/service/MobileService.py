from abc import ABC, abstractmethod

class MobileService(ABC):

    @abstractmethod
    def updgradeSoftware(self):
        pass

    @abstractmethod
    def upgradeCost(self):
        pass
