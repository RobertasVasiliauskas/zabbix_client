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

        try:
            return partitions_info
        except AttributeError:
            raise NotImplementedError("Disk usage per partition is not supported on this platform.")

    @staticmethod
    def get_disk_total() -> float:
        """
        Get the total disk space.
        :return: Total disk space in bytes.
        """
        try:
            return psutil.disk_usage('/').total
        except AttributeError:
            raise NotImplementedError("Total disk space is not supported on this platform.")

    @staticmethod
    def get_disk_used() -> float:
        """
        Get the used disk space.
        :return: Used disk space in bytes.
        """
        try:
            return psutil.disk_usage('/').used
        except AttributeError:
            raise NotImplementedError("Used disk space is not supported on this platform.")

    @staticmethod
    def get_disk_free() -> float:
        """
        Get the free disk space.
        :return: Free disk space in bytes.
        """
        try:
            return psutil.disk_usage('/').free
        except AttributeError:
            raise NotImplementedError("Free disk space is not supported on this platform.")

    @staticmethod
    def get_disk_write_rate() -> float:
        """
        Get the disk write rate.
        :return: Disk write rate in bytes per second.
        """
        try:
            return psutil.disk_io_counters().write_bytes
        except AttributeError:
            raise NotImplementedError("Disk write rate is not supported on this platform.")

    @staticmethod
    def get_disk_read_rate() -> float:
        """
        Get the disk read rate.
        :return: Disk read rate in bytes per second.
        """
        try:
            return psutil.disk_io_counters().read_bytes
        except AttributeError:
            raise NotImplementedError("Disk read rate is not supported on this platform.")
