from netmiko import Netmiko

# Number of routers
total_routers = 3  # Adjust as needed

devices = []
for n in range(1, total_routers + 1):
    device = {
        "device_type": "cisco_ios",
        "ip": f"192.168.1.10{n}",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
    devices.append(device)

for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show version")
        net_connect.disconnect()

        # Extract uptime
        if "uptime is" in output:
            uptime_line = [line for line in output.splitlines() if "uptime is" in line]
            if uptime_line:
                print(f"{device['ip']} => {uptime_line[0]}")

        # Extract Configuration Register
        if "Configuration register is" in output:
            config_line = [line for line in output.splitlines() if "Configuration register is" in line]
            if config_line:
                print(f"{device['ip']} => {config_line[0]}")

        print('-' * 60)

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

