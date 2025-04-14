from CPU import CPU

if __name__ == '__main__':
    cpu = CPU()

    while True:
        cpu_usage = cpu.get_cpu_usage(1)
        print(f" > CPU usage: {cpu_usage}%")