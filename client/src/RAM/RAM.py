import psutil

class RAM:
    def __init__(self):
        pass

    @staticmethod
    def get_total_memory():
        """
        Get the total memory of the system.
        """
        return psutil.virtual_memory().total

    @staticmethod
    def get_available_memory():
        """
        Get the available memory of the system.
        """
        return psutil.virtual_memory().available

    @staticmethod
    def get_used_memory():
        """
        Get the used memory of the system.
        """
        return psutil.virtual_memory().used