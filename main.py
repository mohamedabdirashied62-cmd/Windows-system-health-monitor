import platform
import socket
import psutil


def main():
    print("=" * 45)
    print("WINDOWS SYSTEM HEALTH MONITOR")
    print("=" * 45)

    # Collect basic computer information
    computer_name = socket.gethostname()
    operating_system = platform.system()
    os_version = platform.release()

    # Measure CPU utilization over one second
    cpu_usage = psutil.cpu_percent(interval=1)

    # Collect physical memory information
    memory = psutil.virtual_memory()
    total_ram = round(memory.total / (1024 ** 3), 2)
    available_ram = round(memory.available / (1024 ** 3), 2)
    ram_usage = memory.percent

    # Display computer information
    print(f"\nComputer Name: {computer_name}")
    print(f"Operating System: {operating_system}")
    print(f"OS Version: {os_version}")

    # Display CPU information
    print("\n--- CPU MONITORING ---")
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage >= 85:
        print("CPU Status: WARNING")
    else:
        print("CPU Status: OK")

    # Display memory information
    print("\n--- MEMORY MONITORING ---")
    print(f"Total RAM: {total_ram} GB")
    print(f"Available RAM: {available_ram} GB")
    print(f"RAM Usage: {ram_usage}%")
    if ram_usage >= 85:
        print("RAM Status: WARNING")
    else:
        print("RAM Status: OK")

    # Display disk information
    print("\n--- DISK MONITORING ---")
    for partition in psutil.disk_partitions():
        try:
            disk = psutil.disk_usage(partition.mountpoint)
            total_disk = round(disk.total / (1024 ** 3), 2)
            free_disk = round(disk.free / (1024 ** 3), 2)
            disk_usage = disk.percent

            print(f"\nDrive: {partition.device}")
            print(f"Total Space: {total_disk} GB")
            print(f"Free Space: {free_disk} GB")
            print(f"Disk Usage: {disk_usage}%")

            if disk_usage >= 90:
                print("Disk Status: WARNING")
            else:
                print("Disk Status: OK")

        except OSError as error:
            # Safely handle unready drives (like empty card readers/CD drives)
            if getattr(error, "winerror", None) == 21:
                print(f"\nDrive: {partition.device} - Skipped (Device not ready)")
            else:
                print(f"\nCould not check {partition.device}: {error}")

    # Completion message properly placed at the very end
    print("\n" + "=" * 45)
    print("MONITORING COMPLETED")
    print("=" * 45)


if __name__ == "__main__":
    main()