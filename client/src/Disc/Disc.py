import psutil
class Disc:
    def __init__(self):
        pass

    @staticmethod
    def get_usage_per_partition() -> dict:
        """
        Get the disk usage for each partition.
        :return: A dictionary with partition mount points as keys and their usage percentage as values.
        """

        partitions_info = {}
        mounting_points = psutil.disk_partitions()

        for mounting_point in mounting_points:
            try:
                usage = psutil.disk_usage(mounting_point.mountpoint)

                if usage.free != 0:
                    partitions_info[mounting_point.mountpoint] = usage.percent

            except PermissionError:
                print(f"Permission denied for mount point: {mounting_point.mountpoint}")

        return partitions_info

    @staticmethod
    def get_disk_total() -> float:
        """
        Get the total disk space.
        :return: Total disk space in bytes.
        """
        return psutil.disk_usage('/').total

    @staticmethod
    def get_disk_used() -> float:
        """
        Get the used disk space.
        :return: Used disk space in bytes.
        """
        return psutil.disk_usage('/').used

    @staticmethod
    def get_disk_free() -> float:
        """
        Get the free disk space.
        :return: Free disk space in bytes.
        """
        return psutil.disk_usage('/').free

    @staticmethod
    def get_disk_write_rate() -> float:
        """
        Get the disk write rate.
        :return: Disk write rate in bytes per second.
        """
        return psutil.disk_io_counters().write_bytes

    @staticmethod
    def get_disk_read_rate() -> float:
        """
        Get the disk read rate.
        :return: Disk read rate in bytes per second.
        """
        return psutil.disk_io_counters().read_bytes

