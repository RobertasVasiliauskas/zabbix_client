from CPU import CPU

if __name__ == '__main__':
    cpu = CPU()

    while True:
        try:
            cpu_usage = cpu.get_cpu_usage(1)
            per_core_usage = cpu.get_per_core_usage(1)
            load_avg = cpu.get_load_average()

            print(f"\nCPU Metrics:")
            print(f" > Total CPU usage: {cpu_usage:.2f}%")

            print(f" > Per-core usage:")
            for i, core in enumerate(per_core_usage, start=1):
                print(f"   - Core {i}: {core:.2f}%")

            print(f" > Load average (1, 5, 15 min): {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")

        except NotImplementedError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")