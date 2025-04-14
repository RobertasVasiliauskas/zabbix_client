from CPU import CPU

if __name__ == '__main__':
    cpu = CPU()

    while True:
        cpu_usage = cpu.get_cpu_usage(1)
        load_avg = cpu.get_load_average()

        print(f" > CPU usage: {cpu_usage}%")
        print(f" > Load average: {load_avg[0]}, {load_avg[1]}, {load_avg[2]}")