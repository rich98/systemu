This Python script is a system monitor that provides real-time information about the computer’s CPU usage, memory usage, disk usage, network activity, and running processes. Here’s a breakdown:

get_size(bytes): This function converts a byte value into a human-readable format. It iterates through units of bytes (from bytes to petabytes) and divides the input value by 1024 until it’s less than 1024, then returns that value with the appropriate unit.

clear_screen(): This function clears the terminal screen. It checks if the operating system is Windows (‘nt’) or not, and uses the appropriate command to clear the screen.

The while True: loop runs indefinitely, updating the system information every 5 seconds (as specified by time.sleep(5)).

CPU Info: This section creates a table using the PrettyTable library to display the current CPU usage as a percentage.

Memory Info: This section retrieves information about the system’s virtual memory using the psutil library, then displays the total, used, and free RAM in a table.

Disk Info: This section retrieves information about the disk usage of the root directory (‘/’) and displays the total, used, and free disk space in a table.

Network Info: This section retrieves network I/O information and displays the total bytes sent and received in a table.

Running Processes Info: This section retrieves information about all running processes and displays their process ID (PID) and name in a table.

The script uses the psutil library to gather system information and the PrettyTable library to format that information for display. It’s a simple but effective way to monitor a computer’s resources in real time.
