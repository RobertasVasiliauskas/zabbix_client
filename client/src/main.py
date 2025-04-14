from CPU import CPU
from RAM import RAM

def show_cpu_info():
    cpu_usage = cpu.get_cpu_usage(1)
    per_core_usage = cpu.get_per_core_usage(1)
    load_avg = cpu.get_load_average()

    print(f"\nCPU Metrics:")
    print(f" > Total CPU usage: {cpu_usage:.2f}%")

    print(f" > Per-core usage:")
    for i, core in enumerate(per_core_usage, start=1):
        print(f"   - Core {i}: {core:.2f}%")

    print(f" > Load average (1, 5, 15 min): {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")

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

if __name__ == '__main__':
    cpu = CPU()
    ram = RAM()

    while True:
        try:
            show_cpu_info()
            show_ram_info()

        except NotImplementedError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")