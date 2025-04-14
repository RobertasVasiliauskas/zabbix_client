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
        try:
            theoretical_memory = psutil.virtual_memory().total
            return 2 ** math.ceil(math.log2(theoretical_memory))
        except AttributeError:
            raise NotImplementedError("Theoretical memory calculation is not supported on this system.")

    @staticmethod
    def get_total_memory() -> float:
        """
        Get the total memory of the system.
        """
        try:
            return psutil.virtual_memory().total
        except AttributeError:
            raise NotImplementedError("Total memory calculation is not supported on this system.")

    @staticmethod
    def get_available_memory() -> float:
        """
        Get the available memory of the system.
        """
        try:
            return psutil.virtual_memory().available
        except AttributeError:
            raise NotImplementedError("Available memory calculation is not supported on this system.")

    @staticmethod
    def get_used_memory() -> float:
        """
        Get the used memory of the system.
        """
        try:
            return psutil.virtual_memory().used
        except AttributeError:
            raise NotImplementedError("Used memory calculation is not supported on this system.")