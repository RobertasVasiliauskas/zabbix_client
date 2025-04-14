import psutil
from typing import List, Tuple


class CPU:
    def __init__(self):
        pass

    @staticmethod
    def get_cpu_usage(interval: int) -> float:
        """
        Get the CPU usage percentage over a specified interval.

        :param interval: Time interval in seconds to calculate CPU usage.
        :return: CPU usage percentage as a float.
        """
        try:
            return psutil.cpu_percent(interval=interval)
        except AttributeError:
            raise NotImplementedError("CPU usage is not supported on this platform.")

    @staticmethod
    def get_per_core_usage(interval: int) -> List[float]:
        """
        Get the CPU usage percentage for each core over a specified interval.

        :param interval: Time interval in seconds to calculate per-core CPU usage.
        :return: List of CPU usage percentages for each core.
        """
        try:
            return psutil.cpu_percent(interval=interval, percpu=True)
        except AttributeError:
            raise NotImplementedError("Per-core CPU usage is not supported on this platform.")

    @staticmethod
    def get_load_average() -> Tuple[float, float, float]:
        """
        Get the system load average over the last 1, 5, and 15 minutes.

        :return: A tuple containing the load averages (1 min, 5 min, 15 min).
        :raises NotImplementedError: If the platform does not support load averages.
        """
        try:
            return psutil.getloadavg()
        except AttributeError:
            raise NotImplementedError("Load average is not supported on this platform.")