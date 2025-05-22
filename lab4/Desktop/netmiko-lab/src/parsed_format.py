from netmiko import Netmiko

# List of all router devices in your topology
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },
      {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },

    # Add more routers as needed
]

# Loop through each router and print its interfaces
for router in routers:
    print(f"\nConnecting to router: {router['ip']}")

    try:
        net_connect = Netmiko(**router)

        # Run 'show ip interface brief' and parse output
        output = net_connect.send_command("show ip interface brief", use_textfsm=True)

        print("Interfaces:")
        for interface in output:
            print(f" - {interface['interface']}")

        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {router['ip']}: {e}")

