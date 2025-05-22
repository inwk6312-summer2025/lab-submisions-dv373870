from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
	"ip": "192.168.1.101",
	"username": "student",
	"password": "Meilab123",
	"port": "22",}]
description = 'Description set with Netmiko'
description_config = ["interface GigabitEthernet3", 
			f"description {description}"]

loopback_config = [
    "interface Loopback0",
    "ip address 10.10.10.1 255.255.255.255",
    "description Configured via Netmiko"
]
for device in devices:
	net_connect = Netmiko(**device)
	output = net_connect.send_config_set(loopback_config)
	print(output)
	net_connect.disconnect()
