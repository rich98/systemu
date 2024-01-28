import os
import psutil
import time
from prettytable import PrettyTable

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

while True:
    clear_screen()
    print("----- System Monitor -----")

    # CPU Info
    cpu_table = PrettyTable()
    cpu_table.field_names = ["CPU Usage"]
    cpu_table.add_row([f"{psutil.cpu_percent()}%"])
    print(cpu_table)

    # Memory Info
    memory_info = psutil.virtual_memory()
    memory_table = PrettyTable()
    memory_table.field_names = ["Total RAM", "Used RAM", "Free RAM"]
    memory_table.add_row([f"{get_size(memory_info.total)}", f"{get_size(memory_info.used)}", f"{get_size(memory_info.free)}"])
    print(memory_table)

    # Disk Info
    disk_usage = psutil.disk_usage('/')
    disk_table = PrettyTable()
    disk_table.field_names = ["Total Disk Space", "Used Disk Space", "Free Disk Space"]
    disk_table.add_row([f"{get_size(disk_usage.total)}", f"{get_size(disk_usage.used)}", f"{get_size(disk_usage.free)}"])
    print(disk_table)

    # Network Info
    net_info = psutil.net_io_counters()
    network_table = PrettyTable()
    network_table.field_names = ["Bytes Sent", "Bytes Received"]
    network_table.add_row([f"{get_size(net_info.bytes_sent)}", f"{get_size(net_info.bytes_recv)}"])
    print(network_table)

    # Running Processes Info
    process_table = PrettyTable()
    process_table.field_names = ["PID", "Process Name"]
    for proc in psutil.process_iter(['pid', 'name']):
        process_table.add_row([proc.info['pid'], proc.info['name']])
    print(process_table)

    time.sleep(5)  # Pause for 1 second



