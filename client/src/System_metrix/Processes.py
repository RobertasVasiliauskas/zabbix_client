import psutil
class Processes:
    def __init__(self):
        pass

    @staticmethod
    def get_count_processes():
        """
        Get the number of processes running on the system.
        """

        try:
            return len(psutil.pids())
        except Exception as e:
            raise RuntimeError(f"An error occurred while retrieving process count: {e}")

    @staticmethod
    def get_processes(n: int = None) -> list[dict]:
        """
        Get a list of processes running on the system.
        If n is specified, return only the first n processes.

        :param n: Optional; the number of processes to return.
        :return: A list of dictionaries containing process information.
        """
        processes = []
        try:
            for i, proc in enumerate(psutil.process_iter(['pid', 'name', 'username'])):
                if n is not None and i >= n:
                    break
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
        except Exception as e:
            raise RuntimeError(f"An error occurred while retrieving processes: {e}")

        return processes
