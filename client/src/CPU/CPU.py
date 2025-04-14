import psutil


class CPU:
    def __init__(self):
        pass

    @staticmethod
    def get_cpu_usage(interval: int) -> float:
        """
        Get the CPU usage percentage.
        :param interval: Time interval in seconds
        :return: CPU usage percentage
        """
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_load_average() -> tuple:
        """
        Get the load average for the CPU.
        :return: Load average as a tuple (1 min, 5 min, 15 min)
        """
        return psutil.getloadavg()
