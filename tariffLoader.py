from abc import ABC, abstractmethod
from tariff import *

class TariffLoader(ABC):
    @abstractmethod
    def load_tariffes(self):
        pass


class TariffMemoryLoader(TariffLoader):
    def load_tariffes(self):
        tariffes = [Tariff(15, 0), Tariff(60, 50), Tariff(120, 100), Tariff(180, 140)]
        return tariffes