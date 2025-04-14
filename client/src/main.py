from System_metrix import CPU, RAM, Disc, Processes

def show_cpu_info():
    cpu_usage = cpu.get_cpu_usage(1)
    per_core_usage = cpu.get_per_core_usage(1)
    load_avg = cpu.get_load_average()

    print(f"\nCPU Metrics:")
    print(f" > Total CPU usage: {cpu_usage:.2f}%")

    print(f" > Per-core usage:")
    print(f" > Load average (1, 5, 15 min): {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")
    print(f"{'index'.ljust(10)}{'Usage (%)'.ljust(15)}")
    print("-" * 25)
    for i, core in enumerate(per_core_usage, start=1):
        print(f"{f'Core {i}'.ljust(10)}{core:.2f}%".ljust(15))

def show_ram_info():
    theoretical_memory = ram.get_theoretical_memory()
    total_memory = ram.get_total_memory()
    free_memory = ram.get_available_memory()
    used_memory = ram.get_used_memory()

    print(f"\nRAM Metrics:")
    print(f" > Theoretical memory size: {theoretical_memory/ (1024 ** 3)} GB")
    print(f" > Total usable RAM size: {total_memory / (1024 ** 3):.2f} GB")
    print(f" > Free RAM size: {free_memory / (1024 ** 3):.2f} GB")
    print(f" > Used RAM size: {used_memory / (1024 ** 3):.2f} GB")

def show_disk_info():
    total_disk = disc.get_disk_total()
    used_disk = disc.get_disk_used()
    free_disk = disc.get_disk_free()
    partitions = disc.get_usage_per_partition()
    disk_write_rate = disc.get_disk_write_rate()
    disk_read_rate = disc.get_disk_read_rate()

    print(f"\nDisk Metrics:")
    print(f" > Total disk space: {total_disk / (1024 ** 3):.2f} GB")
    print(f" > Used disk space: {used_disk / (1024 ** 3):.2f} GB")
    print(f" > Free disk space: {free_disk / (1024 ** 3):.2f} GB")
    print(f" > Disk write rate: {disk_write_rate / (1024 ** 3):.2f} GB/s")
    print(f" > Disk read rate: {disk_read_rate / (1024 ** 3):.2f} GB/s")

    print(f"{'Mount Point'.ljust(30)}{'Usage (%)'.ljust(15)}")
    print("-" * 45)
    for mount_point, usage in partitions.items():
        print(f"{mount_point.ljust(30)}{usage:.2f}%")


def show_processes_info():
    count_processes = processes.get_count_processes()
    processes_list = processes.get_processes(10)

    print(f"\nProcesses Metrics:")
    print(f" > Number of processes: {count_processes}")
    print(f"{'PID'.ljust(10)}{'Name'.ljust(40)}{'User'.ljust(20)}")
    print("-" * 70)
    for proc in processes_list:
        print(f"{str(proc['pid']).ljust(10)}{proc['name'].ljust(40)}{proc['username'].ljust(20)}")


if __name__ == '__main__':

    cpu = CPU()
    ram = RAM()
    disc = Disc()

    while True:
        processes = Processes()

        try:
            show_cpu_info()
            show_ram_info()
            show_disk_info()
            show_processes_info()

        except NotImplementedError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")