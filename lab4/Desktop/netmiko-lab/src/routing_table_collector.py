from netmiko import ConnectHandler
import yaml
import textfsm
from io import StringIO

# Load YAML
with open("network_topology.yaml") as file:
    topology = yaml.safe_load(file)

device_template = {
    "device_type": "cisco_ios",
    "username": "student",
    "password": "Meilab123",
    "port": 22,
}

for router, data in topology["routers"].items():
    try:
        print(f"Collecting routes from {router}")
        device = device_template.copy()
        device["ip"] = data["interfaces"][list(data["interfaces"].keys())[0]].split("/")[0]

        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show ip route", use_textfsm=True)
        for route in output:
            print(route)
        net_connect.disconnect()

    except Exception as e:
        print(f"Error on {router}: {e}")

