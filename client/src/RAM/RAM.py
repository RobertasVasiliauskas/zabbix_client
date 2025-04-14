import math
import psutil

class RAM:
    def __init__(self):
        pass

    @staticmethod
    def get_theoretical_memory() -> float:
        """
        Get the theoretical memory of the system.
        """
        theoretical_memory = psutil.virtual_memory().total
        return 2 ** math.ceil(math.log2(theoretical_memory))

    @staticmethod
    def get_total_memory() -> float:
        """
        Get the total memory of the system.
        """
        return psutil.virtual_memory().total

    @staticmethod
    def get_available_memory() -> float:
        """
        Get the available memory of the system.
        """
        return psutil.virtual_memory().available

    @staticmethod
    def get_used_memory() -> float:
        """
        Get the used memory of the system.
        """
        return psutil.virtual_memory().used